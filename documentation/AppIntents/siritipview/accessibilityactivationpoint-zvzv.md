# accessibilityActivationPoint(_:)

**Framework**: App Intents  
**Kind**: method

The activation point for an element is the location assistive technologies use to initiate gestures.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func accessibilityActivationPoint(_ activationPoint: CGPoint) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

Use this modifier to ensure that the activation point for a small element remains accurate even if you present a larger version of the element to VoiceOver.

If an activation point is not provided, an activation point will be derrived from one of the accessibility elements decendents or from the center of the accessibility frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/accessibilityactivationpoint(_:)-zvzv)*