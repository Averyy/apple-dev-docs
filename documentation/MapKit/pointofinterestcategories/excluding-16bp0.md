# excluding(_:)

**Framework**: MapKit  
**Kind**: method

Show all points of interest except those belonging to certain categories using the array you provide.

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
static func excluding(_ categories: [MKPointOfInterestCategory]) -> PointOfInterestCategories
```

#### Return Value

Returns a set of point of interest categories to exclude.

## Parameters

- `categories`: An array of points of interest categories to exclude.

## See Also

- [static func excluding(MKPointOfInterestCategory...) -> PointOfInterestCategories](pointofinterestcategories/excluding(_:)-4jo9h.md)
  Show all points of interest except those belonging to certain categories using the list you provide.
- [static func including([MKPointOfInterestCategory]) -> PointOfInterestCategories](pointofinterestcategories/including(_:)-22f7x.md)
  Show only points of interest belonging to certain categories from the provided array.
- [static func including(MKPointOfInterestCategory...) -> PointOfInterestCategories](pointofinterestcategories/including(_:)-6flda.md)
  Show only points of interest belonging to certain categories from the provided list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/pointofinterestcategories/excluding(_:)-16bp0)*