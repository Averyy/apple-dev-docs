# HistoryProviding

**Framework**: SwiftData  
**Kind**: protocol

An interface that enables a custom data store to provide the history of changes for its persisted models.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+
- Swift 5.9+

## Declaration

```swift
protocol HistoryProviding
```

## Topics

### Processing history fetch requests
- [func fetchHistory(HistoryDescriptor<Self.HistoryType>) throws -> [Self.HistoryType]](historyproviding/fetchhistory(_:).md)
### Deleting history
- [func deleteHistory(HistoryDescriptor<Self.HistoryType>) throws](historyproviding/deletehistory(_:).md)
### Getting the history transaction type
- [associatedtype HistoryType : HistoryTransaction](historyproviding/historytype-swift.associatedtype.md)
### Type Properties
- [static var historyType: Self.HistoryType.Type](historyproviding/historytype-swift.type.property.md)

## Relationships

### Conforming Types
- [DefaultStore](defaultstore.md)

## See Also

- [Maintaining a local copy of server data](maintaining-a-local-copy-of-server-data.md)
  Create and update a persistent store to cache read-only network data.
- [class DefaultStore](defaultstore.md)
  A data store that uses Core Data as its undelying storage mechanism.
- [protocol DataStore](datastore.md)
  An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism.
- [protocol DataStoreBatching](datastorebatching.md)
  An interface that enables a custom data store to support batch requests.
- [Building a document-based app using SwiftData](../SwiftUI/Building-a-document-based-app-using-SwiftData.md)
  Code along with the WWDC presenter to transform an app with SwiftData.
- [struct ModelDocument](modeldocument.md)
  A document type that uses SwiftData to manage its storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/historyproviding)*