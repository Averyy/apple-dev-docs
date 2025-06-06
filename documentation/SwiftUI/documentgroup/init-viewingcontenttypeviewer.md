# init(viewing:contentType:viewer:)

**Framework**: SwiftUI  
**Kind**: init

Instantiates a document group for viewing documents that store a specific model type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

## Declaration

```swift
init(viewing modelType: any PersistentModel.Type, contentType: UTType, viewer: @escaping () -> Content)
```

#### Discussion

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

> ❗ **Important**: If your app declares custom uniform type identifiers, include corresponding entries in the app’s `Info.plist`. For more information, see [`Defining file and data types for your app`](https://developer.apple.com/documentation/UniformTypeIdentifiers/defining-file-and-data-types-for-your-app). Also, remember to specify the supported Document types in the `Info.plist` as well.

If your app declares custom uniform type identifiers, include corresponding entries in the app’s `Info.plist`. For more information, see [`Defining file and data types for your app`](https://developer.apple.com/documentation/UniformTypeIdentifiers/defining-file-and-data-types-for-your-app). Also, remember to specify the supported Document types in the `Info.plist` as well.

## Parameters

- `modelType`: The model type defining the schema used for each document.
- `contentType`: The content type of document your app can view.   It should conform to  .
- `viewer`: The viewing UI for the provided document.

## See Also

- [init(viewing: UTType, migrationPlan: any SchemaMigrationPlan.Type, viewer: () -> Content)](documentgroup/init(viewing:migrationplan:viewer:).md)
  Instantiates a document group for viewing documents described by the last `Schema` in the migration plan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(viewing:contenttype:viewer:))*