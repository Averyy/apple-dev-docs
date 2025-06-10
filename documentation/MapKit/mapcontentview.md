# MapContentView

**Framework**: MapKit  
**Kind**: struct

A view that contains content that displays on a map at a specific position, and that responds to specific interactions you specify.

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
@preconcurrency struct MapContentView<SelectionValue, Content> where SelectionValue : Hashable, Content : MapContent
```

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [protocol DynamicMapContent](dynamicmapcontent.md)
  A  type of view that generates views from an underlying collection of data.
- [protocol MapContent](mapcontent.md)
  A protocol used to construct map content such as controls, markers, and annotations.
- [struct MapContentBuilder](mapcontentbuilder.md)
  A result builder that creates map content from closures you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontentview)*