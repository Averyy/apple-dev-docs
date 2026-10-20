# UIAccessibility.DirectTouchOptions

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum UIAccessibilityDirectTouchOptions : NSUInteger;
```

#### Overview

*Direct touch areas* are regions of the screen where VoiceOver passes gestures directly to the app instead of interpreting them as VoiceOver commands.

Examples of direct touch areas include:

- A keyboard in a music-creation app
- A player view in a game that produces sounds
- An area where you sign your name in a document

If an element doesn’t use `UIAccessibility.DirectTouchOptions`, VoiceOver speaks the element and immediately starts sending touch events to the app.

Specify `DirectTouchOptions` to customize VoiceOver regions using these two constants:

- Use [`silentOnTouch`](../../SwiftUI/accessibilitydirecttouchoptions/silentontouch.md) to ensure VoiceOver is silent when a person touches the direct touch area. In this region, the app produces its own audio feedback without conflicting with VoiceOver audio.
- Use [`requiresActivation`](../../SwiftUI/accessibilitydirecttouchoptions/requiresactivation.md) to ensure a person interacts with the user interface element before a touch passes through to the element. This is useful for scenarios where an errant touch may produce undesired input, such as a signature field.

## Topics

### Initializers
- [init(rawValue: UInt)](./directtouchoptions/init%28rawvalue%29.md)
  Creates a new direct touch options structure using an unsigned integer.
### Type Properties
- [static var requiresActivation: UIAccessibility.DirectTouchOptions](./directtouchoptions/requiresactivation.md)
  Inhibits passthrough to the direct touch area until a person double-taps the element.
- [static var silentOnTouch: UIAccessibility.DirectTouchOptions](./directtouchoptions/silentontouch.md)
  Allows a direct touch area to immediately receive touch events without triggering VoiceOver audio.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Configuring behavior
- [var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?](../../ObjectiveC/nsobject-swift.class/accessibilitycustomrotors.md)
- [var accessibilityElementsHidden: Bool](../../ObjectiveC/nsobject-swift.class/accessibilityelementshidden.md)
- [var accessibilityRespondsToUserInteraction: Bool](../../ObjectiveC/nsobject-swift.class/accessibilityrespondstouserinteraction.md)
- [var accessibilityViewIsModal: Bool](../../ObjectiveC/nsobject-swift.class/accessibilityviewismodal.md)
- [var shouldGroupAccessibilityChildren: Bool](../../ObjectiveC/nsobject-swift.class/shouldgroupaccessibilitychildren.md)
- [var accessibilityDirectTouchOptions: UIAccessibility.DirectTouchOptions](../../ObjectiveC/nsobject-swift.class/accessibilitydirecttouchoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/directtouchoptions)*