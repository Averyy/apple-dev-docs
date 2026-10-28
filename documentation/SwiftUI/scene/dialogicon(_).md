# dialogIcon(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the icon used by alerts.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func dialogIcon(_ icon: Image?) -> some Scene
```

## Discussion

In macOS, this icon replaces the default icon of the app.

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
        .dialogIcon(Image(Trash.png))
    }
}
```

## Parameters

- `icon`: The custom icon to use for the alert. Passing `nil` will use the default app icon.

## See Also

### Configuring a dialog
- [func dialogIcon(Image?) -> some View](../view/dialogicon%28_%29.md)
  Configures the icon used by dialogs within this view.
- [func dialogSeverity(DialogSeverity) -> some View](../view/dialogseverity%28_%29.md)
- [func dialogSeverity(DialogSeverity) -> some Scene](./dialogseverity%28_%29.md)
  Sets the severity for alerts.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/dialogicon(_:))*