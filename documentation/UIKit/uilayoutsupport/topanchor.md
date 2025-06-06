# topAnchor

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A layout anchor representing the guide’s top edge.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var topAnchor: NSLayoutYAxisAnchor { get }
```

#### Discussion

Use this anchor to create constraints with the guide’s top edge. You can only combine this anchor with other [`NSLayoutYAxisAnchor`](nslayoutyaxisanchor.md) anchors. For more information, see [`NSLayoutAnchor`](nslayoutanchor.md).

## See Also

- [var bottomAnchor: NSLayoutYAxisAnchor](uilayoutsupport/bottomanchor.md)
  A layout anchor representing the guide’s bottom edge.
- [var heightAnchor: NSLayoutDimension](uilayoutsupport/heightanchor.md)
  A layout anchor representing the guide’s height.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutsupport/topanchor)*