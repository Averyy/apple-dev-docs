# alert(_:isPresented:presenting:actions:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.

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
nonisolated func alert<A, T>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, presenting data: T?, @ContentBuilder actions: (T) -> A) -> some View where A : View
```

**Other overloads**:

```swift
nonisolated
func alert<A, T>(_ title: Text, isPresented: Binding<Bool>, presenting data: T?, @ContentBuilder actions: (T) -> A) -> some View where A : View
```

```swift
nonisolated
func alert<A, T>(_ titleKey: LocalizedStringKey, isPresented: Binding<Bool>, presenting data: T?, @ContentBuilder actions: (T) -> A) -> some View where A : View
```

```swift
nonisolated
func alert<S, A, T>(_ title: S, isPresented: Binding<Bool>, presenting data: T?, @ContentBuilder actions: (T) -> A) -> some View where S : StringProtocol, A : View
```

#### Discussion

For the alert to appear, both `isPresented` must be `true` and `data` must not be `nil`. The data should not change after the presentation occurs. Any changes that you make after the presentation occurs are ignored.

Use this method when you need to populate the fields of an alert with content from a data source. The example below shows a custom data source, `SaveDetails`, that provides data to populate the alert:

```swift
struct SaveDetails: Identifiable {
    let name: String
    let error: String
    let id = UUID()
}

struct SaveButton: View {
    @State private var didError = false
    @State private var details: SaveDetails?

    var body: some View {
        Button("Save") {
            details = model.save(didError: $didError)
        }
        .alert(
            "Save failed.",
            isPresented: $didError,
            presenting: details
        ) { details in
            Button(role: .destructive) {
                // Handle the deletion.
            } label: {
                Text("Delete \(details.name)")
            }
            Button("Retry") {
                // Handle the retry action.
            }
        }
    }
}
```

This modifier creates a [`Text`](../text.md) view for the title on your behalf. See [`Text`](../text.md) for more information about localizing strings.

All actions in an alert dismiss the alert after the action runs. The default button is shown with greater prominence. You can influence the default button by assigning it the [`defaultAction`](../keyboardshortcut/defaultaction.md) keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No default cancel action is provided. If you want to show a cancel action, use a button with a role of [`cancel`](../buttonrole/cancel.md).

On iOS, tvOS, and watchOS, alerts only support controls with labels that are [`Text`](../text.md). Passing any other type of view results in the content being omitted.

## Parameters

- `titleResource`: Text resource for the localized string that describes the title of the alert.
- `isPresented`: A binding to a Boolean value that determines whether to present the alert. When the user presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.
- `data`: An optional source of truth for the alert. The system passes the contents to the modifier’s closures. You use this data to populate the fields of an alert that you create that the system displays to the user.
- `actions`: A [`ContentBuilder`](../contentbuilder.md) returning the alert’s actions given the currently available data.

## See Also

### Presenting an alert
- [struct AlertScene](../alertscene.md)
  A scene that renders itself as a standalone alert dialog.
- [func alert(_:isPresented:actions:)](./alert%28_,ispresented,actions%29.md)
  Presents an alert when a given condition is true, using a localized string resource for the title.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:presenting:actions:))*