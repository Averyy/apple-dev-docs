# dismissalConfirmationDialog(_:shouldPresent:actions:message:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a confirmation dialog upon an attempt to dismiss the window for this view.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 15.0+

## Declaration

```swift
nonisolated
func dismissalConfirmationDialog<A, M>(_ titleKey: LocalizedStringKey, shouldPresent: Bool, @ContentBuilder actions: () -> A, @ContentBuilder message: () -> M) -> some View where A : View, M : View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func dismissalConfirmationDialog<A, M>(_ titleResource: LocalizedStringResource, shouldPresent: Bool, @ContentBuilder actions: () -> A, @ContentBuilder message: () -> M) -> some View where A : View, M : View
```

```swift
nonisolated
func dismissalConfirmationDialog<A, M>(_ title: Text, shouldPresent: Bool, @ContentBuilder actions: () -> A, @ContentBuilder message: () -> M) -> some View where A : View, M : View
```

```swift
nonisolated
func dismissalConfirmationDialog<S, A, M>(_ title: S, shouldPresent: Bool, @ContentBuilder actions: () -> A, @ContentBuilder message: () -> M) -> some View where S : StringProtocol, A : View, M : View
```

## Discussion

On macOS, the dialog will be presented when attempting to dismiss the window for this view, either through a user-initiated dismissal or a programmatic dismiss action. On iOS, the dialog will only be presented for a user-initiated dismissal.

For example, you could present a dialog asking to persist unsaved changes:

```swift
struct ComposeMessage: View {
    @State private var message = Message()

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
}
```

All actions in the dialog will dismiss the dialog after the action runs. The default button will be shown with greater prominence. You can influence the default button by assigning it the [`defaultAction`](../keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

Dismissal dialogs include a standard cancellation action by default. If you provide a button with a role of [`cancel`](../buttonrole/cancel.md), that button takes the place of the default cancellation action.

The cancellation action will always prevent the dismissal, while other actions will allow the dismiss to proceed.

On iOS, in addition to the standard cancellation action, the dismissal dialog also includes a standard close action by default. If you provide a button with a role of [`destructive`](../buttonrole/destructive.md), that button takes the place of the default close action. This action will immediately dismiss the dialog and the view’s associated window.

## Parameters

- `titleKey`: The key for the localized string that describes the title of the dialog.
- `shouldPresent`: A Boolean value that determines whether to present the dialog upon dismissal.
- `actions`: A content builder returning the dialog’s actions.
- `message`: A content builder returning the message for the dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dismissalconfirmationdialog(_:shouldpresent:actions:message:)-31gad)*