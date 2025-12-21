# UIAccessibility.DirectTouchOptions

**Framework**: UIKit  
**Kind**: struct

Constants that configure how VoiceOver produces audio for direct touch areas.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct DirectTouchOptions
```

#### Overview

 are regions of the screen where VoiceOver passes gestures directly to the app instead of interpreting them as VoiceOver commands.

Examples of direct touch areas include:

- A keyboard in a music-creation app
- A player view in a game that produces sounds
- An area where you sign your name in a document

If an element doesn’t use `UIAccessibility.DirectTouchOptions`, VoiceOver speaks the element and immediately starts sending touch events to the app.

Specify `DirectTouchOptions` to customize VoiceOver regions using these two constants:

- Use [`silentOnTouch`](https://developer.apple.com/documentation/SwiftUI/AccessibilityDirectTouchOptions/silentOnTouch) to ensure VoiceOver is silent when a person touches the direct touch area. In this region, the app produces its own audio feedback without conflicting with VoiceOver audio.
- Use [`requiresActivation`](https://developer.apple.com/documentation/SwiftUI/AccessibilityDirectTouchOptions/requiresActivation) to ensure a person interacts with the user interface element before a touch passes through to the element. This is useful for scenarios where an errant touch may produce undesired input, such as a signature field.

## Topics

### Initializers
- [init(rawValue: UInt)](uiaccessibility/directtouchoptions/init(rawvalue:).md)
  Creates a new direct touch options structure using an unsigned integer.
### Type Properties
- [static var requiresActivation: UIAccessibility.DirectTouchOptions](uiaccessibility/directtouchoptions/requiresactivation.md)
  Inhibits passthrough to the direct touch area until a person double-taps the element.
- [static var silentOnTouch: UIAccessibility.DirectTouchOptions](uiaccessibility/directtouchoptions/silentontouch.md)
  Allows a direct touch area to immediately receive touch events without triggering VoiceOver audio.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?](../ObjectiveC/NSObject-swift.class/accessibilityCustomRotors.md)
- [var accessibilityElementsHidden: Bool](../ObjectiveC/NSObject-swift.class/accessibilityElementsHidden.md)
- [var accessibilityRespondsToUserInteraction: Bool](../ObjectiveC/NSObject-swift.class/accessibilityRespondsToUserInteraction.md)
- [var accessibilityViewIsModal: Bool](../ObjectiveC/NSObject-swift.class/accessibilityViewIsModal.md)
- [var shouldGroupAccessibilityChildren: Bool](../ObjectiveC/NSObject-swift.class/shouldGroupAccessibilityChildren.md)
- [var accessibilityDirectTouchOptions: UIAccessibility.DirectTouchOptions](../ObjectiveC/NSObject-swift.class/accessibilityDirectTouchOptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/directtouchoptions)*