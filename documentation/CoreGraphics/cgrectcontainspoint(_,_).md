# CGRectContainsPoint(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns whether a rectangle contains a specified point.

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
func CGRectContainsPoint(_ rect: CGRect, _ point: CGPoint) -> Bool
```

```c
extern bool CGRectContainsPoint(CGRect rect, CGPoint point);
```

## Return Value

[`true`](../Swift/true.md) if the rectangle is not null or empty and the point is located within the rectangle; otherwise, [`false`](../Swift/false.md).

## Discussion

A point is considered inside the rectangle if its coordinates lie inside the rectangle or on the minimum X or minimum Y edge.

## Parameters

- `rect`: The rectangle to examine.
- `point`: The point to examine.

## See Also

### Checking for Membership
- [func CGRectContainsRect(CGRect, CGRect) -> Bool](./cgrectcontainsrect%28_,_%29.md)
  Returns whether the first rectangle contains the second rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectcontainspoint(_:_:))*