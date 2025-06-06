# AnyMapContent

**Framework**: MapKit  
**Kind**: struct

A structure you use to change the type of content MapKit uses in a map view.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst ?+
- macOS 14.5+
- tvOS 17.5+
- visionOS 1.2+
- watchOS 10.5+

## Declaration

```swift
@MainActor
@preconcurrency struct AnyMapContent
```

#### Overview

`AnyMapContent` enables you to change the type of content in a map. When you change the type of content the map uses in `AnyMapContent`, the framework destroys the old hierarchy and creates a new hierarchy for the new type.

## Topics

### Initializers
- [init<Content>(Content)](anymapcontent/init(_:).md)
  Create an instance that type-erases `base`.

## Relationships

### Conforms To
- [MapContent](mapcontent.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct DefaultUserAnnotationContent](defaultuserannotationcontent.md)
  A structure that represents the view to show at the user’s location on the map.
- [struct EmptyMapContent](emptymapcontent.md)
  A map content element that doesn’t contain any content.
- [struct MapProxy](mapproxy.md)
  A proxy for accessing sizing information about a given map view.
- [struct MapReader](mapreader.md)
  A container view that defines its contents as a function of information about the first contained map.
- [struct TupleMapContent](tuplemapcontent.md)
  A view created from a Swift tuple of map content values.
- [struct MapSelectableContentView](mapselectablecontentview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/anymapcontent)*