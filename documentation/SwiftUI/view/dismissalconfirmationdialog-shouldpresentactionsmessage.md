# dismissalConfirmationDialog(_:shouldPresent:actions:message:)

**Framework**: SwiftUI  
**Kind**: method

Presents a confirmation dialog when a dismiss action has been triggered.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func dismissalConfirmationDialog<A, M>(_ title: Text, shouldPresent: Bool, @ViewBuilder actions: () -> A, @ViewBuilder message: () -> M) -> some View where A : View, M : View
```

#### Discussion

On macOS, the dialog will be presented when attempting to dismiss the window for this view.

For example, you could present a dialog asking to persist unsaved changes:

struct ComposeMessage: View { @State private var message = Message()

```swift
var body: some View {
    MessageEditor(message: $message)
        .dismissalConfirmationDialog(
            "Save This Message As Draft?",
            shouldPresent: message.hasUnsavedChanges
        ) {
            Button("Save") {
                message.save()
            }
            Button("Don't Save", role: .destructive) {
                message.discard()
            }
        } message: {
            Text(
                """
                This message has not been sent and contains\
                unsaved changes.
                """)
        }
```

}

All actions in the dialog will dismiss the dialog after the action runs. The default button will be shown with greater prominence. You can influence the default button by assigning it the [`defaultAction`](keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

Dismissal dialogs include a standard cancellation action by default. If you provide a button with a role of [`cancel`](buttonrole/cancel.md), that button takes the place of the default cancellation action.

The cancellation action will always prevent the dismissal, while other actions will allow the dismiss to proceed.

## Parameters

- `title`: The title of the dialog.
- `shouldPresent`: A a Boolean value that determines whether   to present the dialog upon dismissal.
- `actions`: A view builder returning the dialog’s actions.
- `message`: A view builder returning the message for the dialog.

## See Also

- [func confirmationDialog(_:isPresented:titleVisibility:actions:message:)](view/confirmationdialog(_:ispresented:titlevisibility:actions:message:).md)
  Presents a confirmation dialog with a message when a given condition is true, using a text view for the title.
- [func confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)](view/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:).md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a text view for the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dismissalconfirmationdialog(_:shouldpresent:actions:message:))*