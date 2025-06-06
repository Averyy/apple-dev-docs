# entities

**Framework**: RealityKit  
**Kind**: property  
**Required**: Yes

A collection of RealityKit entities that this view content renders within the scene.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var entities: Self.Entities { get nonmutating set }
```

## See Also

- [func add(Entity)](realityviewcontentprotocol/add(_:).md)
  Adds an entity to this content.
- [func remove(Entity)](realityviewcontentprotocol/remove(_:).md)
  Removes an entity from this content, if present.
- [associatedtype Entities : EntityCollection](realityviewcontentprotocol/entities-swift.associatedtype.md)
  The type of collection used for `entities`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewcontentprotocol/entities-swift.property)*