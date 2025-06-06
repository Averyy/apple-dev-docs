# RenameButton

**Framework**: SwiftUI  
**Kind**: struct

A button that triggers a standard rename action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct RenameButton<Label> where Label : View
```

#### Overview

A rename button receives its action from the environment. Use the [`renameAction(_:)`](view/renameaction(_:).md) modifier to set the action. The system disables the button if you don’t define an action.

```swift
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
        .renameAction { $isFocused = true }
}
```

When someone taps the rename button in the context menu, the rename action focuses the text field by setting the `isFocused` property to true.

You can use this button inside of a navigation title menu and the navigation title modifier automatically configures the environment with the appropriate rename action.

```swift
ContentView()
    .navigationTitle($contentTitle) {
        // ... your own custom actions
        RenameButton()
    }
```

## Topics

### Creating an rename button
- [init()](renamebutton/init.md)
  Creates a rename button.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [struct EditButton](editbutton.md)
  A button that toggles the edit mode environment value.
- [struct PasteButton](pastebutton.md)
  A system button that reads items from the pasteboard and delivers it to a closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/renamebutton)*