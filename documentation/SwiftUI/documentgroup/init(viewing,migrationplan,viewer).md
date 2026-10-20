# init(viewing:migrationPlan:viewer:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Instantiates a document group for viewing documents described by the last `Schema` in the migration plan.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
nonisolated
init(viewing contentType: UTType, migrationPlan: any SchemaMigrationPlan.Type, viewer: @escaping () -> Content)
```

Available when `Document` is `ModelDocument` and `Content` conforms to `View`.

## Parameters

- `viewing`: The content type of the document. It should conform to `UTType.package`.
- `migrationPlan`: The description of steps required to migrate older document versions so that they can be opened. The last `VersionedSchema` in the plan is considered to be the current application schema.
- `viewer`: The viewing UI for the provided document.

## See Also

### Viewing a document backed by a persistent store
- [init(viewing:contentType:viewer:)](./init%28viewing,contenttype,viewer%29.md)
  Instantiates a document group for viewing documents that store a specific model type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(viewing:migrationplan:viewer:))*