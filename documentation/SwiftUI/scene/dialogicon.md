# dialogIcon(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the icon used by alerts.

**Availability**:
- macOS 15.0+

## Declaration

```swift
nonisolated
func dialogIcon(_ icon: Image?) -> some Scene
```

#### Discussion

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

- `icon`: The custom icon to use for the alert.   Passing   will use the default app icon.

## See Also

- [func dialogIcon(Image?) -> some View](view/dialogicon(_:).md)
  Configures the icon used by dialogs within this view.
- [func dialogSeverity(DialogSeverity) -> some View](view/dialogseverity(_:).md)
- [func dialogSeverity(DialogSeverity) -> some Scene](scene/dialogseverity(_:).md)
  Sets the severity for alerts.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](view/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some Scene](scene/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of an alert with a custom suppression message.
- [func dialogSuppressionToggle(_:isSuppressed:)](view/dialogsuppressiontoggle(_:issuppressed:).md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(_:isSuppressed:)](scene/dialogsuppressiontoggle(_:issuppressed:).md)
  Enables user suppression of an alert with a custom suppression message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/dialogicon(_:))*