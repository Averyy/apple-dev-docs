# dialogSuppressionToggle(_:isSuppressed:)

**Framework**: SwiftUI  
**Kind**: method

Enables user suppression of an alert with a custom suppression message.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func dialogSuppressionToggle(_ label: Text, isSuppressed: Binding<Bool>) -> some Scene
```

#### Discussion

Applying dialog suppression adds a toggle to dialogs on macOS, which allows the user to request the alert not be displayed again. Typically whether a dialog is suppressed is stored in `AppStorage` and used to decide whether to present the dialog in the future.

The following example configures an alert with a suppression toggle. The toggle’s state is stored in `AppStorage` and used to determine whether or not to show the dialog when the “Delete Items” button is pressed.

```swift
struct MyApp: App {
    @State private var isShowingDialog = false
    @AppStorage("suppressEraseItemAlert")
    private var suppressAlert = false

    var body: some Scene {
        Window(...) {
            Button("Delete items") {
                isShowingDialog = true
            }
        }

        AlertScene(
            "Are you sure you want to erase these items?",
            isPresented: $isShowingDialog
        ) {
            Button("Erase", role: .destructive) {
                // Handle item deletion.
            }
            Button("Cancel", role: .cancel) {
                // Handle cancellation
            }
        }
        .dialogSuppressionToggle(
            "Do not ask about erasing items again",
            isSuppressed: $suppressAlert)
    }
}
```

## Parameters

- `label`: The label of the suppression toggle in the dialog. This   parameter can be elided to use the default suppression title.
- `isSuppressed`: Whether the suppression toggle is on or off in the   dialog.

## See Also

- [func dialogIcon(Image?) -> some Scene](scene/dialogicon(_:).md)
  Configures the icon used by alerts.
- [func dialogSeverity(DialogSeverity) -> some Scene](scene/dialogseverity(_:).md)
  Sets the severity for alerts.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some Scene](scene/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of an alert with a custom suppression message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/dialogsuppressiontoggle(_:issuppressed:))*