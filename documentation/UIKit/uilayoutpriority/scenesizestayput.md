# sceneSizeStayPut

**Framework**: UIKit  
**Kind**: property

The priority level at which the window’s scene prefers to stay the same size.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.0+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var sceneSizeStayPut: UILayoutPriority { get }
```

#### Discussion

Specify constraint priorities that are either higher or lower than this value, rather than equal to it.

## See Also

- [static var required: UILayoutPriority](uilayoutpriority/required.md)
  A required constraint.
- [static var defaultHigh: UILayoutPriority](uilayoutpriority/defaulthigh.md)
  The priority level with which a button resists compressing its content.
- [static var dragThatCanResizeScene: UILayoutPriority](uilayoutpriority/dragthatcanresizescene.md)
  The priority level for a drag that may end up resizing the window’s scene.
- [static var dragThatCannotResizeScene: UILayoutPriority](uilayoutpriority/dragthatcannotresizescene.md)
  The priority level for a drag that won’t resize the window’s scene.
- [static var defaultLow: UILayoutPriority](uilayoutpriority/defaultlow.md)
  The priority level at which a button hugs its contents horizontally.
- [static var fittingSizeLevel: UILayoutPriority](uilayoutpriority/fittingsizelevel.md)
  The priority level with which the view wants to conform to the target size in that computation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutpriority/scenesizestayput)*