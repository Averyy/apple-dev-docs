# MapSelectableContentView

**Framework**: MapKit  
**Kind**: struct

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct MapSelectableContentView<SelectionValue, Content> where SelectionValue : MapSelectable, Content : MapContent
```

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
- [struct MapReader](mapreader.md)
  A container view that defines its contents as a function of information about the first contained map.
- [struct TupleMapContent](tuplemapcontent.md)
  A view created from a Swift tuple of map content values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapselectablecontentview)*