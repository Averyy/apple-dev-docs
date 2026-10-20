# contains(_:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) containsPoint:(CGPoint) p;
```

#### Return Value

[`true`](../../Swift/true.md) if the bounds of the layer contains the point.

## Parameters

- `p`: A point in the receiver’s coordinate system.

## See Also

### Hit testing
- [func hitTest(CGPoint) -> CALayer?](./hittest%28_%29.md)
  Returns the farthest descendant of the receiver in the layer hierarchy (including itself) that contains the specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/contains(_:))*