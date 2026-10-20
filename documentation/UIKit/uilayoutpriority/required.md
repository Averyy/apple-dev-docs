# required

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A required constraint.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var required: UILayoutPriority { get }
```

```c
static const UILayoutPriority UILayoutPriorityRequired;
```

#### Discussion

Don’t specify a layout constraint that exceeds this number.

## See Also

### Constants
- [static var defaultHigh: UILayoutPriority](./defaulthigh.md)
  The priority level with which a button resists compressing its content.
- [static var dragThatCanResizeScene: UILayoutPriority](./dragthatcanresizescene.md)
  The priority level for a drag that may end up resizing the window’s scene.
- [static var sceneSizeStayPut: UILayoutPriority](./scenesizestayput.md)
  The priority level at which the window’s scene prefers to stay the same size.
- [static var dragThatCannotResizeScene: UILayoutPriority](./dragthatcannotresizescene.md)
  The priority level for a drag that won’t resize the window’s scene.
- [static var defaultLow: UILayoutPriority](./defaultlow.md)
  The priority level at which a button hugs its contents horizontally.
- [static var fittingSizeLevel: UILayoutPriority](./fittingsizelevel.md)
  The priority level with which the view wants to conform to the target size in that computation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutpriority/required)*