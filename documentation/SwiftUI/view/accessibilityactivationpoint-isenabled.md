# accessibilityActivationPoint(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

The activation point for an element is the location assistive technologies use to initiate gestures.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func accessibilityActivationPoint(_ activationPoint: CGPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this modifier to ensure that the activation point for a small element remains accurate even if you present a larger version of the element to VoiceOver.

If an activation point is not provided, an activation point will be derived from one of the accessibility elements decedents or from the center of the accessibility frame.

## Parameters

- `activationPoint`: The accessibility activation point to apply.
- `isEnabled`: If true the accessibility activation point is applied;   otherwise the accessibility activation point is unchanged.

## See Also

- [func accessibilityActivationPoint(_:)](view/accessibilityactivationpoint(_:).md)
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
- [struct AccessibilityZoomGestureAction](accessibilityzoomgestureaction.md)
  Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityactivationpoint(_:isenabled:))*