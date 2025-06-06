# PointOfInterestCategories

**Framework**: MapKit  
**Kind**: struct

A structure you use to define points of interest to include or exclude on a map.

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
struct PointOfInterestCategories
```

## Topics

### Categories to include or exclude
- [static var all: PointOfInterestCategories](pointofinterestcategories/all.md)
  A list of all points of interest categories, both included and excluded.
- [static var excludingAll: PointOfInterestCategories](pointofinterestcategories/excludingall.md)
  A list of point of interest categories to exclude from display on the map.
### Modifying the categories to include or exclude
- [static func excluding([MKPointOfInterestCategory]) -> PointOfInterestCategories](pointofinterestcategories/excluding(_:)-16bp0.md)
  Show all points of interest except those belonging to certain categories using the array you provide.
- [static func excluding(MKPointOfInterestCategory...) -> PointOfInterestCategories](pointofinterestcategories/excluding(_:)-4jo9h.md)
  Show all points of interest except those belonging to certain categories using the list you provide.
- [static func including([MKPointOfInterestCategory]) -> PointOfInterestCategories](pointofinterestcategories/including(_:)-22f7x.md)
  Show only points of interest belonging to certain categories from the provided array.
- [static func including(MKPointOfInterestCategory...) -> PointOfInterestCategories](pointofinterestcategories/including(_:)-6flda.md)
  Show only points of interest belonging to certain categories from the provided list.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/pointofinterestcategories)*