# alert(item:content:)

**Framework**: FamilyControls  
**Kind**: method

Presents an alert to the user.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some View where Item : Identifiable
```

#### Discussion

Use this method when you need to show an alert that contains information from a binding to an optional data source that you provide. The example below shows a custom data source `FileInfo` whose properties configure the alert’s `message` field:

```swift
struct FileInfo: Identifiable {
    var id: String { name }
    let name: String
    let fileType: UTType
}

struct ConfirmImportAlert: View {
    @State private var alertDetails: FileInfo?
    var body: some View {
        Button("Show Alert") {
            alertDetails = FileInfo(name: "MyImageFile.png",
                                    fileType: .png)
        }
        .alert(item: $alertDetails) { details in
            Alert(title: Text("Import Complete"),
                  message: Text("""
                    Imported \(details.name) \n File
                    type: \(details.fileType.description).
                    """),
                  dismissButton: .default(Text("Dismiss")))
        }
    }
}
```

## Parameters

- `item`: A binding to an optional source of truth for the alert.   if   is non- , the system passes the contents to   the modifier’s closure. You use this content to populate the fields   of an alert that you create that the system displays to the user.   If   changes, the system dismisses the currently displayed   alert and replaces it with a new one using the same process.
- `content`: A closure returning the alert to present.

## See Also

- [func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) -> some View](familyactivitypicker/actionsheet(ispresented:content:).md)
  Presents an action sheet when a given condition is true.
- [func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View](familyactivitypicker/actionsheet(item:content:).md)
  Presents an action sheet using the given item as a data source for the sheet’s content.
- [func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View](familyactivitypicker/alert(ispresented:content:).md)
  Presents an alert to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/alert(item:content:))*