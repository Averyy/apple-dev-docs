# TupleMapContent

**Framework**: MapKit  
**Kind**: struct

A view created from a Swift tuple of map content values.

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
@frozen @preconcurrency struct TupleMapContent<T>
```

## Topics

### Accessing the tuple value
- [var value: T](tuplemapcontent/value.md)
  The contents of the tuple.

## Relationships

### Conforms To
- [MapContent](mapcontent.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DefaultUserAnnotationContent](defaultuserannotationcontent.md)
  A structure that represents the view to show at the user’s location on the map.
- [struct EmptyMapContent](emptymapcontent.md)
  A map content element that doesn’t contain any content.
- [struct MapProxy](mapproxy.md)
  A proxy for accessing sizing information about a given map view.
- [struct MapReader](mapreader.md)
  A container view that defines its contents as a function of information about the first contained map.
- [struct MapSelectableContentView](mapselectablecontentview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/tuplemapcontent)*