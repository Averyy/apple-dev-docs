# actionSheet(item:content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents an action sheet using the given item as a data source for the sheet’s content.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- tvOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 6.0+ - Deprecated in 27.2

> **Deprecated**: Use [`confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)`](./confirmationdialog%28_,ispresented,titlevisibility,presenting,actions,message%29-8y541.md) instead.

## Declaration

```swift
nonisolated
func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View where T : Identifiable
```

## Discussion

Use this method when you need to populate the fields of an action sheet with content from a data source. The example below shows a custom data source, `FileDetails`, that provides data to populate the action sheet:

```swift
struct FileDetails: Identifiable {
    var id: String { name }
    let name: String
    let fileType: UTType
}
struct ConfirmFileImport: View {
    @State private var sheetDetail: FileDetails?
    var body: some View {
        Button("Show Action Sheet") {
            sheetDetail = FileDetails(name: "MyImageFile.png",
                                      fileType: .png)
        }
        .actionSheet(item: $sheetDetail) { detail in
            ActionSheet(
                title: Text("File Import"),
                message: Text("""
                         Import \(detail.name)?
                         File Type: \(detail.fileType.description)
                         """),
                buttons: [
                    .destructive(Text("Import"),
                                 action: importFile),
                    .cancel()
                ])
        }
    }

    func importFile() {
        // Handle import action.
    }
}
```

![A screenshot showing an action sheet populated using a custom data source that describes a file and file format.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SwiftUI-View-ActionSheetItemContent@2x.png)

## Parameters

- `item`: A binding to an optional source of truth for the action sheet. When `item` is non-`nil`, the system passes the contents to the modifier’s closure. You use this content to populate the fields of an action sheet that you create that the system displays to the user. If `item` changes, the system dismisses the currently displayed action sheet and replaces it with a new one using the same process.
- `content`: A closure returning the [`ActionSheet`](../actionsheet.md) you create.

## See Also

### View presentation modifiers
- [func actionSheet(isPresented: Binding<Bool>, content: () -> ActionSheet) -> some View](./actionsheet%28ispresented,content%29.md)
  Presents an action sheet when a given condition is true.
- [func alert(isPresented: Binding<Bool>, content: () -> Alert) -> some View](./alert%28ispresented,content%29.md)
  Presents an alert to the user.
- [func alert<Item>(item: Binding<Item?>, content: (Item) -> Alert) -> some View](./alert%28item,content%29.md)
  Presents an alert to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/actionsheet(item:content:))*