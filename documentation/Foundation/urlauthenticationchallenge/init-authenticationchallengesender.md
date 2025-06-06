# init(authenticationChallenge:sender:)

**Framework**: Foundation  
**Kind**: init

Creates an authentication challenge from an existing challenge instance.

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
init(authenticationChallenge challenge: URLAuthenticationChallenge, sender: any URLAuthenticationChallengeSender)
```

#### Return Value

A new authentication challenge object, based on an existing challenge.

#### Discussion

Most apps don’t create [`URLAuthenticationChallenge`](urlauthenticationchallenge.md) instances themselves. Instead, they handle received challenges in the [`urlSession(_:task:didReceive:completionHandler:)`](urlsessiontaskdelegate/urlsession(_:task:didreceive:completionhandler:).md) method of [`URLSessionTaskDelegate`](urlsessiontaskdelegate.md).

However, you might need to create authentication challenge objects when adding support for custom networking protocols, as part of a custom [`URLProtocol`](urlprotocol.md) subclass. When you subclass an existing [`URLProtocol`](urlprotocol.md) subclass, this initializer lets you modify challenges issued by the existing class so that your subclass receives any responses to those challenges.

## Parameters

- `challenge`: The challenge that you want to copy. Usually, this is a challenge received by an existing   subclass that you are subclassing.
- `sender`: The sender that you want to use for the new object. Typically, the sender is the instance of your custom   subclass that called this method.

## See Also

- [init(protectionSpace: URLProtectionSpace, proposedCredential: URLCredential?, previousFailureCount: Int, failureResponse: URLResponse?, error: (any Error)?, sender: any URLAuthenticationChallengeSender)](urlauthenticationchallenge/init(protectionspace:proposedcredential:previousfailurecount:failureresponse:error:sender:).md)
  Initializes an authentication challenge from parameters you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlauthenticationchallenge/init(authenticationchallenge:sender:))*