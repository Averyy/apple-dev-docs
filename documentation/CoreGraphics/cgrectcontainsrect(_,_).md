# CGRectContainsRect(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns whether the first rectangle contains the second rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGRectContainsRect(_ rect1: CGRect, _ rect2: CGRect) -> Bool
```

```c
extern bool CGRectContainsRect(CGRect rect1, CGRect rect2);
```

#### Return Value

[`true`](../Swift/true.md) if the rectangle specified by `rect2` is contained in the rectangle passed in `rect1`; otherwise, [`false`](../Swift/false.md). The first rectangle contains the second if the union of the two rectangles is equal to the first rectangle.

## Parameters

- `rect1`: The rectangle to examine for containment of the rectangle passed in `rect2`.
- `rect2`: The rectangle to examine for being contained in the rectangle passed in `rect1`.

## See Also

### Checking for Membership
- [func CGRectContainsPoint(CGRect, CGPoint) -> Bool](./cgrectcontainspoint%28_,_%29.md)
  Returns whether a rectangle contains a specified point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectcontainsrect(_:_:))*