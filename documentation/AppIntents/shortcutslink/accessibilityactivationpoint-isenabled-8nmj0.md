# accessibilityActivationPoint(_:isEnabled:)

**Framework**: App Intents  
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
func accessibilityActivationPoint(_ activationPoint: UnitPoint, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this modifier to ensure that the activation point for a small element remains accurate even if you present a larger version of the element to VoiceOver.

If an activation point is not provided, an activation point will be derived from one of the accessibility elements decedents or from the center of the accessibility frame.

## Parameters

- `activationPoint`: The accessibility activation point to apply.
- `isEnabled`: If true the accessibility activation point is applied;   otherwise the accessibility activation point is unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/accessibilityactivationpoint(_:isenabled:)-8nmj0)*