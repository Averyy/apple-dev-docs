# accessibilityAction(intent:label:)

**Framework**: FinanceKitUI  
**Kind**: method

Adds an accessibility action labeled by the contents of `label` to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action. When the action is performed, the `intent` will be invoked.

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
func accessibilityAction<I, Label>(intent: I, @ViewBuilder label: () -> Label) -> some View where I : AppIntent, Label : View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/accessibilityaction(intent:label:))*