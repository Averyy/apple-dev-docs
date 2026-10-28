# alert(_:isPresented:actions:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents an alert when a given condition is true, using a localized string resource for the title.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
nonisolated func alert<A>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, @ContentBuilder actions: () -> A) -> some View where A : View
```

**Other overloads**:

```swift
nonisolated
func alert<A>(_ title: Text, isPresented: Binding<Bool>, @ContentBuilder actions: () -> A) -> some View where A : View
```

```swift
nonisolated
func alert<A>(_ titleKey: LocalizedStringKey, isPresented: Binding<Bool>, @ContentBuilder actions: () -> A) -> some View where A : View
```

```swift
nonisolated
func alert<S, A>(_ title: S, isPresented: Binding<Bool>, @ContentBuilder actions: () -> A) -> some View where S : StringProtocol, A : View
```

## Discussion

In the example below, a login form conditionally presents an alert by setting the `didFail` state variable. When the form sets the value to to `true`, the system displays an alert with an “OK” action.

```swift
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
            }
    }
}
```

All actions in an alert dismiss the alert after the action runs. The default button is shown with greater prominence. You can influence the default button by assigning it the [`defaultAction`](../keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No default cancel action is provided. If you want to show a cancel action, use a button with a role of [`cancel`](../buttonrole/cancel.md).

On iOS, tvOS, and watchOS, alerts only support controls with labels that are [`Text`](../text.md). Passing any other type of view results in the content being omitted.

This modifier creates a [`Text`](../text.md) view for the title on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `titleResource`: Text resource for the localized string that describes the title of the alert.
- `isPresented`: A binding to a Boolean value that determines whether to present the alert. When the user presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.
- `actions`: A [`ContentBuilder`](../contentbuilder.md) returning the alert’s actions.

## See Also

### Presenting an alert
- [struct AlertScene](../alertscene.md)
  A scene that renders itself as a standalone alert dialog.
- [func alert(_:isPresented:presenting:actions:)](./alert%28_,ispresented,presenting,actions%29.md)
  Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.
- [func alert(_:item:actions:)](./alert%28_,item,actions%29.md)
  Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [func alert(error:actions:)](./alert%28error,actions%29.md)
  Presents an alert when an error is present.
- [func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) -> some View](./alert%28ispresented,error,actions%29.md)
  Presents an alert when an error is present.
- [func alert(_:isPresented:actions:message:)](./alert%28_,ispresented,actions,message%29.md)
  Presents an alert with a message when a given condition is true, using a localized string resource for a title.
- [func alert(_:isPresented:presenting:actions:message:)](./alert%28_,ispresented,presenting,actions,message%29.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.
- [func alert(_:item:actions:message:)](./alert%28_,item,actions,message%29.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [func alert(error:actions:message:)](./alert%28error,actions,message%29.md)
  Presents an alert with a message when an error is present.
- [func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A, message: (E) -> M) -> some View](./alert%28ispresented,error,actions,message%29.md)
  Presents an alert with a message when an error is present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:actions:))*