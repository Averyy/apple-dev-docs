# AnchoringComponent.ObjectAnchoringSource

**Framework**: RealityKit  
**Kind**: struct

Defines the source of object anchoring target based on how it is created.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ObjectAnchoringSource
```

## Topics

### Operators
- [static func == (AnchoringComponent.ObjectAnchoringSource, AnchoringComponent.ObjectAnchoringSource) -> Bool](anchoringcomponent/objectanchoringsource/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(URL)](anchoringcomponent/objectanchoringsource/init(_:).md)
  Creates the object anchoring source by reference object file URL.
- [init(group: String, name: String)](anchoringcomponent/objectanchoringsource/init(group:name:).md)
  Creates the object anchoring source by group and name in AR Resources.
- [init(name: String, in: Bundle)](anchoringcomponent/objectanchoringsource/init(name:in:).md)
  Creates the object anchoring source by reference object file asset with provided name and bundle.
### Instance Properties
- [var hashValue: Int](anchoringcomponent/objectanchoringsource/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](anchoringcomponent/objectanchoringsource/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](anchoringcomponent/objectanchoringsource/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [AnchoringComponent.ImageAnchoringSource](anchoringcomponent/imageanchoringsource.md)
  Defines the source of object anchoring target based on how it is created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/anchoringcomponent/objectanchoringsource)*