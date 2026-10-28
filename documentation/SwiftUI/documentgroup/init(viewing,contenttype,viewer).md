# init(viewing:contentType:viewer:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Instantiates a document group for viewing documents that store a specific model type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
init(viewing modelType: any PersistentModel.Type, contentType: UTType, viewer: @escaping () -> Content)
```

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(viewing modelTypes: [any PersistentModel.Type], contentType: UTType, viewer: @escaping () -> Content)
```

## Discussion

```swift
 @main
 struct Todo: App {
     var body: some Scene {
         DocumentGroup(viewing: TodoItem.self, contentType: .todoItem) {
             ContentView()
         }
     }
 }

 extension UTType {
     static var todoItem = UTType(exportedAs: "com.myApp.todoItem")
 }
```

> ❗ **Important**: If your app declares custom uniform type identifiers, include corresponding entries in the app’s `Info.plist`. For more information, see [Defining file and data types for your app](../../UniformTypeIdentifiers/defining-file-and-data-types-for-your-app.md). Also, remember to specify the supported Document types in the `Info.plist` as well.

## Parameters

- `modelType`: The model type defining the schema used for each document.
- `contentType`: The content type of document your app can view. It should conform to `UTType.package`.
- `viewer`: The viewing UI for the provided document.

## See Also

### Viewing a document backed by a persistent store
- [init(viewing: UTType, migrationPlan: any SchemaMigrationPlan.Type, viewer: () -> Content)](./init%28viewing,migrationplan,viewer%29.md)
  Instantiates a document group for viewing documents described by the last `Schema` in the migration plan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(viewing:contenttype:viewer:))*