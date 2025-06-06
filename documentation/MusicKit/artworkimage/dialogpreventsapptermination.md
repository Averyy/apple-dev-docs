# dialogPreventsAppTermination(_:)

**Framework**: MusicKit  
**Kind**: method

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

- There is only a single button and its role is not `ButtonRole/destructive`
- The `View/dialogSeverity(_:)` is not `DialogSeverity/critical``
- There are no `TextField`s

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/dialogpreventsapptermination(_:))*