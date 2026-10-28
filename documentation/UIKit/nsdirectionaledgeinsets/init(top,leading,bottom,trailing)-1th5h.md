# init(top:leading:bottom:trailing:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a directional edge insets structure that contains the specified values.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)
```

```c
static NSDirectionalEdgeInsets NSDirectionalEdgeInsetsMake(CGFloat top, CGFloat leading, CGFloat bottom, CGFloat trailing);
```

## Return Value

A directional inset structure.

## Discussion

An inset is a margin around a rectangle. Positive values represent margins closer to the center of the rectangle, while negative values represent margins further from the center.

## Parameters

- `top`: The inset on the top of an object.
- `leading`: The inset on the leading edge of an object. In a left-to-right system, the left edge is the leading edge. In a right-to-left system, the right edge is the leading edge.
- `bottom`: The inset on the bottom edge of an object.
- `trailing`: The inset on the trailing edge of an object. In a left-to-right system, the right edge is the trailing edge. In a right-to-left system, the left edge is the trailing edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdirectionaledgeinsets/init(top:leading:bottom:trailing:)-1th5h)*