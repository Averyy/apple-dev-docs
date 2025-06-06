# confirmationDialog(_:isPresented:titleVisibility:actions:message:)

**Framework**: Appintents  
**Kind**: method

Presents a confirmation dialog with a message when a given condition is true, using a string variable for the title.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func confirmationDialog<S, A, M>(_ title: S, isPresented: Binding<Bool>, titleVisibility: Visibility = .automatic, @ViewBuilder actions: () -> A, @ViewBuilder message: () -> M) -> some View where S : StringProtocol, A : View, M : View
```

#### Discussion

In the example below, a button conditionally presents a confirmation dialog depending upon the value of a bound Boolean variable. When the Boolean value is set to `true`, the system displays a confirmation dialog with a cancel action and a destructive action.

```swift
struct ConfirmEraseItems: View {
    @State private var isShowingDialog = false
    var title: String
    var body: some View {
        Button("Empty Trash") {
            isShowingDialog = true
        }
        .confirmationDialog(
            title,
            isPresented: $isShowingDialog
        ) {
            Button("Empty Trash", role: .destructive) {
                // Handle empty trash action.
            }
            Button("Cancel", role: .cancel) {
                isShowingDialog = false
            }
        } message: {
            Text("You cannot undo this action.")
        }
    }
}
```

All actions in a confirmation dialog will dismiss the dialog after the action runs. The default button will be shown with greater prominence. You can influence the default button by assigning it the `KeyboardShortcut/defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button with a role of `ButtonRole/cancel`, that button takes the place of the default dismiss action. You don’t have to dismiss the presentation with the cancel button’s action.

> **Note**: In regular size classes in iOS, the system renders confirmation dialogs as a popover that the user dismisses by tapping anywhere outside the popover, rather than displaying the standard dismiss action.

## Parameters

- `title`: A text string used as the title of the dialog.
- `isPresented`: A binding to a Boolean value that determines whether to   present the dialog. When the user presses or taps the dialog’s   default action button, the system sets this value to  ,   dismissing the dialog.
- `titleVisibility`: The visibility of the dialog’s title. The default   value is  .
- `actions`: A view builder returning the dialog’s actions.
- `message`: A view builder returning the message for the dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/confirmationdialog(_:ispresented:titlevisibility:actions:message:)-6sbqa)*