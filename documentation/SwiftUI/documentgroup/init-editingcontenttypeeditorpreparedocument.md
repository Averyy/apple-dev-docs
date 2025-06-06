# init(editing:contentType:editor:prepareDocument:)

**Framework**: SwiftUI  
**Kind**: init

Instantiates a document group for creating and editing documents that store a specific model type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

## Declaration

```swift
init(editing modelType: any PersistentModel.Type, contentType: UTType, editor: @escaping () -> Content, prepareDocument: @escaping (ModelContext) -> Void = { _ in })
```

#### Discussion

```swift
 @main
 struct Todo: App {
     var body: some Scene {
         DocumentGroup(editing: TodoItem.self, contentType: .todoItem) {
             ContentView()
         }
     }
 }

 struct ContentView: View {
     @Query var items: [TodoItem]

         var body: some View {
             List {
                 ForEach(items) { item in
                     @Bindable var item = item
                     Toggle(item.text, isOn: $item.isDone)
                 }
              }
         }
 }

 @Model
 final class TodoItem {
     var created: Date
     var text: String
     var isDone = false
 }

 extension UTType {
     static var todoItem = UTType(exportedAs: "com.myApp.todoItem")
 }
```

> ❗ **Important**: If your app declares custom uniform type identifiers, include corresponding entries in the app’s `Info.plist`. For more information, see [`Defining file and data types for your app`](https://developer.apple.com/documentation/UniformTypeIdentifiers/defining-file-and-data-types-for-your-app). Also, remember to specify the supported Document types in the Info.plist as well.

If your app declares custom uniform type identifiers, include corresponding entries in the app’s `Info.plist`. For more information, see [`Defining file and data types for your app`](https://developer.apple.com/documentation/UniformTypeIdentifiers/defining-file-and-data-types-for-your-app). Also, remember to specify the supported Document types in the Info.plist as well.

## Parameters

- `modelType`: The model type defining the schema used for each document.
- `contentType`: The content type of the document.   It should conform to  .
- `editor`: The editing UI for the provided document.
- `prepareDocument`: The optional closure that accepts    associated with the new document.   Use this closure to set the document’s initial contents   before it is displayed: insert preconfigured models   in the provided  .

## See Also

- [init(editing: UTType, migrationPlan: any SchemaMigrationPlan.Type, editor: () -> Content, prepareDocument: (ModelContext) -> Void)](documentgroup/init(editing:migrationplan:editor:preparedocument:).md)
  Instantiates a document group for creating and editing documents described by the last `Schema` in the migration plan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(editing:contenttype:editor:preparedocument:))*