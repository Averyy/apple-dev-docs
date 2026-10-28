# CGRectIsInfinite(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns whether a rectangle is infinite.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGRectIsInfinite(_ rect: CGRect) -> Bool
```

```c
extern bool CGRectIsInfinite(CGRect rect);
```

## Return Value

Returns [`true`](../Swift/true.md) if the specified rectangle is infinite; otherwise, [`false`](../Swift/false.md).

## Discussion

An infinite rectangle is one that has no defined bounds. Infinite rectangles can be created as output from a tiling filter. For example, the Core Image framework perspective tile filter creates an image whose extent is described by an infinite rectangle.

## Parameters

- `rect`: The rectangle to examine.

## See Also

### Checking Rectangle Characteristics
- [func CGRectIsEmpty(CGRect) -> Bool](./cgrectisempty%28_%29.md)
  Returns whether a rectangle has zero width or height, or is a null rectangle.
- [func CGRectIsNull(CGRect) -> Bool](./cgrectisnull%28_%29.md)
  Returns whether the rectangle is equal to the null rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectisinfinite(_:))*