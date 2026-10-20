# NSFileProviderNamespacePolicy

**Framework**: File Provider  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum NSFileProviderNamespacePolicy
```

```c
enum NSFileProviderNamespacePolicy : NSInteger;
```

## Topics

### Enumeration Cases
- [NSFileProviderNamespacePolicy.inherited](./nsfileprovidernamespacepolicy/inherited.md)
  Inherit the namespace policy of the parent folder.
- [NSFileProviderNamespacePolicy.materializeEagerly](./nsfileprovidernamespacepolicy/materializeeagerly.md)
  Download this folder eagerly, make sure it’s always fully enumerated Keep downloading remote updates eagerly. Prevent eviction on low disk pressure and other triggers.
- [NSFileProviderNamespacePolicy.materializeLazily](./nsfileprovidernamespacepolicy/materializelazily.md)
  Enumerate this folder lazily (i.e upon access) if it is dataless. Keep populate new items below this folder eagerly if it’s already on disk.
### Initializers
- [init?(rawValue: Int)](./nsfileprovidernamespacepolicy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidernamespacepolicy)*