# dialogSeverity(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the severity for alerts.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func dialogSeverity(_ severity: DialogSeverity) -> some Scene
```

## Discussion

The following example configures an alert for erasing some number of items. Since this operation is destructive and non-recoverable, a `.critical` severity is used.

```swift
struct MyApp: App {
    @State private var isShowingDialog = false

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
        .dialogSeverity(.critical)
    }
}
```

## Parameters

- `severity`: The severity to use for alerts.

## See Also

### Configuring a dialog
- [func dialogIcon(Image?) -> some View](../view/dialogicon%28_%29.md)
  Configures the icon used by dialogs within this view.
- [func dialogIcon(Image?) -> some Scene](./dialogicon%28_%29.md)
  Configures the icon used by alerts.
- [func dialogSeverity(DialogSeverity) -> some View](../view/dialogseverity%28_%29.md)
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](../view/dialogsuppressiontoggle%28issuppressed%29.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some Scene](./dialogsuppressiontoggle%28issuppressed%29.md)
  Enables user suppression of an alert with a custom suppression message.
- [func dialogSuppressionToggle(_:isSuppressed:)](../view/dialogsuppressiontoggle%28_,issuppressed%29.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(_:isSuppressed:)](./dialogsuppressiontoggle%28_,issuppressed%29.md)
  Enables user suppression of an alert with a custom suppression message.
- [func dialogPreventsAppTermination(Bool?) -> some View](../view/dialogpreventsapptermination%28_%29.md)
  Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/dialogseverity(_:))*