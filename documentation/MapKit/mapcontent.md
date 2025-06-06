# MapContent

**Framework**: MapKit  
**Kind**: protocol

A protocol used to construct map content such as controls, markers, and annotations.

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
@preconcurrency protocol MapContent
```

## Topics

### Accessing the view body
- [var body: Self.Body](mapcontent/body-swift.property.md)
  The content and behavior of the view.
### Supplying annotation titles
- [func annotationTitles(Visibility) -> some MapContent](mapcontent/annotationtitles(_:).md)
  Sets the visibility of titles for markers and annotations.
- [func annotationSubtitles(Visibility) -> some MapContent](mapcontent/annotationsubtitles(_:).md)
  Sets the visibility of subtitles for markers and annotations.
### Setting the content style
- [func foregroundStyle(some ShapeStyle) -> some MapContent](mapcontent/foregroundstyle(_:).md)
  Specifies the shape style used to fill content in drawing map overlays.
- [func tint<S>(S) -> some MapContent](mapcontent/tint(_:).md)
  The tint shape style to apply to map content.
### Setting stroke properties
- [func stroke(some ShapeStyle, lineWidth: CGFloat) -> some MapContent](mapcontent/stroke(_:linewidth:).md)
  Applies the given shape style to drawn map overlays using the line width you specify.
- [func stroke(some ShapeStyle, style: StrokeStyle) -> some MapContent](mapcontent/stroke(_:style:).md)
  Applies the given shape style to drawn map overlays using the stroke style you specify.
- [func stroke(lineWidth: CGFloat) -> some MapContent](mapcontent/stroke(linewidth:).md)
  Applies the given stoke drawn map overlays using the line width you specify.
- [func strokeStyle(style: StrokeStyle) -> some MapContent](mapcontent/strokestyle(style:).md)
  Applies the given stroke style to drawn map overlays.
### Setting the overlay level
- [func mapOverlayLevel(level: MKOverlayLevel) -> some MapContent](mapcontent/mapoverlaylevel(level:).md)
  Specifies the position of overlays relative to other map content.
### Associated types
- [associatedtype Body : MapContent](mapcontent/body-swift.associatedtype.md)
  The content and behavior of the view.
### Displaying place information
- [func mapItemDetailSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some MapContent](mapcontent/mapitemdetailselectionaccessory(_:).md)
  Specifies the selection accessory to display for the selected map item content.
### Instance Methods
- [func tag<V>(V) -> some MapContent](mapcontent/tag(_:).md)
  Sets the unique tag value of this piece of map content.

## Relationships

### Inherited By
- [DynamicMapContent](dynamicmapcontent.md)
### Conforming Types
- [Annotation](annotation.md)
- [AnyMapContent](anymapcontent.md)
- [EmptyMapContent](emptymapcontent.md)
- [MapCircle](mapcircle.md)
- [MapPolygon](mappolygon.md)
- [MapPolyline](mappolyline.md)
- [Marker](marker.md)
- [TupleMapContent](tuplemapcontent.md)
- [UserAnnotation](userannotation.md)

## See Also

- [protocol DynamicMapContent](dynamicmapcontent.md)
  A  type of view that generates views from an underlying collection of data.
- [struct MapContentBuilder](mapcontentbuilder.md)
  A result builder that creates map content from closures you provide.
- [struct MapContentView](mapcontentview.md)
  A view that contains content that displays on a map at a specific position, and that responds to specific interactions you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontent)*