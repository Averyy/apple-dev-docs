# alert(_:isPresented:presenting:actions:message:)

**Framework**: FamilyControls  
**Kind**: method

Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func alert<A, M, T>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, presenting data: T?, @ViewBuilder actions: (T) -> A, @ViewBuilder message: (T) -> M) -> some View where A : View, M : View
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
        } message: { details in
            Text(details.error)
        }
    }
}
```

This modifier creates a `Text` view for the title on your behalf. See `Text` for more information about localizing strings.

All actions in an alert dismiss the alert after the action runs. The default button is shown with greater prominence.  You can influence the default button by assigning it the `KeyboardShortcut/defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

If no actions are present, the system includes a standard “OK” action. No default cancel action is provided. If you want to show a cancel action, use a button with a role of `ButtonRole/cancel`.

On iOS, tvOS, and watchOS, alerts only support controls with labels that are `Text`. Passing any other type of view results in the content being omitted.

Only unstyled text is supported for the message.

## Parameters

- `titleResource`: Text resource for the localized string that describes   the title.
- `isPresented`: A binding to a Boolean value that determines whether to   present the alert. When the user presses or taps one of the alert’s   actions, the system sets this value to   and dismisses.
- `data`: An optional source of truth for the alert. The system passes   the contents to the modifier’s closures. You use this data to   populate the fields of an alert that you create that the system   displays to the user.
- `actions`: A   returning the alert’s actions given the   currently available data.
- `message`: A   returning the message for the alert given   the currently available data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/alert(_:ispresented:presenting:actions:message:)-5rpk5)*