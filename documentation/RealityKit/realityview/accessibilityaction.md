# accessibilityAction(_:_:)

**Framework**: RealityKit  
**Kind**: method

Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func accessibilityAction(_ actionKind: AccessibilityActionKind = .default, _ handler: @escaping () -> Void) -> ModifiedContent<Self, AccessibilityAttachmentModifier>
```

#### Discussion

For example, this is how a `.default` action to compose a new email could be added to a view.

```None
var body: some View {
    ContentView()
        .accessibilityAction {
            // Handle action
        }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/accessibilityaction(_:_:))*