# renameAction(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Sets the rename action in the environment to update focus state.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func renameAction(_ isFocused: FocusState<Bool>.Binding) -> some View
```

#### Return Value

A view that has the specified rename action.

#### Discussion

Use this modifier in conjunction with the `RenameButton` to implement standard rename interactions. A rename button receives its action from the environment. Use this modifier to customize the action provided to the rename button.

```None
struct RowView: View {
    @State private var text = ""
    @FocusState private var isFocused: Bool

    var body: some View {
        TextField(text: $item.name) {
            Text("Prompt")
        }
        .focused($isFocused)
        .contextMenu {
            RenameButton()
            // ... your own custom actions
        }
        .renameAction($isFocused)
}
```

When someone taps the rename button in the context menu, the rename action focuses the text field by setting the `isFocused` property to true.

## Parameters

- `isFocused`: The focus binding to update when   activating the rename action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/renameaction(_:)-8ygjj)*