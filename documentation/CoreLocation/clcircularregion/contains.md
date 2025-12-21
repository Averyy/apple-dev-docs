# contains(_:)

**Framework**: Core Location  
**Kind**: method

Returns a Boolean value indicating whether the geographic area contains the specified coordinate.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- watchOS 2.0+

## Declaration

```swift
func contains(_ coordinate: CLLocationCoordinate2D) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the coordinate lies within the region’s boundaries, or [`false`](https://developer.apple.com/documentation/Swift/false) if it doesn’t.

## Parameters

- `coordinate`: The coordinate to test against the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clcircularregion/contains(_:))*