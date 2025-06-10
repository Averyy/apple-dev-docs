# alert(_:isPresented:actions:message:)

**Framework**: FinanceKitUI  
**Kind**: method

Presents an alert with a message when a given condition is true, using a localized string resource for a title.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func alert<A, M>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, @ViewBuilder actions: () -> A, @ViewBuilder message: () -> M) -> some View where A : View, M : View
```

#### Discussion

In the example below, a login form conditionally presents an alert by setting the `didFail` state variable. When the form sets the value to to `true`, the system displays an alert with an “OK” action.

```None
struct Login: View {
    @State private var didFail = false

    var body: some View {
        LoginForm(didFail: $didFail)
            .alert(
                "Login failed.",
                isPresented: $didFail
            ) {
                Button("OK") {
                    // Handle the acknowledgement.
                }
            } message: {
                Text("Please check your credentials and try again.")
            }
    }
}
```

All actions in an alert dismiss the alert after the action runs. The default button is shown with greater prominence.  You can influence the default button by assigning it the `KeyboardShortcut/defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No default cancel action is provided. If you want to show a cancel action, use a button with a role of `ButtonRole/cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are `Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

This modifier creates a `Text` view for the title on your behalf. See `Text` for more information about localizing strings.

## Parameters

- `titleResource`: Text resource for the localized string that describes   the title of the alert.
- `isPresented`: A binding to a Boolean value that determines whether to   present the alert. When the user presses or taps one of the alert’s   actions, the system sets this value to   and dismisses.
- `actions`: A   returning the alert’s actions.
- `message`: A   returning the message for the alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/alert(_:ispresented:actions:message:)-24mh2)*