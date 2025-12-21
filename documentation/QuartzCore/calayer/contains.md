# contains(_:)

**Framework**: Core Animation  
**Kind**: method

Returns whether the receiver contains a specified point.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func contains(_ p: CGPoint) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the bounds of the layer contains the point.

## Parameters

- `p`: A point in the receiver’s coordinate system.

## See Also

- [func hitTest(CGPoint) -> CALayer?](calayer/hittest(_:).md)
  Returns the farthest descendant of the receiver in the layer hierarchy (including itself) that contains the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/contains(_:))*