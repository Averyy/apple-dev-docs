# postQuantumKeyExchangeMethods

**Framework**: Network Extension  
**Kind**: property

The post-quantum key exchange method(s) used by the Security Association, if any.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var postQuantumKeyExchangeMethods: [NEVPNIKEv2PostQuantumKeyExchangeMethod] { get set }
```

#### Discussion

Up to 7 methods may be specified, mapping to ADDKE1 - ADDKE7 from RFC 9370.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnikev2securityassociationparameters/postquantumkeyexchangemethods-3173s)*