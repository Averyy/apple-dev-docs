# ScrollEdgeEffectStyle

**Framework**: SwiftUI  
**Kind**: struct

A structure that specifies blur transitions between scrolling content and an area with controls, such as toolbars.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct ScrollEdgeEffectStyle
```

#### Overview

By default, the system sets an automatic scroll edge effect style to provide a visual transition between scrolling content and stationary controls at both edges of the scroll view in the scrolling direction. The system determines which style to apply based on the platform and context. The [`hard`](scrolledgeeffectstyle/hard.md) style provides a more opaque, clearly defined linear boundary, and the [`soft`](scrolledgeeffectstyle/soft.md) style provides a subtle blurred transition:

**Hard**:

![A partial image of a list scrolling behind a bottom toolbar on iPhone. The area where the toolbar overlaps the list content is nearly opaque, with a defined, straight horizontal line at the top.](/images/com.apple.SwiftUI/ScrollEdgeEffectStyle-2@2x.png)

**Soft**:

![A partial image of a list scrolling behind a bottom toolbar on iPhone. The area where the toolbar overlaps the list is translucent and blurry and gets progressively more opaque from the top to the bottom.](/images/com.apple.SwiftUI/ScrollEdgeEffectStyle-1@2x.png)

**None**:

![A partial image of a list scrolling behind a bottom toolbar on iPhone. The area where the toolbar overlaps the list is transparent.](/images/com.apple.SwiftUI/ScrollEdgeEffectStyle-3@2x.png)

Specify a `ScrollEdgeEffectStyle` for a scroll view using [`scrollEdgeEffectStyle(_:for:)`](view/scrolledgeeffectstyle(_:for:).md) when the automatic style the system applies isn’t appropriate for your content and controls. Apply [`scrollEdgeEffectHidden(_:for:)`](view/scrolledgeeffecthidden(_:for:).md) to a scroll view to remove the scroll edge effect entirely for an edge you specify.

## Topics

### Creating a scroll edge effect style
- [static var automatic: ScrollEdgeEffectStyle](scrolledgeeffectstyle/automatic.md)
  A scroll edge effect the system applies automatically when pinned content overlaps scrolling content.
- [static var hard: ScrollEdgeEffectStyle](scrolledgeeffectstyle/hard.md)
  A scroll edge effect that provides a linear, nearly opaque boundary between pinned controls and scrolling content.
- [static var soft: ScrollEdgeEffectStyle](scrolledgeeffectstyle/soft.md)
  A scroll edge effect that provides a subtle, blurred boundary between pinned controls and scrolling content.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func scrollEdgeEffectStyle(ScrollEdgeEffectStyle?, for: Edge.Set) -> some View](view/scrolledgeeffectstyle(_:for:).md)
  Configures the scroll edge effect style for scroll views within this hierarchy.
- [func scrollEdgeEffectHidden(Bool, for: Edge.Set) -> some View](view/scrolledgeeffecthidden(_:for:).md)
  Hides any scroll edge effects for scroll views within this hierarchy.
- [func safeAreaBar(edge:alignment:spacing:content:)](view/safeareabar(edge:alignment:spacing:content:).md)
  Shows the specified content as a custom bar beside the modified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle)*