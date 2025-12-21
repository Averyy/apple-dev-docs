# DefaultStore

**Framework**: SwiftData  
**Kind**: class

A data store that uses Core Data as its undelying storage mechanism.

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
final class DefaultStore
```

## Topics

### Accessing store information
- [let name: String](defaultstore/name.md)
### Processing fetch requests
- [struct DefaultSnapshot](defaultsnapshot.md)
### Managing model change history
- [DefaultStore.TokenType](defaultstore/tokentype.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [DataStore](datastore.md)
- [DataStoreBatching](datastorebatching.md)
- [HistoryProviding](historyproviding.md)

## See Also

- [Maintaining a local copy of server data](maintaining-a-local-copy-of-server-data.md)
  Create and update a persistent store to cache read-only network data.
- [protocol DataStore](datastore.md)
  An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism.
- [protocol DataStoreBatching](datastorebatching.md)
  An interface that enables a custom data store to support batch requests.
- [protocol HistoryProviding](historyproviding.md)
  An interface that enables a custom data store to provide the history of changes for its persisted models.
- [Building a document-based app using SwiftData](../SwiftUI/Building-a-document-based-app-using-SwiftData.md)
  Code along with the WWDC presenter to transform an app with SwiftData.
- [struct ModelDocument](modeldocument.md)
  A document type that uses SwiftData to manage its storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/defaultstore)*