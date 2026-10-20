# heightAnchor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A layout anchor representing the guide’s height.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var heightAnchor: NSLayoutDimension { get }
```

```objc
@property (strong, readonly) NSLayoutDimension * heightAnchor;
```

#### Discussion

Use this anchor to create constraints with the guide’s height. You can only combine this anchor with other [`NSLayoutDimension`](../nslayoutdimension.md) anchors. For more information, see [`NSLayoutAnchor`](../nslayoutanchor.md).

## See Also

### Creating constraints using layout anchors
- [var bottomAnchor: NSLayoutYAxisAnchor](./bottomanchor.md)
  A layout anchor representing the guide’s bottom edge.
- [var topAnchor: NSLayoutYAxisAnchor](./topanchor.md)
  A layout anchor representing the guide’s top edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutsupport/heightanchor)*