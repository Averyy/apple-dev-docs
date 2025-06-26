# alert(_:isPresented:actions:message:)

**Framework**: FamilyControls  
**Kind**: method

Presents an alert with a message when a given condition is true using a text view as a title.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func alert<A, M>(_ title: Text, isPresented: Binding<Bool>, @ViewBuilder actions: () -> A, @ViewBuilder message: () -> M) -> some View where A : View, M : View
```

#### Discussion

In the example below, a login form conditionally presents an alert by setting the `didFail` state variable. When the form sets the value to to `true`, the system displays an alert with an “OK” action.

```swift
struct Login: View {
    @State private var didFail = false
    let alertTitle: String = "Login failed."

    var body: some View {
        LoginForm(didFail: $didFail)
            .alert(
                Text(alertTitle),
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

## Parameters

- `title`: The title of the alert.
- `isPresented`: A binding to a Boolean value that determines whether to   present the alert. When the user presses or taps one of the alert’s   actions, the system sets this value to   and dismisses.
- `actions`: A   returning the alert’s actions.
- `message`: A   returning the message for the alert.

## See Also

- [func alert<S, A, M>(S, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](familyactivitypicker/alert(_:ispresented:actions:message:)-5d7w0.md)
  Presents an alert with a message when a given condition is true using a string variable as a title.
- [func alert<A, M>(LocalizedStringKey, isPresented: Binding<Bool>, actions: () -> A, message: () -> M) -> some View](familyactivitypicker/alert(_:ispresented:actions:message:)-8ae3a.md)
  Presents an alert with a message when a given condition is true, using a localized string key for a title.
- [func alert<A, M, T>(LocalizedStringKey, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](familyactivitypicker/alert(_:ispresented:presenting:actions:message:)-233cu.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [func alert<A, M, T>(Text, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](familyactivitypicker/alert(_:ispresented:presenting:actions:message:)-2d9eq.md)
  Presents an alert with a message using the given data to produce the alert’s content and a text view for a title.
- [func alert<S, A, M, T>(S, isPresented: Binding<Bool>, presenting: T?, actions: (T) -> A, message: (T) -> M) -> some View](familyactivitypicker/alert(_:ispresented:presenting:actions:message:)-7626v.md)
  Presents an alert with a message using the given data to produce the alert’s content and a string variable as a title.
- [func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A, message: (E) -> M) -> some View](familyactivitypicker/alert(ispresented:error:actions:message:).md)
  Presents an alert with a message when an error is present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/alert(_:ispresented:actions:message:)-3yino)*