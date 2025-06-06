# init(editing:migrationPlan:editor:prepareDocument:)

**Framework**: SwiftUI  
**Kind**: init

Instantiates a document group for creating and editing documents described by the last `Schema` in the migration plan.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

## Declaration

```swift
init(editing contentType: UTType, migrationPlan: any SchemaMigrationPlan.Type, editor: @escaping () -> Content, prepareDocument: @escaping (ModelContext) -> Void = { _ in })
```

## Parameters

- `editing`: The content type of the document. It should conform to  .
- `migrationPlan`: The description of steps required to migrate older document   versions so that they can be opened and edited.   The last   in the plan is considered to be   the current application schema.
- `editor`: The editing UI for the provided document.

## See Also

- [init(editing:contentType:editor:prepareDocument:)](documentgroup/init(editing:contenttype:editor:preparedocument:).md)
  Instantiates a document group for creating and editing documents that store a specific model type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(editing:migrationplan:editor:preparedocument:))*