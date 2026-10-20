# init(including:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Initialize the point of interest filter with a list of categories to include.

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
init(including categories: [MKPointOfInterestCategory])
```

```objc
- (instancetype) initIncludingCategories:(NSArray<NSString *> *) categories;
```

## Parameters

- `categories`: An array of categories to include.

## See Also

### Creating filters
- [class var excludingAll: MKPointOfInterestFilter](./excludingall.md)
  A filter that excludes all point of interest categories.
- [class var includingAll: MKPointOfInterestFilter](./includingall.md)
  A filter that includes all point of interest categories.
- [init(excluding: [MKPointOfInterestCategory])](./init%28excluding%29.md)
  Initialize the point of interest filter with a list of categories to exclude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/init(including:))*