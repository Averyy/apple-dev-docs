# CGRectIsEmpty(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns whether a rectangle has zero width or height, or is a null rectangle.

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
func CGRectIsEmpty(_ rect: CGRect) -> Bool
```

```c
extern bool CGRectIsEmpty(CGRect rect);
```

## Return Value

[`true`](../Swift/true.md) if the specified rectangle is empty; otherwise, [`false`](../Swift/false.md).

## Discussion

An empty rectangle is either a null rectangle or a valid rectangle with zero height or width.

## Parameters

- `rect`: The rectangle to examine.

## See Also

### Checking Rectangle Characteristics
- [func CGRectIsNull(CGRect) -> Bool](./cgrectisnull%28_%29.md)
  Returns whether the rectangle is equal to the null rectangle.
- [func CGRectIsInfinite(CGRect) -> Bool](./cgrectisinfinite%28_%29.md)
  Returns whether a rectangle is infinite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectisempty(_:))*