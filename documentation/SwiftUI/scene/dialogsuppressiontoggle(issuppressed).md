# dialogSuppressionToggle(isSuppressed:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Enables user suppression of an alert with a custom suppression message.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some Scene
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

- `isSuppressed`: Whether the suppression toggle is on or off in the dialog.

## See Also

### Configuring a dialog
- [func dialogIcon(Image?) -> some View](../view/dialogicon%28_%29.md)
  Configures the icon used by dialogs within this view.
- [func dialogIcon(Image?) -> some Scene](./dialogicon%28_%29.md)
  Configures the icon used by alerts.
- [func dialogSeverity(DialogSeverity) -> some View](../view/dialogseverity%28_%29.md)
- [func dialogSeverity(DialogSeverity) -> some Scene](./dialogseverity%28_%29.md)
  Sets the severity for alerts.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](../view/dialogsuppressiontoggle%28issuppressed%29.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(_:isSuppressed:)](../view/dialogsuppressiontoggle%28_,issuppressed%29.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(_:isSuppressed:)](./dialogsuppressiontoggle%28_,issuppressed%29.md)
  Enables user suppression of an alert with a custom suppression message.
- [func dialogPreventsAppTermination(Bool?) -> some View](../view/dialogpreventsapptermination%28_%29.md)
  Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/dialogsuppressiontoggle(issuppressed:))*