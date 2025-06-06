# alert(isPresented:error:actions:message:)

**Framework**: SwiftUI  
**Kind**: method

Presents an alert with a message when an error is present.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, @ViewBuilder actions: (E) -> A, @ViewBuilder message: (E) -> M) -> some View where E : LocalizedError, A : View, M : View
```

#### Discussion

In the example below, a form conditionally presents an alert depending upon the value of an error. When the error value isn’t `nil`, the system presents an alert with an “OK” action.

The title of the alert is inferred from the error’s `errorDescription`.

```swift
struct TicketPurchase: View {
    @State private var error: TicketPurchaseError? = nil
    @State private var showAlert = false

    var body: some View {
        TicketForm(showAlert: $showAlert, error: $error)
            .alert(isPresented: $showAlert, error: error) { _ in
                Button("OK") {
                    // Handle acknowledgement.
                }
            } message: { error in
                Text(error.recoverySuggestion ?? "Try again later.")
            }
    }
}
```

All actions in an alert dismiss the alert after the action runs. The default button is shown with greater prominence.  You can influence the default button by assigning it the [`defaultAction`](keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No default cancel action is provided. If you want to show a cancel action, use a button with a role of [`cancel`](buttonrole/cancel.md).

On iOS, tvOS, and watchOS, alerts only support controls with labels that are [`Text`](text.md). Passing any other type of view results in the content being omitted.

This modifier creates a [`Text`](text.md) view for the title on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See [`Text`](text.md) for more information about localizing strings.

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether to   present the alert. When the user presses or taps one of the alert’s   actions, the system sets this value to   and dismisses.
- `error`: An optional localized Error that is used to generate the   alert’s title.  The system passes the contents to the modifier’s   closures. You use this data to populate the fields of an alert that   you create that the system displays to the user.
- `actions`: A   returning the alert’s actions.
- `message`: A view builder returning the message for the alert given   the current error.

## See Also

- [struct AlertScene](alertscene.md)
  A scene that renders itself as a standalone alert dialog.
- [func alert(_:isPresented:actions:)](view/alert(_:ispresented:actions:).md)
  Presents an alert when a given condition is true, using a text view for the title.
- [func alert(_:isPresented:presenting:actions:)](view/alert(_:ispresented:presenting:actions:).md)
  Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) -> some View](view/alert(ispresented:error:actions:).md)
  Presents an alert when an error is present.
- [func alert(_:isPresented:actions:message:)](view/alert(_:ispresented:actions:message:).md)
  Presents an alert with a message when a given condition is true using a text view as a title.
- [func alert(_:isPresented:presenting:actions:message:)](view/alert(_:ispresented:presenting:actions:message:).md)
  Presents an alert with a message using the given data to produce the alert’s content and a text view for a title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/alert(ispresented:error:actions:message:))*