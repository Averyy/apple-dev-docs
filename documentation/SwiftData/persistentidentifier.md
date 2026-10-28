# PersistentIdentifier

**Framework**: SwiftData  
**Kind**: struct  
**Role**: Structure

A type that describes the aggregate identity of a SwiftData model.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct PersistentIdentifier
```

## Overview

> **Note**: Decoded [`PersistentIdentifier`](./persistentidentifier.md) and identifiers created by the [`DefaultStore`](./defaultstore.md) are not considered equivalent.

## Topics

### Accessing identity information
- [let id: PersistentIdentifier.ID](./persistentidentifier/id-swift.property.md)
  The value that uniquely identifies the associated model within the containing store.
- [PersistentIdentifier.ID](./persistentidentifier/id-swift.struct.md)
  A type that represents the stable identity of a SwiftData model.
- [var storeIdentifier: String?](./persistentidentifier/storeidentifier.md)
  The identifier of the store that contains the associated model.
- [var entityName: String](./persistentidentifier/entityname.md)
  The entity name for the associated model.
### Instance Properties
- [var isTemporary: Bool](./persistentidentifier/istemporary.md)
  A Boolean value that indicates whether the identifier is temporary.
### Type Methods
- [static func identifier<T>(for: String, entityName: String, primaryKey: T) throws -> PersistentIdentifier](./persistentidentifier/identifier%28for,entityname,primarykey%29.md)

## Relationships

### Conforms To
- [Comparable](../Swift/comparable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Identifying the model instance
- [var persistentModelID: PersistentIdentifier](./persistentmodel/persistentmodelid.md)
- [var modelContext: ModelContext?](./persistentmodel/modelcontext.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/persistentidentifier)*