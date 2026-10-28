# CGRectIsNull(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns whether the rectangle is equal to the null rectangle.

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
func CGRectIsNull(_ rect: CGRect) -> Bool
```

```c
extern bool CGRectIsNull(CGRect rect);
```

## Return Value

[`true`](../Swift/true.md) if the specified rectangle is null; otherwise, [`false`](../Swift/false.md).

## Discussion

A null rectangle is the equivalent of an empty set. For example, the result of intersecting two disjoint rectangles is a null rectangle. A null rectangle cannot be drawn and interacts with other rectangles in special ways.

## Parameters

- `rect`: The rectangle to examine.

## See Also

### Checking Rectangle Characteristics
- [func CGRectIsEmpty(CGRect) -> Bool](./cgrectisempty%28_%29.md)
  Returns whether a rectangle has zero width or height, or is a null rectangle.
- [func CGRectIsInfinite(CGRect) -> Bool](./cgrectisinfinite%28_%29.md)
  Returns whether a rectangle is infinite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectisnull(_:))*