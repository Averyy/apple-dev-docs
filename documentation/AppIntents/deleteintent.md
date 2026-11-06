# DeleteIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

An app intent that deletes one or more entities.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
protocol DeleteIntent : SystemIntent
```

## Overview

Declare the entities to delete as the [`entities`](./deleteintent/entities.md) parameter, or, starting in the 27.3 releases, as [`target`](./deleteintent/target-1cesv.md) to use a set or an [`EntityCollection`](./entitycollection.md):

```swift
struct DeleteNotesIntent: DeleteIntent {
    static let title: LocalizedStringResource = "Delete Notes"

    @Parameter(title: "Notes")
    var entities: [NoteEntity]

    func perform() async throws -> some IntentResult {
        try await NoteStore.shared.delete(entities.map(\.id))
        return .result()
    }
}
```

## Topics

### Associated Types
- [associatedtype Entity : AppEntity](./deleteintent/entity.md)
  The type of the entities to delete.
- [associatedtype Target : AppEntityCollectionValue = [Self.Entity]](./deleteintent/target-swift.associatedtype.md)
  The type of [`target`](./deleteintent/target-1cesv.md): an array or set of entities, or an [`EntityCollection`](./entitycollection.md).
### Instance Properties
- [var entities: [Self.Entity]](./deleteintent/entities.md)
  The entities to delete.
- [var target: Self.Target](./deleteintent/target-1cesv.md)
  The entities to delete.

## Relationships

### Inherits From
- [AppIntent](./appintent.md)
- [PersistentlyIdentifiable](./persistentlyidentifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SystemIntent](./systemintent.md)

## See Also

### Common actions
- [protocol OpenIntent](./openintent.md)
  An app intent that opens and displays a specific item in your app’s interface.
- [struct OpenURLIntent](./openurlintent.md)
  An app intent that opens one of your universal links and displays its contents.
- [protocol SetValueIntent](./setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol DeprecatedAppIntent](./deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/deleteintent)*