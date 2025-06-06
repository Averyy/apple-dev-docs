# includes(_:)

**Framework**: MapKit  
**Kind**: method

Returns a Boolean value indicating whether the filter includes the point of interest category.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func includes(_ category: MKPointOfInterestCategory) -> Bool
```

#### Return Value

`true` if the filter includes the point of interest category; otherwise, `false`.

## Parameters

- `category`: A point of interest category that the method checks for inclusion in the filter.

## See Also

- [func excludes(MKPointOfInterestCategory) -> Bool](mkpointofinterestfilter/excludes(_:).md)
  Returns a Boolean value indicating whether the filter excludes the point of interest category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/includes(_:))*