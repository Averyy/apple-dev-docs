# excludes(_:)

**Framework**: MapKit  
**Kind**: method

Returns a Boolean value indicating whether the filter excludes the point of interest category.

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
func excludes(_ category: MKPointOfInterestCategory) -> Bool
```

#### Return Value

`true` if the filter excludes the point of interest category; otherwise, `false`.

## Parameters

- `category`: A point of interest category that the method checks for exclusion in the filter.

## See Also

- [func includes(MKPointOfInterestCategory) -> Bool](mkpointofinterestfilter/includes(_:).md)
  Returns a Boolean value indicating whether the filter includes the point of interest category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/excludes(_:))*