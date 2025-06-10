# MusicCatalogChart

**Framework**: MusicKit  
**Kind**: struct

An object that contains popular items in the Apple Music catalog.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct MusicCatalogChart<MusicItemType> where MusicItemType : MusicCatalogChartRequestable
```

## Topics

### Instance Properties
- [let id: String](musiccatalogchart/id-swift.property.md)
  The unique identifier for the catalog chart.
- [let items: MusicItemCollection<MusicItemType>](musiccatalogchart/items.md)
  The items for the catalog chart.
- [let kind: MusicCatalogChartKind](musiccatalogchart/kind.md)
  The kind of catalog chart.
- [let title: String](musiccatalogchart/title.md)
  The title for the catalog chart.
### Type Aliases
- [MusicCatalogChart.ID](musiccatalogchart/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [CustomDebugStringConvertible Implementations](musiccatalogchart/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](musiccatalogchart/customstringconvertible-implementations.md)
- [Decodable Implementations](musiccatalogchart/decodable-implementations.md)
- [Encodable Implementations](musiccatalogchart/encodable-implementations.md)
- [Equatable Implementations](musiccatalogchart/equatable-implementations.md)
- [Hashable Implementations](musiccatalogchart/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogchart)*