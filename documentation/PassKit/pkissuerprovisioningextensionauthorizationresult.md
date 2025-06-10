# PKIssuerProvisioningExtensionAuthorizationResult

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

A value that indicates the result of authorizing the addition of a payment card.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
enum PKIssuerProvisioningExtensionAuthorizationResult
```

## Topics

### Authorization results
- [PKIssuerProvisioningExtensionAuthorizationResult.authorized](pkissuerprovisioningextensionauthorizationresult/authorized.md)
  A result that indicates the user successfully authorized adding the payment pass.
- [PKIssuerProvisioningExtensionAuthorizationResult.canceled](pkissuerprovisioningextensionauthorizationresult/canceled.md)
  A result that indicates the user canceled authorization or wasn’t authorized to add the payment card.
### Initializers
- [init?(rawValue: Int)](pkissuerprovisioningextensionauthorizationresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var completionHandler: ((PKIssuerProvisioningExtensionAuthorizationResult) -> Void)?](pkissuerprovisioningextensionauthorizationproviding/completionhandler.md)
  A completion handler the system calls to find the result of authorizing the addition of the payment card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionauthorizationresult)*