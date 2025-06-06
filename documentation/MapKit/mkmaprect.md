# MKMapRect

**Framework**: MapKit  
**Kind**: struct

A rectangular area on a two-dimensional map projection.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct MKMapRect
```

#### Overview

If you project the curved surface of the globe onto a flat surface, what you get is a two-dimensional version of a map where longitude lines appear to be parallel. Such maps are often used to show the entire surface of the globe all at once. An `MKMapRect` data structure represents a rectangular area as seen on this two-dimensional map.

## Topics

### Creating a map rectangle
- [init()](mkmaprect/init.md)
  Creates the rectangle with an empty region.
- [init(origin: MKMapPoint, size: MKMapSize)](mkmaprect/init(origin:size:).md)
  Creates the map rectangle with the specified point and size.
- [init(x: Double, y: Double, width: Double, height: Double)](mkmaprect/init(x:y:width:height:).md)
  Creates a new map rectangle structure from the specified values.
- [init(MKMapRect)](mkcoordinateregion/init(_:).md)
  Returns the region that corresponds to the specified map rectangle.
### Getting standard map rectangles
- [static let null: MKMapRect](mkmaprect/null.md)
  The null map rectangle.
- [static let world: MKMapRect](mkmaprect/world.md)
  The map rectangle that represents the world in the two-dimensional map projection.
### Getting the rectangle coordinates
- [var origin: MKMapPoint](mkmaprect/origin.md)
  The origin point of the rectangle.
- [var size: MKMapSize](mkmaprect/size.md)
  The width and height of the rectangle, starting from the origin point.
### Getting the boundaries
- [var minX: Double](mkmaprect/minx.md)
  Returns the minimum x-axis value of the specified rectangle.
- [var minY: Double](mkmaprect/miny.md)
  Returns the minimum y-axis value of the specified rectangle.
- [var midX: Double](mkmaprect/midx.md)
  Returns the mid-point along the x-axis of the specified rectangle.
- [var midY: Double](mkmaprect/midy.md)
  Returns the mid-point along the y-axis of the specified rectangle.
- [var maxX: Double](mkmaprect/maxx.md)
  Returns the maximum x-axis value of the specified rectangle.
- [var maxY: Double](mkmaprect/maxy.md)
  Returns the maximum y-axis value of the specified rectangle.
- [var width: Double](mkmaprect/width.md)
  Returns the width of the map rectangle.
- [var height: Double](mkmaprect/height.md)
  Returns the height of the map rectangle.
### Comparing rectangles
- [var isNull: Bool](mkmaprect/isnull.md)
  A Boolean value that indicates whether the specified rectangle is null.
- [func MKMapRectEqualToRect(MKMapRect, MKMapRect) -> Bool](mkmaprectequaltorect(_:_:).md)
  Returns a Boolean value that indicates whether two map rectangles are equal.
- [var isEmpty: Bool](mkmaprect/isempty.md)
  A Boolean value that indicates whether the specified rectangle has no area.
- [var spans180thMeridian: Bool](mkmaprect/spans180thmeridian.md)
  A Boolean value that indicates whether the specified map rectangle crosses the 180th meridian.
- [var remainder: MKMapRect](mkmaprect/remainder.md)
  A rectangle that represents the normalized portion of the specified rectangle that lies outside the world map boundaries.
### Intersecting the rectangle
- [func contains(MKMapPoint) -> Bool](mkmaprect/contains(_:)-79tjt.md)
  Returns a Boolean value that indicates whether the specified map point lies within the rectangle.
- [func contains(MKMapRect) -> Bool](mkmaprect/contains(_:)-1z5oa.md)
  Returns a Boolean value that indicates whether one rectangle contains another.
- [func intersects(MKMapRect) -> Bool](mkmaprect/intersects(_:).md)
  Returns a Boolean value that indicates whether two rectangles intersect each other.
### Modifying the rectangle
- [func union(MKMapRect) -> MKMapRect](mkmaprect/union(_:).md)
  Returns a rectangle that represents the union of two rectangles.
- [func intersection(MKMapRect) -> MKMapRect](mkmaprect/intersection(_:).md)
  Returns the rectangle that represents the intersection of two rectangles.
- [func insetBy(dx: Double, dy: Double) -> MKMapRect](mkmaprect/insetby(dx:dy:).md)
  Returns the specified rectangle with an inset by the specified amounts.
- [func offsetBy(dx: Double, dy: Double) -> MKMapRect](mkmaprect/offsetby(dx:dy:).md)
  Returns a rectangle with an origin point that shifts by the specified amount.
- [func MKMapRectDivide(MKMapRect, UnsafeMutablePointer<MKMapRect>, UnsafeMutablePointer<MKMapRect>, Double, CGRectEdge)](mkmaprectdivide(_:_:_:_:_:).md)
  Divides the specified rectangle into two smaller rectangles.
### Getting a description of the rectangle
- [func MKStringFromMapRect(MKMapRect) -> String](mkstringfrommaprect(_:).md)
  Returns a formatted string for the specified map rectangle.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MKCoordinateRegion](mkcoordinateregion.md)
  A rectangular geographic region that centers around a specific latitude and longitude.
- [struct MKCoordinateSpan](mkcoordinatespan.md)
  The width and height of a map region.
- [struct MKMapPoint](mkmappoint.md)
  A point on a two-dimensional map projection.
- [struct MKMapSize](mkmapsize.md)
  Width and height information on a two-dimensional map projection.
- [class MKDistanceFormatter](mkdistanceformatter.md)
  A utility object that converts between a geographic distance and a string-based expression of that distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect)*