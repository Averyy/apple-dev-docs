# PartialMusicAsyncProperty

**Framework**: MusicKit  
**Kind**: class

A partially type-erased identifier for a music item property that you can fetch asynchronously from a concrete root type to any resulting value type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class PartialMusicAsyncProperty<Root>
```

## Relationships

### Inherits From
- [PartialMusicProperty](partialmusicproperty.md)
### Inherited By
- [MusicExtendedAttributeProperty](musicextendedattributeproperty.md)
- [MusicRelationshipProperty](musicrelationshipproperty.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MusicItem](musicitem.md)
  A protocol with basic requirements for music items.
- [struct MusicItemID](musicitemid.md)
  An object that represents a unique identifier for a music item.
- [struct MusicItemCollection](musicitemcollection.md)
  A collection of music items.
- [protocol MusicPropertyContainer](musicpropertycontainer.md)
  A protocol for music items that allow loading additional properties that you can fetch asynchronously.
- [class MusicRelationshipProperty](musicrelationshipproperty.md)
  An identifier for a music item relationship property from a specific root type to a specific value type for the element of the resulting collection.
- [class MusicExtendedAttributeProperty](musicextendedattributeproperty.md)
  An identifier for a music item extended attribute property from a specific root type to a specific resulting value type.
- [class MusicAttributeProperty](musicattributeproperty.md)
  An identifier for a music item attribute property from a specific root type to a specific resulting value type.
- [class PartialMusicProperty](partialmusicproperty.md)
  A partially type-erased identifier for a music item property from a concrete root type to any resulting value type.
- [class AnyMusicProperty](anymusicproperty.md)
  A type-erased identifier for a music item property, from any root type to any resulting value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/partialmusicasyncproperty)*