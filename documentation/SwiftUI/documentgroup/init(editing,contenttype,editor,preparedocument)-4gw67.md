# init(editing:contentType:editor:prepareDocument:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Instantiates a document group for creating and editing documents that store several model types.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
init(editing modelTypes: [any PersistentModel.Type], contentType: UTType, editor: @escaping () -> Content, prepareDocument: @escaping (ModelContext) -> Void = { _ in })
```

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(editing modelType: any PersistentModel.Type, contentType: UTType, editor: @escaping () -> Content, prepareDocument: @escaping (ModelContext) -> Void = { _ in })
```

## Discussion

```swift
 @main
 struct Todo: App {
     var body: some Scene {
         DocumentGroup(editing: [TodoItem.self, CalendarEvent.self], contentType: .tasks) {
             ContentView()
         }
     }
 }

 struct ContentView: View {
     @Query var items: [TodoItem]
     @Query var events: [CalendarEvent]

     var body: some View {
         Form {
             Section("Todo") {
                 ForEach(items) { item in
                     @Bindable var item = item
                     Toggle(item.text, isOn: $item.isDone)
                 }
             }
             Section("Events") {
                 ForEach(events) { event in
                     LabeledContent(event.title, value: event.date.formatted())
                  }
              }
         }
         .formStyle(.grouped)
         .padding()
     }
 }

 @Model
 final class TodoItem {
     var created: Date
     var text: String
     var isDone = false
 }

 @Model
 final class CalendarEvent {
     var title: String
     var date: Date
}


 extension UTType {
     static var tasks = UTType(exportedAs: "com.myApp.tasks")
 }
```

> ❗ **Important**: If your app declares custom uniform type identifiers, include corresponding entries in the app’s `Info.plist`. For more information, see [Defining file and data types for your app](../../UniformTypeIdentifiers/defining-file-and-data-types-for-your-app.md). Also, remember to specify the supported Document types in the Info.plist as well.

## Parameters

- `modelTypes`: The array of model types defining the schema used for each document.
- `contentType`: The content type of the document. It should conform to `UTType.package`.
- `editor`: The editing UI for the provided document.
- `prepareDocument`: The optional closure that accepts `ModelContext` associated with the new document. Use this closure to set the document’s initial contents before it is displayed: insert preconfigured models in the provided `ModelContext`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(editing:contenttype:editor:preparedocument:)-4gw67)*