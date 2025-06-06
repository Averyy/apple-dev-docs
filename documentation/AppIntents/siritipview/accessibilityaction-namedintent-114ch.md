# accessibilityAction(named:intent:)

**Framework**: App Intents  
**Kind**: method

Adds an accessibility action labeled `name` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.

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
func accessibilityAction<I>(named name: Text, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where I : AppIntent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/accessibilityaction(named:intent:)-114ch)*