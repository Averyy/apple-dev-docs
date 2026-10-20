# EmptyMapContent

**Framework**: MapKit  
**Kind**: struct  
**Role**: Structure

A map content element that doesn’t contain any content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct EmptyMapContent
```

## Topics

### Creating an empty map content structure
- [init()](./emptymapcontent/init%28%29.md)
  Creates an empty map content element.
### Setting the tag
- [func tag<V>(V) -> some MapContent](./mapcontent/tag%28_%29.md)
  Sets the unique tag value of this piece of map content.
### Type aliases
- [associatedtype Body : MapContent](./mapcontent/body-swift.associatedtype.md)
  The content and behavior of the view.

## Relationships

### Conforms To
- [MapContent](./mapcontent.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Structures
- [struct DefaultUserAnnotationContent](./defaultuserannotationcontent.md)
  A structure that represents the view to show at the user’s location on the map.
- [struct MapProxy](./mapproxy.md)
  A proxy for accessing sizing information about a given map view.
- [struct MapReader](./mapreader.md)
  A container view that defines its contents as a function of information about the first contained map.
- [struct TupleMapContent](./tuplemapcontent.md)
  A view created from a Swift tuple of map content values.
- [struct MapSelectableContentView](./mapselectablecontentview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/emptymapcontent)*