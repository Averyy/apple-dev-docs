# excludingAll

**Framework**: MapKit  
**Kind**: property

A filter that excludes all point of interest categories.

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
class var excludingAll: MKPointOfInterestFilter { get }
```

#### Discussion

You can use [`excludingAll`](mkpointofinterestfilter/excludingall.md)  to remove all points of interest from your map view without listing all the categories individually.

## See Also

- [class var includingAll: MKPointOfInterestFilter](mkpointofinterestfilter/includingall.md)
  A filter that includes all point of interest categories.
- [init(excluding: [MKPointOfInterestCategory])](mkpointofinterestfilter/init(excluding:).md)
  Initialize the point of interest filter with a list of categories to exclude.
- [init(including: [MKPointOfInterestCategory])](mkpointofinterestfilter/init(including:).md)
  Initialize the point of interest filter with a list of categories to include.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/excludingall)*