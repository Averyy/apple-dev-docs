# urlSession(_:task:didReceive:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Requests credentials from the delegate in response to an authentication request from the remote server.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, didReceive challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```

#### Discussion

This method handles task-level authentication challenges. The [`URLSessionDelegate`](urlsessiondelegate.md) protocol also provides a session-level authentication delegate method. The method called depends on the type of authentication challenge:

- For session-level challenges—[`NSURLAuthenticationMethodNTLM`](nsurlauthenticationmethodntlm.md), [`NSURLAuthenticationMethodNegotiate`](nsurlauthenticationmethodnegotiate.md), [`NSURLAuthenticationMethodClientCertificate`](nsurlauthenticationmethodclientcertificate.md), or [`NSURLAuthenticationMethodServerTrust`](nsurlauthenticationmethodservertrust.md)—the `NSURLSession` object calls the session delegate’s [`urlSession(_:didReceive:completionHandler:)`](urlsessiondelegate/urlsession(_:didreceive:completionhandler:).md) method. If your app does not provide a session delegate method, the `NSURLSession` object  calls the task delegate’s [`urlSession(_:task:didReceive:completionHandler:)`](urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:).md) method to handle the challenge.
- For non-session-level challenges (all others), the [`URLSession`](urlsession.md) object calls the session delegate’s [`urlSession(_:task:didReceive:completionHandler:)`](urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:).md) method to handle the challenge. If your app provides a session delegate and you need to handle authentication, then you must either handle the authentication at the task level or provide a task-level handler that calls the per-session handler explicitly. The session delegate’s [`urlSession(_:didReceive:completionHandler:)`](urlsessiondelegate/urlsession(_:didreceive:completionhandler:).md) method is  called for non-session-level challenges.

## Parameters

- `session`: The session containing the task whose request requires authentication.
- `task`: The task whose request requires authentication.
- `challenge`: An object that contains the request for authentication.
- `completionHandler`: A handler that your delegate method must call. Its parameters are:

## See Also

- [URLSession.AuthChallengeDisposition](urlsession/authchallengedisposition.md)
  Constants passed by session or task delegates to the provided continuation block in response to an authentication challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:))*