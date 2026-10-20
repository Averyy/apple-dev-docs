# hitTest(_:)

**Framework**: Core Animation  
**Kind**: method

Returns the farthest descendant of the receiver in the layer hierarchy (including itself) that contains the specified point.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func hitTest(_ p: CGPoint) -> CALayer?
```

#### Return Value

The layer that contains `thePoint` or `nil` if the point lies outside the receiver’s bounds rectangle.

## Parameters

- `p`: A point in the coordinate system of the receiver’s superlayer.

## See Also

- [func contains(CGPoint) -> Bool](calayer/contains(_:).md)
  Returns whether the receiver contains a specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/hittest(_:))*