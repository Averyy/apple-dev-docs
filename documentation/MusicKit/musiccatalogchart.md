# MusicCatalogChart

**Framework**: MusicKit  
**Kind**: struct  
**Role**: Structure

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
- [let id: String](./musiccatalogchart/id.md)
  The unique identifier for the catalog chart.
- [let items: MusicItemCollection<MusicItemType>](./musiccatalogchart/items.md)
  The items for the catalog chart.
- [let kind: MusicCatalogChartKind](./musiccatalogchart/kind.md)
  The kind of catalog chart.
- [let title: String](./musiccatalogchart/title.md)
  The title for the catalog chart.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiccatalogchart)*