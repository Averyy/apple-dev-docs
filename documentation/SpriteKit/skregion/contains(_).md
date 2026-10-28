# contains(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether a particular point is contained in the region.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func contains(_ point: CGPoint) -> Bool
```

```objc
- (BOOL) containsPoint:(CGPoint) point;
```

## Return Value

[`true`](../../Swift/true.md) if the point is contained in the region; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `point`: A point.

## See Also

### Interacting with a Region
- [var path: CGPath?](./path.md)
  Returns a Core Graphics path that defines the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skregion/contains(_:))*