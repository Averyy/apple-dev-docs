# allowPostQuantumKeyExchangeFallback

**Framework**: Network Extension  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var allowPostQuantumKeyExchangeFallback: Bool { get set }
```

#### Discussion

Allow servers that do not support post-quantum key exchanges to skip them. This property has no effect if no post-quantum key exchange methods are configured for the IKE SA or Child SA (see NEVPNIKEv2SecurityAssociationParameters.postQuantumKeyExchangeMethods). Default is NO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/allowpostquantumkeyexchangefallback)*