# contentInsets

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The amount of space added around the content of the container to adjust its final size.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentInsets: NSDirectionalEdgeInsets { get }
```

#### Discussion

If the value of a content inset is less than `1.0`, the content inset is fractional. For example, a top content inset of `20.0` adds 20 points of space between the top of the layout and the top of its container. A top content inset of `0.2` adds space equal to 20% of the container’s height between the top of the layout and the top of its container.

![Two diagrams that compare two ways of specifying content insets. Both diagrams show a container box with a layout box inside of it. The first diagram shows a top content inset with the value 20.0. The space between the top of the container box and the top of the layout box displays the value 20 points. The second diagram shows a top content inset with the value 0.2. The space between the top of the container box and the top of the layout box displays the value 20% of container height.](https://docs-assets.developer.apple.com/published/9aaff7a4fcdb9cd07fbd499b39d6fd11/media-3570380%402x.png)

## See Also

- [var effectiveContentInsets: NSDirectionalEdgeInsets](nscollectionlayoutcontainer/effectivecontentinsets.md)
  The amount of space added around the content of the container to adjust its final size after item content insets are applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutcontainer/contentinsets)*