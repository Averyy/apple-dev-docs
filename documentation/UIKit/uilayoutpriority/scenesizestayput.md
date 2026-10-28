# sceneSizeStayPut

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The priority level at which the window’s scene prefers to stay the same size.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst 13.0+
- tvOS
- visionOS

## Declaration

```swift
static var sceneSizeStayPut: UILayoutPriority { get }
```

```c
static const UILayoutPriority UILayoutPrioritySceneSizeStayPut;
```

## Discussion

Specify constraint priorities that are either higher or lower than this value, rather than equal to it.

## See Also

### Constants
- [static var required: UILayoutPriority](./required.md)
  A required constraint.
- [static var defaultHigh: UILayoutPriority](./defaulthigh.md)
  The priority level with which a button resists compressing its content.
- [static var dragThatCanResizeScene: UILayoutPriority](./dragthatcanresizescene.md)
  The priority level for a drag that may end up resizing the window’s scene.
- [static var dragThatCannotResizeScene: UILayoutPriority](./dragthatcannotresizescene.md)
  The priority level for a drag that won’t resize the window’s scene.
- [static var defaultLow: UILayoutPriority](./defaultlow.md)
  The priority level at which a button hugs its contents horizontally.
- [static var fittingSizeLevel: UILayoutPriority](./fittingsizelevel.md)
  The priority level with which the view wants to conform to the target size in that computation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutpriority/scenesizestayput)*