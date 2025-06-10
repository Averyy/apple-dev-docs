# Performing manual server trust authentication

**Framework**: Foundation

Evaluate the server’s security credentials in your app.

#### Overview

When you use a secure connection (such as `https`) with a URL request, your [`URLSessionDelegate`](urlsessiondelegate.md) receives an authentication challenge with an authentication type of [`NSURLAuthenticationMethodServerTrust`](nsurlauthenticationmethodservertrust.md). Unlike other challenges where the server is asking your app to authenticate itself, this is an opportunity for you to authenticate the server’s credentials.

> 💡 **Tip**:  See [`Handling an authentication challenge`](handling-an-authentication-challenge.md) for an introduction to authentication challenges.

##### Determine When Manual Server Trust Evaluation Is Appropriate

In most cases, you should let the URL Loading System’s default handling evaluate the server trust. You get this behavior when you either don’t have a delegate or don’t handle authentication challenges. However, performing your own evaluation may be useful for scenarios like the following:

- You want to accept server credentials that would otherwise be rejected by the system. For example, your app makes a secure connection to a development server that uses a self-signed certificate, which would ordinarily not match anything in the system’s trust store.
- You want to reject credentials that would otherwise be accepted by the system. For example, you want to “pin” your app to a set of specific keys or certificates under your control, rather than accept any valid credential.

[`Figure 1`](url_loading_system/handling_an_authentication_challenge/performing_manual_server_trust_authentication#2959678.md) illustrates how an app performs manual credential evaluation by providing a delegate method to handle the authentication challenge. This bypasses the default handling. Instead, the delegate directly compares the server certificate or its public key against a copy of the certificate or key (or a hash of either of these) stored in the app bundle itself. If the delegate decides the server credential is valid, it accepts the server trust and allows the connection to continue.

![Flow diagram of a server trust being evaluated manually by a delegate method. A certificate in the server trust matches a certificate inside the app bundle, so the server trust is manually accepted and the flow ends with a “connect” state.](https://docs-assets.developer.apple.com/published/f0b62792d68fe6d5404e22e59c322799/media-2959678%402x.png)

> **Note**:  [`URLSession`](urlsession.md) enforces [`App Transport Security (ATS)`](urlsession#App-Transport-Security-ATS.md), if it is enabled for the domain you are connecting to. This applies security requirements for the certificates, TLS version, and cipher used by the connection. You cannot loosen server trust requirements for an ATS-protected domain, but you can tighten them, using the manual evaluation technique shown in this article. See [`NSAppTransportSecurity`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/NSAppTransportSecurity) in [`Information Property List Key Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247) for further details.

##### Handle Server Trust Authentication Challenges

To perform manual server trust authentication, implement the [`URLSessionDelegate`](urlsessiondelegate.md) method [`urlSession(_:didReceive:completionHandler:)`](urlsessiondelegate/urlsession(_:didreceive:completionhandler:).md). When this method is called, the first things your implementation needs to do are to check that:

- The challenge type is server trust, and not some other kind of challenge.
- The challenge’s host name matches the host that you want to perform manual credential evaluation for.

The following example shows how to test these conditions, given the `challenge` parameter passed to the [`urlSession(_:didReceive:completionHandler:)`](urlsessiondelegate/urlsession(_:didreceive:completionhandler:).md) callback. It gets the challenge’s [`protectionSpace`](urlauthenticationchallenge/protectionspace.md) and uses it to perform the two checks listed above. First, it gets the [`authenticationMethod`](urlprotectionspace/authenticationmethod.md) from the protection space and checks that the type of authentication is [`NSURLAuthenticationMethodServerTrust`](nsurlauthenticationmethodservertrust.md). Then it makes sure the protection space’s [`host`](urlprotectionspace/host.md) matches the expected name `example.com`. If either of these conditions are not met, it calls the `completionHandler` with the [`URLSession.AuthChallengeDisposition.performDefaultHandling`](urlsession/authchallengedisposition/performdefaulthandling.md) disposition to allow the system to handle the challenge.

Testing the challenge type and host name of a server trust authentication challenge.

```swift
let protectionSpace = challenge.protectionSpace
guard protectionSpace.authenticationMethod ==
    NSURLAuthenticationMethodServerTrust,
    protectionSpace.host.contains("example.com") else {
        completionHandler(.performDefaultHandling, nil)
        return
}
```

##### Evaluate the Credential in the Challenge

To access the server’s credential, get the [`serverTrust`](urlprotectionspace/servertrust.md) property (an instance of the [`SecTrust`](https://developer.apple.com/documentation/Security/SecTrust) class) from the protection space. The following example shows how to access the server trust and accept or reject it. The listing starts by attempting to get the [`serverTrust`](urlprotectionspace/servertrust.md) property from the protection space, and falls back to default handling if the property is `nil`. Next, it passes the server trust to a private helper method `checkValidity(of:)` that compares the certificate or public key in the server trust to known-good values stored in the app bundle.

Evaluating credentials in a server trust instance.

```swift
guard let serverTrust = protectionSpace.serverTrust else {
    completionHandler(.performDefaultHandling, nil)
    return
}
if checkValidity(of: serverTrust) {
    let credential = URLCredential(trust: serverTrust)
    completionHandler(.useCredential, credential)
} else {
    // Show a UI here warning the user the server credentials are
    // invalid, and cancel the load.
    completionHandler(.cancelAuthenticationChallenge, nil)
}
```

Once the code determines the validity of the server trust, it takes one of two actions:

- If the server trust’s credential is valid, create a new [`URLCredential`](urlcredential.md) instance from the server trust. Then call the `completionHandler` with the [`URLSession.AuthChallengeDisposition.useCredential`](urlsession/authchallengedisposition/usecredential.md) disposition, passing in the newly-created credential. This tells the system to accept the server’s credentials.
- If the challenge’s credential is invalid, call the `completionHandler` with the [`URLSession.AuthChallengeDisposition.cancelAuthenticationChallenge`](urlsession/authchallengedisposition/cancelauthenticationchallenge.md) disposition. This tells the system to reject the server’s credentials.

> 💡 **Tip**:  See [`Certificate, Key, and Trust Services`](https://developer.apple.com/documentation/Security/certificate-key-and-trust-services) to learn more about how to evaluate a [`SecTrust`](https://developer.apple.com/documentation/Security/SecTrust) instance or access certificates or public keys from it.

##### Create a Long Term Server Authentication Strategy

If you determine that you need to evaluate server trust manually in some or all cases,  plan for what your app will do if you need to change your server credentials. Keep the following guidelines in mind:

- Compare the server’s credentials against a public key, instead of storing a single certificate in your app bundle. This will allow you to reissue a certificate for the same key and update the server, rather than needing to update the app.
- Compare the issuing certificate authority’s (CA’s) keys, rather than using the leaf key. This way, you can deploy certificates containing new keys signed by the same CA.
- Use a set of keys or CAs, so you can rotate server credentials more gracefully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/performing-manual-server-trust-authentication)*