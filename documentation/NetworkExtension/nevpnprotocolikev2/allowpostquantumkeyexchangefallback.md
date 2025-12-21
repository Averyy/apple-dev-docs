# allowPostQuantumKeyExchangeFallback

**Framework**: Network Extension  
**Kind**: property

A Boolean value that indicates whether servers that don’t support post-quantum key exchanges can skip them.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var allowPostQuantumKeyExchangeFallback: Bool { get set }
```

#### Discussion

This property has no effect if you don’t configure any post-quantum key exchange methods in the [`NEVPNIKEv2SecurityAssociationParameters`](nevpnikev2securityassociationparameters.md). The property’s default value is `false`.

## See Also

- [var ppkConfiguration: NEVPNIKEv2PPKConfiguration?](nevpnprotocolikev2/ppkconfiguration.md)
  The configuration for a post-quantum pre-shared key (PPK).
- [class NEVPNIKEv2PPKConfiguration](nevpnikev2ppkconfiguration.md)
  A class that manages parameters of a post-quantum pre-shared key (PPK).


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnprotocolikev2/allowpostquantumkeyexchangefallback)*