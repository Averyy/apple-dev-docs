# PKIssuerProvisioningExtensionAuthorizationResult

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum PKIssuerProvisioningExtensionAuthorizationResult : NSInteger;
```

## Topics

### Authorization results
- [PKIssuerProvisioningExtensionAuthorizationResult.authorized](./pkissuerprovisioningextensionauthorizationresult/authorized.md)
  A result that indicates the user successfully authorized adding the payment pass.
- [PKIssuerProvisioningExtensionAuthorizationResult.canceled](./pkissuerprovisioningextensionauthorizationresult/canceled.md)
  A result that indicates the user canceled authorization or wasn’t authorized to add the payment card.
### Initializers
- [init?(rawValue: Int)](./pkissuerprovisioningextensionauthorizationresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Providing the result of authorization
- [var completionHandler: ((PKIssuerProvisioningExtensionAuthorizationResult) -> Void)?](./pkissuerprovisioningextensionauthorizationproviding/completionhandler.md)
  A completion handler the system calls to find the result of authorizing the addition of the payment card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionauthorizationresult)*