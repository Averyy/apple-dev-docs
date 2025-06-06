# init(excluding:)

**Framework**: MapKit  
**Kind**: init

Initialize the point of interest filter with a list of categories to exclude.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(excluding categories: [MKPointOfInterestCategory])
```

## Parameters

- `categories`: An array of categories to exclude.

## See Also

- [class var excludingAll: MKPointOfInterestFilter](mkpointofinterestfilter/excludingall.md)
  A filter that excludes all point of interest categories.
- [class var includingAll: MKPointOfInterestFilter](mkpointofinterestfilter/includingall.md)
  A filter that includes all point of interest categories.
- [init(including: [MKPointOfInterestCategory])](mkpointofinterestfilter/init(including:).md)
  Initialize the point of interest filter with a list of categories to include.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/init(excluding:))*