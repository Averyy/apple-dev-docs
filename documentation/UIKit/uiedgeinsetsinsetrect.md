# UIEdgeInsetsInsetRect

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Adjusts a rectangle by the given edge insets.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```c
static CGRect UIEdgeInsetsInsetRect(CGRect rect, UIEdgeInsets insets);
```

#### Return Value

A rectangle that is adjusted by the `UIEdgeInsets` structure passed in insets.

#### Discussion

This inline function increments the origin of `rect` and decrements the size of `rect` by applying the appropriate member values of the `UIEdgeInsets` structure.

## Parameters

- `rect`: The rectangle to be adjusted.
- `insets`: The edge insets to be applied to the adjustment.

## See Also

### Related Documentation
- [init(top: CGFloat, left: CGFloat, bottom: CGFloat, right: CGFloat)](./uiedgeinsets/init%28top,left,bottom,right%29-1s1t9.md)
  Creates an edge insets structure with the specified edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiedgeinsetsinsetrect)*