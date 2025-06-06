# DynamicMapContent

**Framework**: MapKit  
**Kind**: protocol

A  type of view that generates views from an underlying collection of data.

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
protocol DynamicMapContent : MapContent
```

## Topics

### Accessing the data
- [var data: Self.Data](dynamicmapcontent/data-swift.property.md)
  The collection of underlying data.
### Associated types
- [associatedtype Data : Collection](dynamicmapcontent/data-swift.associatedtype.md)
  The type represents the data this protocol contains.

## Relationships

### Inherits From
- [MapContent](mapcontent.md)

## See Also

- [protocol MapContent](mapcontent.md)
  A protocol used to construct map content such as controls, markers, and annotations.
- [struct MapContentBuilder](mapcontentbuilder.md)
  A result builder that creates map content from closures you provide.
- [struct MapContentView](mapcontentview.md)
  A view that contains content that displays on a map at a specific position, and that responds to specific interactions you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/dynamicmapcontent)*