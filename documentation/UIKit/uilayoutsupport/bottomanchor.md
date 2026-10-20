# bottomAnchor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A layout anchor representing the guide’s bottom edge.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var bottomAnchor: NSLayoutYAxisAnchor { get }
```

```objc
@property (strong, readonly) NSLayoutYAxisAnchor * bottomAnchor;
```

#### Discussion

Use this anchor to create constraints with the guide’s bottom edge. You can only combine this anchor with other [`NSLayoutYAxisAnchor`](../nslayoutyaxisanchor.md) anchors. For more information, see [`NSLayoutAnchor`](../nslayoutanchor.md).

## See Also

### Creating constraints using layout anchors
- [var heightAnchor: NSLayoutDimension](./heightanchor.md)
  A layout anchor representing the guide’s height.
- [var topAnchor: NSLayoutYAxisAnchor](./topanchor.md)
  A layout anchor representing the guide’s top edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutsupport/bottomanchor)*