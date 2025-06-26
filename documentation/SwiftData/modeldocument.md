# ModelDocument

**Framework**: SwiftData  
**Kind**: struct

A document type that uses SwiftData to manage its storage.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct ModelDocument
```

#### Overview

> ❗ **Important**: Don’t create instances of this type. Instead, use one of the initializers on [`DocumentGroup`](https://developer.apple.com/documentation/SwiftUI/DocumentGroup).

## See Also

- [Maintaining a local copy of server data](maintaining-a-local-copy-of-server-data.md)
  Create and update a persistent store to cache read-only network data.
- [class DefaultStore](defaultstore.md)
  A data store that uses Core Data as its undelying storage mechanism.
- [protocol DataStore](datastore.md)
  An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism.
- [protocol DataStoreBatching](datastorebatching.md)
  An interface that enables a custom data store to support batch requests.
- [protocol HistoryProviding](historyproviding.md)
  An interface that enables a custom data store to provide the history of changes for its persisted models.
- [Building a document-based app using SwiftData](../SwiftUI/Building-a-document-based-app-using-SwiftData.md)
  Code along with the WWDC presenter to transform an app with SwiftData.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modeldocument)*