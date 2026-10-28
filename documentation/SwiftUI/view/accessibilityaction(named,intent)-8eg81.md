# accessibilityAction(named:intent:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an accessibility action labeled with the localized representation of `nameKey` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.

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
func accessibilityAction<I>(named nameKey: LocalizedStringKey, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where I : AppIntent
```

**Other overloads**:

```swift
nonisolated
func accessibilityAction<I>(named name: Text, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where I : AppIntent
```

```swift
nonisolated
func accessibilityAction<I>(named nameResource: LocalizedStringResource, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where I : AppIntent
```

```swift
nonisolated
func accessibilityAction<S, I>(named name: S, intent: I) -> ModifiedContent<Self, AccessibilityAttachmentModifier> where S : StringProtocol, I : AppIntent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/accessibilityaction(named:intent:)-8eg81)*