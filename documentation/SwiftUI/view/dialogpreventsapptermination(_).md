# dialogPreventsAppTermination(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
nonisolated
func dialogPreventsAppTermination(_ prevents: Bool?) -> some View
```

#### Discussion

SwiftUI uses the actions passed to the above dialogs to determine whether the dialog should block app termination by default when presented. If all of the following are satisfied, the dialog will not block app quit:

- There is only a single button and its role is not [`destructive`](../buttonrole/destructive.md)
- The [`dialogSeverity(_:)`](./dialogseverity%28_%29.md) is not `DialogSeverity/critical``
- There are no [`TextField`](../textfield.md)s

Use this modifier after a `View/alert` or `View/confirmationDialog` to specify whether the dialog should prevent app termination. Pass `nil` to explicitly request the automatic behavior/for the inert version of this modifier.

```swift
struct ConfirmLogoutView: View {
  @State private var isConfirming = false

  var body: some View {
    Button("Logout") { isConfirming = true }
      .confirmationDialog(
        Text("Logout?"),
          isPresented: $isConfirming
        ) {
          Button("Yes") {
            // Handle logout action.
          }
        }
        .dialogPreventsAppTermination(false)
    }
}
```

## See Also

### Configuring a dialog
- [func dialogIcon(Image?) -> some View](./dialogicon%28_%29.md)
  Configures the icon used by dialogs within this view.
- [func dialogIcon(Image?) -> some Scene](../scene/dialogicon%28_%29.md)
  Configures the icon used by alerts.
- [func dialogSeverity(DialogSeverity) -> some View](./dialogseverity%28_%29.md)
- [func dialogSeverity(DialogSeverity) -> some Scene](../scene/dialogseverity%28_%29.md)
  Sets the severity for alerts.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](./dialogsuppressiontoggle%28issuppressed%29.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some Scene](../scene/dialogsuppressiontoggle%28issuppressed%29.md)
  Enables user suppression of an alert with a custom suppression message.
- [func dialogSuppressionToggle(_:isSuppressed:)](./dialogsuppressiontoggle%28_,issuppressed%29.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(_:isSuppressed:)](../scene/dialogsuppressiontoggle%28_,issuppressed%29.md)
  Enables user suppression of an alert with a custom suppression message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/dialogpreventsapptermination(_:))*