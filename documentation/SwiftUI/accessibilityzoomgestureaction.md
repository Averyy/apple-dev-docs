# AccessibilityZoomGestureAction

**Framework**: SwiftUI  
**Kind**: struct

Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct AccessibilityZoomGestureAction
```

## Topics

### Getting the action’s direction
- [let direction: AccessibilityZoomGestureAction.Direction](accessibilityzoomgestureaction/direction-swift.property.md)
  The zoom gesture’s direction.
- [AccessibilityZoomGestureAction.Direction](accessibilityzoomgestureaction/direction-swift.enum.md)
  A direction that matches the movement of a zoom gesture performed by an assistive technology, such as a swipe up and down in Voiceover’s zoom rotor.
### Getting location information
- [let location: UnitPoint](accessibilityzoomgestureaction/location.md)
  The zoom gesture’s activation point, normalized to the accessibility element’s frame.
- [let point: CGPoint](accessibilityzoomgestureaction/point.md)
  The zoom gesture’s activation point within the window’s coordinate space.

## See Also

- [func accessibilityActivationPoint(_:)](view/accessibilityactivationpoint(_:).md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(_:isEnabled:)](view/accessibilityactivationpoint(_:isenabled:).md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityDragPoint(_:description:)](view/accessibilitydragpoint(_:description:).md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(_:description:isEnabled:)](view/accessibilitydragpoint(_:description:isenabled:).md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDropPoint(_:description:)](view/accessibilitydroppoint(_:description:).md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(_:description:isEnabled:)](view/accessibilitydroppoint(_:description:isenabled:).md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilitydirecttouch(_:options:).md)
  Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityzoomaction(_:).md)
  Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [struct AccessibilityDirectTouchOptions](accessibilitydirecttouchoptions.md)
  An option set that defines the functionality of a view’s direct touch area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilityzoomgestureaction)*