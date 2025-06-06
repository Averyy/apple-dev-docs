# init(top:leading:bottom:trailing:)

**Framework**: UIKit  
**Kind**: init

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

#### Return Value

An initialized inset structure.

## Parameters

- `top`: The inset on the top of an object.
- `leading`: The inset on the leading edge of an object. In a left-to-right system, the left edge is the leading edge. In a right-to-left system, the right edge is the leading edge.
- `bottom`: The inset on the bottom of an object.
- `trailing`: The inset on the trailing edge of an object. In a left-to-right system, the right edge is the trailing edge. In a right-to-left system, the left edge is the trailing edge.

## See Also

- [init()](nsdirectionaledgeinsets/init.md)
  Creates a directional edge insets structure that contains default values.
- [init(EdgeInsets)](nsdirectionaledgeinsets/init(_:).md)
  Creates a directional edge insets structure from a SwiftUI edge insets structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdirectionaledgeinsets/init(top:leading:bottom:trailing:)-6wnda)*