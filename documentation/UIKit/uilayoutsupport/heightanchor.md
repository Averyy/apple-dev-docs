# heightAnchor

**Framework**: UIKit  
**Kind**: property  
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
@MainActor
var heightAnchor: NSLayoutDimension { get }
```

#### Discussion

Use this anchor to create constraints with the guide’s height. You can only combine this anchor with other [`NSLayoutDimension`](nslayoutdimension.md) anchors. For more information, see [`NSLayoutAnchor`](nslayoutanchor.md).

## See Also

- [var bottomAnchor: NSLayoutYAxisAnchor](uilayoutsupport/bottomanchor.md)
  A layout anchor representing the guide’s bottom edge.
- [var topAnchor: NSLayoutYAxisAnchor](uilayoutsupport/topanchor.md)
  A layout anchor representing the guide’s top edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutsupport/heightanchor)*