# confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)

**Framework**: DeviceActivity  
**Kind**: method

Presents a confirmation dialog using data to produce the dialog’s content and a string variable for the title.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func confirmationDialog<S, A, T>(_ title: S, isPresented: Binding<Bool>, titleVisibility: Visibility = .automatic, presenting data: T?, @ViewBuilder actions: (T) -> A) -> some View where S : StringProtocol, A : View
```

#### Discussion

In order for the interface to appear, both `isPresented` must be `true` and `data` must not be `nil`. `data` should not change after the presentation occurs. Any changes which occur after the presentation occurs will be ignored.

Use this method when you need to populate the fields of a confirmation dialog with content from a data source. The example below shows a custom data source, `FileDetails`, that provides data to populate the dialog:

```swift
struct FileDetails: Identifiable {
    var id: String { name }
    let name: String
    let fileType: UTType
}
struct ConfirmFileImport: View {
    var title: String
    @State private var isConfirming = false
    @State private var dialogDetail: FileDetails?
    var body: some View {
        Button("Import File") {
            dialogDetail = FileDetails(
                name: "MyImageFile.png", fileType: .png)
            isConfirming = true
        }
        .confirmationDialog(
            title, isPresented: $isConfirming,
            presenting: dialogDetail
        ) { detail in
            Button {
                // Handle import action.
            } label: {
                Text("""
                Import \(detail.name)
                File Type: \(detail.fileType.description)
                """)
            }
            Button("Cancel", role: .cancel) {
                dialogDetail = nil
            }
        }
    }
}
```

All actions in a confirmation dialog will dismiss the dialog after the action runs. The default button will be shown with greater prominence. You can influence the default button by assigning it the `KeyboardShortcut/defaultAction` keyboard shortcut.

The system may reorder the buttons based on their role and prominence.

Dialogs include a standard dismiss action by default. If you provide a button with a role of `ButtonRole/cancel`, that button takes the place of the default dismiss action. You don’t have to dismiss the presentation with the cancel button’s action.

> **Note**: In regular size classes in iOS, the system renders confirmation dialogs as a popover that the user dismisses by tapping anywhere outside the popover, rather than displaying the standard dismiss action.

In regular size classes in iOS, the system renders confirmation dialogs as a popover that the user dismisses by tapping anywhere outside the popover, rather than displaying the standard dismiss action.

On iOS, tvOS, and watchOS, confirmation dialogs only support controls with labels that are `Text`. Passing any other type of view results in the content being omitted.

## Parameters

- `title`: A text string used as the title of the dialog.
- `isPresented`: A binding to a Boolean value that determines whether   to present the dialog. When the user presses or taps the dialog’s   default action button, the system sets this value to  ,   dismissing the dialog.
- `titleVisibility`: The visibility of the dialog’s title. The default   value is  .
- `data`: An optional source of truth for the confirmation dialog. The   system passes the contents to the modifier’s closures. You use this   data to populate the fields of a confirmation dialog that you create   that the system displays to the user.
- `actions`: A view builder returning the dialog’s actions given the   currently available data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:)-7kaoz)*