# urlSession(_:didReceive:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Requests credentials from the delegate in response to a session-level authentication request from the remote server.

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
optional func urlSession(_ session: URLSession, didReceive challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```

## Mentions

- [Performing manual server trust authentication](performing-manual-server-trust-authentication.md)

#### Discussion

This method is called in two situations:

- When a remote server asks for client certificates or Windows NT LAN Manager (NTLM) authentication, to allow your app to provide appropriate credentials
- When a session first establishes a connection to a remote server that uses SSL or TLS, to allow your app to verify the server’s certificate chain

If you do not implement this method, the session calls its delegate’s [`urlSession(_:task:didReceive:completionHandler:)`](urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:).md) method instead.

> **Note**:  This method handles  the [`NSURLAuthenticationMethodNTLM`](nsurlauthenticationmethodntlm.md), [`NSURLAuthenticationMethodNegotiate`](nsurlauthenticationmethodnegotiate.md), [`NSURLAuthenticationMethodClientCertificate`](nsurlauthenticationmethodclientcertificate.md), and [`NSURLAuthenticationMethodServerTrust`](nsurlauthenticationmethodservertrust.md) authentication types. For all other authentication schemes, the session calls  the [`urlSession(_:task:didReceive:completionHandler:)`](urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:).md) method.

## Parameters

- `session`: The session containing the task that requested authentication.
- `challenge`: An object that contains the request for authentication.
- `completionHandler`: A handler that your delegate method must call. This completion handler takes the following parameters::

## See Also

- [URLSession.AuthChallengeDisposition](urlsession/authchallengedisposition.md)
  Constants passed by session or task delegates to the provided continuation block in response to an authentication challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondelegate/urlsession(_:didreceive:completionhandler:))*