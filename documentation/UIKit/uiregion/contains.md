# contains(_:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean indicating whether the specified point is inside of the current region.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func contains(_ point: CGPoint) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the point is in the current region or [`false`](https://developer.apple.com/documentation/swift/false) if it is not.

#### Discussion

UIKit Dynamics normally calls this method when it needs to determine the interactions between two objects. If you call this method yourself, remember that the origin of the region object itself is at the center of the region’s shape and you might need to adjust the value of `point` accordingly.

## Parameters

- `point`: The point to test. The specified point must be in the region’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiregion/contains(_:))*