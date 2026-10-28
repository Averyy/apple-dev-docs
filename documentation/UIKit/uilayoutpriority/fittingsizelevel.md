# fittingSizeLevel

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The priority level with which the view wants to conform to the target size in that computation.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var fittingSizeLevel: UILayoutPriority { get }
```

```c
static const UILayoutPriority UILayoutPriorityFittingSizeLevel;
```

## Discussion

When you send a [`systemLayoutSizeFitting(_:)`](../uiview/systemlayoutsizefitting%28_%29.md) message to a view, the size fitting most closely to the target size is computed. This priority is quite low. It’s generally not appropriate to make a constraint at exactly this priority. You want to be higher or lower.

## See Also

### Constants
- [static var required: UILayoutPriority](./required.md)
  A required constraint.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutpriority/fittingsizelevel)*