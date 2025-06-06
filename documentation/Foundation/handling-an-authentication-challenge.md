# Handling an authentication challenge

**Framework**: Foundation

Respond appropriately when a server demands authentication for a URL request.

#### Overview

When your app makes a request with a [`URLSessionTask`](urlsessiontask.md), the server may respond with one or more demands for credentials before continuing. The session task attempts to handle this for you. If it can’t, it calls your session’s [`delegate`](urlsession/delegate.md) to handle the challenges.

Implement the delegate methods described in this article to answer challenges issued by a server that your app connects to. If you don’t implement a delegate, your request may be denied by the server, and you receive a response with HTTP status code `401` (Forbidden) instead of the data you expect.

##### Determine the Appropriate Delegate Method

Implement one or both delegate authentication methods, depending on the nature of the challenge(s) you receive.

- Implement the [`urlSession(_:didReceive:completionHandler:)`](urlsessiondelegate/urlsession(_:didreceive:completionhandler:).md) method of [`URLSessionDelegate`](urlsessiondelegate.md) to handle session-wide challenges. These are challenges like Transport Layer Security (TLS) validation. Once you’ve successfully handled this kind of challenge, your action remains in effect for all tasks created from that [`URLSession`](urlsession.md).
- Implement the [`urlSession(_:task:didReceive:completionHandler:)`](urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:).md) method of [`URLSessionTaskDelegate`](urlsessiontaskdelegate.md) to handle task-specific challenges. These are challenges like demands for username/password authentication. Each task created from a given session may issue its own challenges.

> **Note**:  See [`NSURLProtectionSpace authentication method constants`](nsurlprotectionspace-authentication-method-constants.md) for a guide to which authentication methods are session-wide or task-specific.

 See [`NSURLProtectionSpace authentication method constants`](nsurlprotectionspace-authentication-method-constants.md) for a guide to which authentication methods are session-wide or task-specific.

As a simple example, consider what happens when you request an `http` URL protected by HTTP Basic authentication, as defined in [`RFC 7617`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7617). Because this is a task-specific challenge, you handle this by implementing [`urlSession(_:task:didReceive:completionHandler:)`](urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:).md).

> **Note**:  If you connect via `https`, you also receive a server trust challenge. See [`Performing manual server trust authentication`](performing-manual-server-trust-authentication.md) for information on handling this type of session-wide challenge.

 If you connect via `https`, you also receive a server trust challenge. See [`Performing manual server trust authentication`](performing-manual-server-trust-authentication.md) for information on handling this type of session-wide challenge.

[`Figure 1`](url_loading_system/handling_an_authentication_challenge#2948287.md) outlines a strategy for responding to the HTTP Basic challenge.

![Decision tree showing states and choices for handling an authentication challenge. The first decision point is whether the received challenge’s authentication method is HTTP Basic; if not, use system default handling. If so, the user is challenged for username and password. The second decision point asks if the user did provide a username and password. If yes, create and use credential; if not, cancel the challenge.](https://docs-assets.developer.apple.com/published/a70a97e52f61df7e7837448151858330/media-2948287%402x.png)

The following sections implement this strategy.

##### Determine the Type of Authentication Challenge

When you receive an authentication challenge, use your delegate method to determine the type of challenge. The delegate method receives a [`URLAuthenticationChallenge`](urlauthenticationchallenge.md) instance that describes the challenge being issued. This instance contains a [`protectionSpace`](urlauthenticationchallenge/protectionspace.md) property whose [`authenticationMethod`](urlprotectionspace/authenticationmethod.md) property indicates the kind of challenge being issued (such as a request for a username and password, or a client certificate). You use this value to determine whether you can handle the challenge.

You respond to the challenge by directly invoking the completion handler passed in to the challenge, passing an [`URLSession.AuthChallengeDisposition`](urlsession/authchallengedisposition.md) indicating your response to the challenge. You use the disposition argument to provide a credential, cancel the request, or allow the default handling to proceed, whichever is appropriate.

The following example tests the authentication method to see if it is the expected type, HTTP Basic. If the `authenticationMethod` property indicates some other kind of challenge, it calls the completion handler with the [`URLSession.AuthChallengeDisposition.performDefaultHandling`](urlsession/authchallengedisposition/performdefaulthandling.md) disposition. Telling the task to use its default handling may satisfy the challenge; otherwise, the task will move on to the next challenge in the response and call this delegate again. This process continues until the task reaches the HTTP Basic challenge that you expect to handle.

Checking the authentication method of an authentication challenge

```swift
let authMethod = challenge.protectionSpace.authenticationMethod
guard authMethod == NSURLAuthenticationMethodHTTPBasic else {
    completionHandler(.performDefaultHandling, nil)
    return
}
```

##### Create a Credential Instance

To successfully answer the challenge, you need to submit a credential appropriate to type of challenge you have received. For HTTP Basic and HTTP Digest challenges, you provide a username and password. The following example shows a helper method that attempts to create a [`URLCredential`](urlcredential.md) instance from user-interface fields, if they are filled in.

Creating a URLCredential from user interface values

```swift
func credentialsFromUI() -> URLCredential? {
    guard let username = usernameField.text, !username.isEmpty,
        let password = passwordField.text, !password.isEmpty else {
            return nil
    }
    return URLCredential(user: username, password: password,
                         persistence: .forSession)
}
```

In this example, the returned [`URLCredential`](urlcredential.md) has [`URLCredential.Persistence.forSession`](urlcredential/persistence-swift.enum/forsession.md) persistence, so it’s only stored by the [`URLSession`](urlsession.md) instance that created the task. You would need to supply new [`URLCredential`](urlcredential.md) instances for tasks created by other session instances, and on future runs of the app.

##### Call the Completion Handler

Once you’ve tried to create a credential instance, you must call the completion handler to answer the challenge.

- If you can’t create a credential, or if the user explicitly canceled, call the completion handler and pass the [`URLSession.AuthChallengeDisposition.cancelAuthenticationChallenge`](urlsession/authchallengedisposition/cancelauthenticationchallenge.md) disposition.
- If you can create a credential instance, use the [`URLSession.AuthChallengeDisposition.useCredential`](urlsession/authchallengedisposition/usecredential.md) disposition to pass it to the completion handler.

The following example shows both these options.

Invoking the authentication challenge completion Handler

```swift
guard let credential = credentialOrNil else {
    completionHandler(.cancelAuthenticationChallenge, nil)
    return
}
completionHandler(.useCredential, credential)
```

If you supply a credential that is accepted by the server, the task begins uploading or downloading data.

> ❗ **Important**:  You can pass the completion handler to other methods or temporarily store it in a property, for situations like waiting for the user to complete a username/password dialog. But eventually you must call the completion handler to complete the challenge and allow the task to proceed, even if you’re choosing to cancel, as seen in the failure case of the previous example.

 You can pass the completion handler to other methods or temporarily store it in a property, for situations like waiting for the user to complete a username/password dialog. But eventually you must call the completion handler to complete the challenge and allow the task to proceed, even if you’re choosing to cancel, as seen in the failure case of the previous example.

##### Handle Failures Gracefully

If the credential is refused, the system calls your delegate method again. When this happens, the callback provides your rejected credential as the [`proposedCredential`](urlauthenticationchallenge/proposedcredential.md) property of the [`URLAuthenticationChallenge`](urlauthenticationchallenge.md) parameter. The challenge instance also includes a [`previousFailureCount`](urlauthenticationchallenge/previousfailurecount.md) property, which indicates how many times the credential has been rejected. You can use these properties to determine what to do next. For example, if the [`previousFailureCount`](urlauthenticationchallenge/previousfailurecount.md) is greater than zero, you could use the user string of the [`proposedCredential`](urlauthenticationchallenge/proposedcredential.md) to populate a user/password reentry UI.

## Topics

### Creating URL credentials
- [Performing manual server trust authentication](performing-manual-server-trust-authentication.md)
  Evaluate the server’s security credentials in your app.

## See Also

- [class URLAuthenticationChallenge](urlauthenticationchallenge.md)
  A challenge from a server requiring authentication from the client.
- [class URLCredential](urlcredential.md)
  `A`n authentication credential consisting of information specific to the type of credential and the type of persistent storage to use, if any.
- [class URLCredentialStorage](urlcredentialstorage.md)
  The manager of a shared credentials cache.
- [class URLProtectionSpace](urlprotectionspace.md)
  A server or an area on a server, commonly referred to as a realm, that requires authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/handling-an-authentication-challenge)*