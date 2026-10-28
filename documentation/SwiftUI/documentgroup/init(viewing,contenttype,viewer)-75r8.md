# init(viewing:contentType:viewer:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Instantiates a document group for viewing documents that store several model types.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
init(viewing modelTypes: [any PersistentModel.Type], contentType: UTType, viewer: @escaping () -> Content)
```

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(viewing modelType: any PersistentModel.Type, contentType: UTType, viewer: @escaping () -> Content)
```

## Discussion

```swift
 @main
 struct Todo: App {
     var body: some Scene {
         DocumentGroup(viewing: [TodoItem.self, CalendarEvent.self], contentType: .tasks) {
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
                     Image(systemName: item.isDone ? "checkmark.square" : "square")
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

> ❗ **Important**: If your app declares custom uniform type identifiers, include corresponding entries in the app’s `Info.plist`. For more information, see [Defining file and data types for your app](../../UniformTypeIdentifiers/defining-file-and-data-types-for-your-app.md). Also, remember to specify the supported Document types in the `Info.plist` as well.

## Parameters

- `modelTypes`: The model types defining the schema used for each document.
- `contentType`: The content type of document your app can view. It should conform to `UTType.package`.
- `viewer`: The viewing UI for the provided document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(viewing:contenttype:viewer:)-75r8)*