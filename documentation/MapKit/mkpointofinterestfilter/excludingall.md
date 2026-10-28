# excludingAll

**Framework**: MapKit  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, nonatomic, readonly) MKPointOfInterestFilter * filterExcludingAllCategories;
```

## Discussion

You can use [`excludingAll`](./excludingall.md)  to remove all points of interest from your map view without listing all the categories individually.

## See Also

### Creating filters
- [class var includingAll: MKPointOfInterestFilter](./includingall.md)
  A filter that includes all point of interest categories.
- [init(excluding: [MKPointOfInterestCategory])](./init%28excluding%29.md)
  Initialize the point of interest filter with a list of categories to exclude.
- [init(including: [MKPointOfInterestCategory])](./init%28including%29.md)
  Initialize the point of interest filter with a list of categories to include.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/excludingall)*