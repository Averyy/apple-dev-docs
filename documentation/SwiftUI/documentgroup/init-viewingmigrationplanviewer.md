# init(viewing:migrationPlan:viewer:)

**Framework**: SwiftUI  
**Kind**: init

Instantiates a document group for viewing documents described by the last `Schema` in the migration plan.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

## Declaration

```swift
init(viewing contentType: UTType, migrationPlan: any SchemaMigrationPlan.Type, viewer: @escaping () -> Content)
```

## Parameters

- `viewing`: The content type of the document. It should conform to  .
- `migrationPlan`: The description of steps required to migrate older document   versions so that they can be opened.   The last   in the plan is considered to be   the current application schema.
- `viewer`: The viewing UI for the provided document.

## See Also

- [init(viewing:contentType:viewer:)](documentgroup/init(viewing:contenttype:viewer:).md)
  Instantiates a document group for viewing documents that store a specific model type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/documentgroup/init(viewing:migrationplan:viewer:))*