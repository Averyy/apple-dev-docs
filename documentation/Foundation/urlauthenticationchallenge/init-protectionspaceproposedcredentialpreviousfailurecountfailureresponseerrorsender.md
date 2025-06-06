# init(protectionSpace:proposedCredential:previousFailureCount:failureResponse:error:sender:)

**Framework**: Foundation  
**Kind**: init

Initializes an authentication challenge from parameters you provide.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(protectionSpace space: URLProtectionSpace, proposedCredential credential: URLCredential?, previousFailureCount: Int, failureResponse response: URLResponse?, error: (any Error)?, sender: any URLAuthenticationChallengeSender)
```

#### Return Value

A new authentication challenge object, with the given properties.

#### Discussion

Most apps don’t create [`URLAuthenticationChallenge`](urlauthenticationchallenge.md) instances themselves. Instead, they handle received challenges in the [`urlSession(_:task:didReceive:completionHandler:)`](urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:).md) method of [`URLSessionTaskDelegate`](urlsessiontaskdelegate.md).

However, you might need to create authentication challenge objects when adding support for custom networking protocols, as part of your custom [`URLProtocol`](urlprotocol.md) subclasses.

## Parameters

- `space`: The protection space for the authentication challenge. This provides additional information about the authentication request, such as the host, port, authentication realm, and so on.
- `credential`: The proposed credential, or  .
- `previousFailureCount`: The total number of previous failures for this request, including failures for other protection spaces.
- `response`: An instance of   containing the server response that caused you to generate an authentication challenge, or   if no response object is applicable to the challenge.
- `error`: An   instance describing the authentication failure, or   if it is not applicable to the challenge.
- `sender`: The object that initiated the authentication challenge (typically, the object that called this method).

## See Also

- [init(authenticationChallenge: URLAuthenticationChallenge, sender: any URLAuthenticationChallengeSender)](urlauthenticationchallenge/init(authenticationchallenge:sender:).md)
  Creates an authentication challenge from an existing challenge instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/init(protectionspace:proposedcredential:previousfailurecount:failureresponse:error:sender:))*