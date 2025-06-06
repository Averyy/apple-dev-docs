# isHoverEffectEnabled

**Framework**: SwiftUI  
**Kind**: property

A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var isHoverEffectEnabled: Bool { get set }
```

#### Discussion

The default value is `true`.

## See Also

- [func onHover(perform: (Bool) -> Void) -> some View](view/onhover(perform:).md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [func onContinuousHover(coordinateSpace:perform:)](view/oncontinuoushover(coordinatespace:perform:).md)
  Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [func hoverEffect(_:isEnabled:)](view/hovereffect(_:isenabled:).md)
  Applies a hover effect to this view.
- [func hoverEffectDisabled(Bool) -> some View](view/hovereffectdisabled(_:).md)
  Adds a condition that controls whether this view can display hover effects.
- [func defaultHoverEffect(_:)](view/defaulthovereffect(_:).md)
  Sets the default hover effect to use for views within this view.
- [enum HoverPhase](hoverphase.md)
  The current hovering state and value of the pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/ishovereffectenabled)*