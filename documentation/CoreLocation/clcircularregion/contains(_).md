# contains(_:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the geographic area contains the specified coordinate.

**Availability**:
- iOS 7.0+ - Deprecated in 27.2
- iPadOS 7.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.2

## Declaration

```swift
func contains(_ coordinate: CLLocationCoordinate2D) -> Bool
```

```objc
- (BOOL) containsCoordinate:(CLLocationCoordinate2D) coordinate;
```

#### Return Value

Returns [`true`](../../Swift/true.md) if the coordinate lies within the region’s boundaries, or [`false`](../../Swift/false.md) if it doesn’t.

## Parameters

- `coordinate`: The coordinate to test against the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clcircularregion/contains(_:))*