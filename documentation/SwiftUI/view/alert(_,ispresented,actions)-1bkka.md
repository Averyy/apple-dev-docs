# alert(_:isPresented:actions:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents an alert when a given condition is true, using a string variable as a title.

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
func alert<S, A>(_ title: S, isPresented: Binding<Bool>, @ContentBuilder actions: () -> A) -> some View where S : StringProtocol, A : View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func alert<A>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, @ContentBuilder actions: () -> A) -> some View where A : View
```

```swift
nonisolated
func alert<A>(_ title: Text, isPresented: Binding<Bool>, @ContentBuilder actions: () -> A) -> some View where A : View
```

```swift
nonisolated
func alert<A>(_ titleKey: LocalizedStringKey, isPresented: Binding<Bool>, @ContentBuilder actions: () -> A) -> some View where A : View
```

## Discussion

In the example below, a login form conditionally presents an alert by setting the `didFail` state variable. When the form sets the value to to `true`, the system displays an alert with an “OK” action.

```swift
struct Login: View {
    @State private var didFail = false
    let alertTitle: String = "Login failed."

    var body: some View {
        LoginForm(didFail: $didFail)
            .alert(
                alertTitle,
                isPresented: $didFail
            ) {
                Button("OK") {
                    // Handle the acknowledgement.
                }
            }
    }
}
```

All actions in an alert dismiss the alert after the action runs. The default button is shown with greater prominence. You can influence the default button by assigning it the [`defaultAction`](../keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No default cancel action is provided. If you want to show a cancel action, use a button with a role of [`cancel`](../buttonrole/cancel.md).

On iOS, tvOS, and watchOS, alerts only support controls with labels that are [`Text`](../text.md). Passing any other type of view results in the content being omitted.

## Parameters

- `title`: A text string used as the title of the alert.
- `isPresented`: A binding to a Boolean value that determines whether to present the alert. When the user presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.
- `actions`: A [`ContentBuilder`](../contentbuilder.md) returning the alert’s actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:actions:)-1bkka)*