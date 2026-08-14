# UserAnnotation

**Framework**: MapKit  
**Kind**: struct

Displays the person’s current location on the map.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct UserAnnotation<Content> where Content : View
```

#### Overview

Displays the person’s current location using the system styled user location indicator.

## Topics

### Creating a user annotation
- [init()](userannotation/init.md)
  Creates an annotation that displays the person’s current location.
- [init(anchor: UnitPoint)](userannotation/init(anchor:).md)
  Creates an annotation that displays the person’s current location using the system styled user location indicator with the specified anchor point.
- [init(anchor: UnitPoint, content: (UserLocation) -> Content)](userannotation/init(anchor:content:)-8u3r4.md)
  Creates an annotation that displays a person’s current location using the system styled user location indicator with the specified anchor point using a custom view.
- [init(anchor: UnitPoint, content: () -> Content)](userannotation/init(anchor:content:)-3e78j.md)
  Create an annotation that displays the person’s current location of the user using a custom view.
### Setting the visibility of the title and subtitle
- [func annotationTitles(Visibility) -> some MapContent](mapcontent/annotationtitles(_:).md)
  Sets the visibility of titles for markers and annotations.
- [func annotationSubtitles(Visibility) -> some MapContent](mapcontent/annotationsubtitles(_:).md)
  Sets the visibility of subtitles for markers and annotations.
### Information about a person’s location
- [struct UserLocation](userlocation.md)
  A structure that contains Information about the person’s current location.
### Setting the overlay level
- [func mapOverlayLevel(level: MKOverlayLevel) -> some MapContent](mapcontent/mapoverlaylevel(level:).md)
  Specifies the position of overlays relative to other map content.
### Setting the tag
- [func tag<V>(V) -> some MapContent](mapcontent/tag(_:).md)
  Sets the unique tag value of this piece of map content.
### Type aliases
- [associatedtype Body : MapContent](mapcontent/body-swift.associatedtype.md)
  The content and behavior of the view.

## Relationships

### Conforms To
- [MapContent](mapcontent.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct Annotation](annotation.md)
  A customizable annotation used to indicate a location on a map.
- [struct MapCircle](mapcircle.md)
  A circular overlay with a configurable radius that you center on a geographic coordinate.
- [struct MapPolygon](mappolygon.md)
  A closed polygon overlay.
- [struct MapPolyline](mappolyline.md)
  An open polygon overlay consisting of one or more connected line segments.
- [struct Marker](marker.md)
  A balloon-shaped annotation that marks a map location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/userannotation)*