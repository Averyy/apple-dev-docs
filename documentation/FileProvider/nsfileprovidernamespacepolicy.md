# NSFileProviderNamespacePolicy

**Framework**: File Provider  
**Kind**: enum

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum NSFileProviderNamespacePolicy
```

## Topics

### Enumeration Cases
- [NSFileProviderNamespacePolicy.inherited](nsfileprovidernamespacepolicy/inherited.md)
  Inherit the namespace policy of the parent folder.
- [NSFileProviderNamespacePolicy.materializeEagerly](nsfileprovidernamespacepolicy/materializeeagerly.md)
  Download this folder eagerly, make sure it’s always fully enumerated Keep downloading remote updates eagerly. Prevent eviction on low disk pressure and other triggers.
- [NSFileProviderNamespacePolicy.materializeLazily](nsfileprovidernamespacepolicy/materializelazily.md)
  Enumerate this folder lazily (i.e upon access) if it is dataless. Keep populate new items below this folder eagerly if it’s already on disk.
### Initializers
- [init?(rawValue: Int)](nsfileprovidernamespacepolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidernamespacepolicy)*