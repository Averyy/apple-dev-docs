# includingAll

**Framework**: MapKit  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, nonatomic, readonly) MKPointOfInterestFilter * filterIncludingAllCategories;
```

## Discussion

You can use [`includingAll`](./includingall.md)  to include all points of interest in your map view without listing all the categories individually.

## See Also

### Creating filters
- [class var excludingAll: MKPointOfInterestFilter](./excludingall.md)
  A filter that excludes all point of interest categories.
- [init(excluding: [MKPointOfInterestCategory])](./init%28excluding%29.md)
  Initialize the point of interest filter with a list of categories to exclude.
- [init(including: [MKPointOfInterestCategory])](./init%28including%29.md)
  Initialize the point of interest filter with a list of categories to include.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/includingall)*