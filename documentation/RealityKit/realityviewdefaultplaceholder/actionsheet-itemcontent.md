# actionSheet(item:content:)

**Framework**: RealityKit  
**Kind**: method

Presents an action sheet using the given item as a data source for the sheet’s content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func actionSheet<T>(item: Binding<T?>, content: (T) -> ActionSheet) -> some View where T : Identifiable
```

#### Discussion

Use this method when you need to populate the fields of an action sheet with content from a data source. The example below shows a custom data source, `FileDetails`, that provides data to populate the action sheet:

```None
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

## Parameters

- `item`: A binding to an optional source of truth for the action   sheet. When   is non- , the system passes   the contents to the modifier’s closure. You use this content   to populate the fields of an action sheet that you create that the   system displays to the user. If   changes, the system   dismisses the currently displayed action sheet and replaces it   with a new one using the same process.
- `content`: A closure returning the   you create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/actionsheet(item:content:))*