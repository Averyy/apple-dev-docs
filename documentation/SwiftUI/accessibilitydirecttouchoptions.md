# AccessibilityDirectTouchOptions

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [static let requiresActivation: AccessibilityDirectTouchOptions](./accessibilitydirecttouchoptions/requiresactivation.md)
  Prevents touch passthrough with the direct touch area until an assistive technology, such as VoiceOver, has activated the direct touch area through a user action, for example a double tap.
- [static let silentOnTouch: AccessibilityDirectTouchOptions](./accessibilitydirecttouchoptions/silentontouch.md)
  Allows a direct touch area to immediately receive touch events without an assitive technology, such as VoiceOver, speaking. Appropriate for apps that provide direct audio feedback on touch that would conflict with speech feedback.
### Creating a set of options
- [init(rawValue: AccessibilityDirectTouchOptions.RawValue)](./accessibilitydirecttouchoptions/init%28rawvalue%29.md)
  Create a set of direct touch options

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Making gestures accessible
- [func accessibilityActivationPoint(_:)](./view/accessibilityactivationpoint%28_%29.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityActivationPoint(_:isEnabled:)](./view/accessibilityactivationpoint%28_,isenabled%29.md)
  The activation point for an element is the location assistive technologies use to initiate gestures.
- [func accessibilityDragPoint(_:description:)](./view/accessibilitydragpoint%28_,description%29.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDragPoint(_:description:isEnabled:)](./view/accessibilitydragpoint%28_,description,isenabled%29.md)
  The point an assistive technology should use to begin a drag interaction.
- [func accessibilityDropPoint(_:description:)](./view/accessibilitydroppoint%28_,description%29.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDropPoint(_:description:isEnabled:)](./view/accessibilitydroppoint%28_,description,isenabled%29.md)
  The point an assistive technology should use to end a drag interaction.
- [func accessibilityDirectTouch(Bool, options: AccessibilityDirectTouchOptions) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilitydirecttouch%28_,options%29.md)
  Explicitly set whether this accessibility element is a direct touch area. Direct touch areas passthrough touch events to the app rather than being handled through an assistive technology, such as VoiceOver. The modifier accepts an optional `AccessibilityDirectTouchOptions` option set to customize the functionality of the direct touch area.
- [func accessibilityZoomAction((AccessibilityZoomGestureAction) -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](./view/accessibilityzoomaction%28_%29.md)
  Adds an accessibility zoom action to the view. Actions allow assistive technologies, such as VoiceOver, to interact with the view by invoking the action.
- [struct AccessibilityZoomGestureAction](./accessibilityzoomgestureaction.md)
  Position and direction information of a zoom gesture that someone performs with an assistive technology like VoiceOver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitydirecttouchoptions)*