# init(top:left:bottom:right:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an edge insets structure with the specified edges.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```swift
init(top: CGFloat, left: CGFloat, bottom: CGFloat, right: CGFloat)
```

```c
static UIEdgeInsets UIEdgeInsetsMake(CGFloat top, CGFloat left, CGFloat bottom, CGFloat right);
```

## Return Value

An initialized inset structure.

## Discussion

An inset is a margin around a rectangle. Positive values represent margins closer to the center of the rectangle, while negative values represent margins further from the center.

## Parameters

- `top`: The inset at the top of an object.
- `left`: The inset on the left of an object
- `bottom`: The inset on the bottom of an object.
- `right`: The inset on the right of an object.

## See Also

### Related Documentation
- [UIEdgeInsetsEqualToEdgeInsets](../uiedgeinsetsequaltoedgeinsets.md)
  Returns a Boolean value indicating whether the two edge insets are the same.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiedgeinsets/init(top:left:bottom:right:)-1s1t9)*