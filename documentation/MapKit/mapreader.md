# MapReader

**Framework**: MapKit  
**Kind**: struct

A container view that defines its contents as a function of information about the first contained map.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct MapReader<Content> where Content : View
```

#### Overview

The map reader’s content builder receives a [`MapProxy`](mapproxy.md) instance. You can use this instance to get the information you’ll need to convert between a [`MapCamera`](mapcamera.md) and a [`MKMapRect`](mkmaprect.md) or [`MKCoordinateRegion`](mkcoordinateregion.md).

## Topics

### Creating a map reader
- [init(content: (MapProxy) -> Content)](mapreader/init(content:).md)
  Creates an instance that allows view content to reference information about a contained map.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct DefaultUserAnnotationContent](defaultuserannotationcontent.md)
  A structure that represents the view to show at the user’s location on the map.
- [struct AnyMapContent](anymapcontent.md)
  A structure you use to change the type of content MapKit uses in a map view.
- [struct EmptyMapContent](emptymapcontent.md)
  A map content element that doesn’t contain any content.
- [struct MapProxy](mapproxy.md)
  A proxy for accessing sizing information about a given map view.
- [struct TupleMapContent](tuplemapcontent.md)
  A view created from a Swift tuple of map content values.
- [struct MapSelectableContentView](mapselectablecontentview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapreader)*