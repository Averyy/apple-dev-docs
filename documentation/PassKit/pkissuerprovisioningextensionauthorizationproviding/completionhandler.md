# completionHandler

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Required**: Yes

A completion handler the system calls to find the result of authorizing the addition of the payment card.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var completionHandler: ((PKIssuerProvisioningExtensionAuthorizationResult) -> Void)? { get set }
```

#### Discussion

The completion handler takes the following parameter:

## See Also

- [enum PKIssuerProvisioningExtensionAuthorizationResult](pkissuerprovisioningextensionauthorizationresult.md)
  A value that indicates the result of authorizing the addition of a payment card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionauthorizationproviding/completionhandler)*