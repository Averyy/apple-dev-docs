# accessibilityAction(action:label:)

**Framework**: Assignables  
**Kind**: method

Adds an accessibility action to the view. Actions allow assistive technologies, such as the VoiceOver, to interact with the view by invoking the action.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func accessibilityAction<Label>(action: @escaping () -> Void, @ViewBuilder label: () -> Label) -> some View where Label : View
```

#### Discussion

For example, this is how a custom action to compose a new email could be added to a view.

```None
var body: some View {
    ContentView()
        .accessibilityAction {
            // Handle action
        } label: {
            Label("New Message", systemImage: "plus")
        }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/accessibilityaction(action:label:))*