# dialogSuppressionToggle(_:isSuppressed:)

**Framework**: SwiftUI  
**Kind**: method

Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func dialogSuppressionToggle(_ label: Text, isSuppressed: Binding<Bool>) -> some View
```

#### Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows the user to request the alert not be displayed again. Typically whether a dialog is suppressed is stored in `AppStorage` and used to decide whether to present the dialog in the future.

The following example configures a `confirmationDialog` with a suppression toggle. The toggle’s state is stored in `AppStorage` and used to determine whether or not to show the dialog when the “Delete Items” button is pressed.

```swift
struct ConfirmEraseItems: View {
    @State private var isShowingDialog = false

    @AppStorage("suppressEraseItemAlert")
    private var suppressAlert = false

    var body: some View {
        Button("Delete Items") {
            if !suppressAlert {
                isShowingDialog = true
            } else {
                // Handle item deletion.
            }
        }
        .confirmationDialog(
            "Are you sure you want to erase these items?",
            isPresented: $isShowingDialog
        ) {
            Button("Erase", role: .destructive) {
                // Handle item deletion.
            }
            Button("Cancel", role: .cancel) {
                isShowingDialog = false
            }
        }
        .dialogSuppressionToggle(
            Text("Do not ask about erasing items again"),
            isSuppressed: $suppressAlert)
    }
}
```

## Parameters

- `label`: The label of the suppression toggle in the dialog. This   parameter can be elided to use the default suppression title.
- `isSuppressed`: Whether the suppression toggle is on or off in the   dialog.

## See Also

- [func dialogIcon(Image?) -> some View](view/dialogicon(_:).md)
  Configures the icon used by dialogs within this view.
- [func dialogIcon(Image?) -> some Scene](scene/dialogicon(_:).md)
  Configures the icon used by alerts.
- [func dialogSeverity(DialogSeverity) -> some View](view/dialogseverity(_:).md)
- [func dialogSeverity(DialogSeverity) -> some Scene](scene/dialogseverity(_:).md)
  Sets the severity for alerts.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](view/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some Scene](scene/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of an alert with a custom suppression message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dialogsuppressiontoggle(_:issuppressed:))*