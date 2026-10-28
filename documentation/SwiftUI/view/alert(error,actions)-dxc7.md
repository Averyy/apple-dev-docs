# alert(error:actions:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents an alert when an error is present.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
func alert<E, A>(error: Binding<E?>, @ContentBuilder actions: () -> A) -> some View where E : Error, A : View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func alert<E, A>(error: Binding<E?>, @ContentBuilder actions: () -> A) -> some View where E : LocalizedError, A : View
```

## Discussion

In the example below, a form conditionally presents an alert depending upon the value of an error. When the error value isn’t `nil`, the system presents an alert with an “OK” action.

The title of the alert is inferred from the error’s `errorDescription` if the error is a `LocalizedError`; otherwise it will be `Error/localizedDescription`.

```swift
struct TicketPurchase: View {
    @State private var error: TicketPurchaseError? = nil

    var body: some View {
        TicketForm(error: $error)
            .alert(error: $error) {
                Button("OK") {
                    // Handle acknowledgement.
                }
            }
    }
}
```

All actions in an alert dismiss the alert after the action runs. The default button is shown with greater prominence. You can influence the default button by assigning it the [`defaultAction`](../keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No default cancel action is provided. If you want to show a cancel action, use a button with a role of [`cancel`](../buttonrole/cancel.md).

On iOS, tvOS, and watchOS, alerts only support controls with labels that are [`Text`](../text.md). Passing any other type of view results in the content being omitted.

This modifier creates a [`Text`](../text.md) view for the title on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `error`: A binding to an optional localized Error. The system presents the alert when the binding’s value is non-nil, and uses the error to generate the alert’s title. When the user presses or taps one of the alert’s actions, the system sets this value to `nil` and dismisses. If the error is a `LocalizedError`, its `errorDescription` will be used as the title, otherwise, the title will be `Error/localizedDescription`.
- `actions`: A [`ContentBuilder`](../contentbuilder.md) returning the alert’s actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/alert(error:actions:)-dxc7)*