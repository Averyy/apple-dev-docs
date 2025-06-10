# AccessibilityDirectTouchOptions

**Framework**: SwiftUI  
**Kind**: struct

An option set that defines the functionality of a view’s direct touch area.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct AccessibilityDirectTouchOptions
```

## Topics

### Getting the options
- [static let requiresActivation: AccessibilityDirectTouchOptions](accessibilitydirecttouchoptions/requiresactivation.md)
  Prevents touch passthrough with the direct touch area until an assistive technology, such as VoiceOver, has activated the direct touch area through a user action, for example a double tap.
- [static let silentOnTouch: AccessibilityDirectTouchOptions](accessibilitydirecttouchoptions/silentontouch.md)
  Allows a direct touch area to immediately receive touch events without an assitive technology, such as VoiceOver, speaking. Appropriate for apps that provide direct audio feedback on touch that would conflict with speech feedback.
### Creating a set of options
- [init(rawValue: AccessibilityDirectTouchOptions.RawValue)](accessibilitydirecttouchoptions/init(rawvalue:).md)
  Create a set of direct touch options

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [struct AccessibilityZoomGestureAction](accessibilityzoomgestureaction.md)
  Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitydirecttouchoptions)*