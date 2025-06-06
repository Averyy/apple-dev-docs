# accessibilityRespondsToUserInteraction(_:isEnabled:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Explicitly set whether this Accessibility element responds to user interaction and would thus be interacted with by technologies such as Switch Control, Voice Control or Full Keyboard Access.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func accessibilityRespondsToUserInteraction(_ respondsToUserInteraction: Bool, isEnabled: Bool) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

If this is not set, the value is inferred from the traits of the Accessibility element, the presence of Accessibility actions on the element, or the presence of gestures on the element or containing views.

## Parameters

- `respondsToUserInteraction`: Whether the view responds to user   interaction.
- `isEnabled`: If true the accessibility interaction state is applied;   otherwise the accessibility interaction state is unchanged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/accessibilityrespondstouserinteraction(_:isenabled:))*