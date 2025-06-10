# includingAll

**Framework**: MapKit  
**Kind**: property

A filter that includes all point of interest categories.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class var includingAll: MKPointOfInterestFilter { get }
```

#### Discussion

You can use [`includingAll`](mkpointofinterestfilter/includingall.md)  to include all points of interest in your map view without listing all the categories individually.

## See Also

- [class var excludingAll: MKPointOfInterestFilter](mkpointofinterestfilter/excludingall.md)
  A filter that excludes all point of interest categories.
- [init(excluding: [MKPointOfInterestCategory])](mkpointofinterestfilter/init(excluding:).md)
  Initialize the point of interest filter with a list of categories to exclude.
- [init(including: [MKPointOfInterestCategory])](mkpointofinterestfilter/init(including:).md)
  Initialize the point of interest filter with a list of categories to include.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/includingall)*