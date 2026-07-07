# FileEntityIdentifier

**Framework**: App Intents  
**Kind**: struct

An identifier for an app entity that refers to a document or other file.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct FileEntityIdentifier
```

## Topics

### Instance Properties
- [var draftIdentifier: String?](fileentityidentifier/draftidentifier.md)
  The document draft identifier, if the document hasn’t been materialized on disk yet.
- [var fileURL: URL?](fileentityidentifier/fileurl.md)
  A URL that locates a file saved to disk.
- [var isDraft: Bool](fileentityidentifier/isdraft.md)
  Indicates whether this identifier represents a document draft.
### Type Methods
- [static func draft(identifier: String) -> FileEntityIdentifier](fileentityidentifier/draft(identifier:).md)
  Creates and returns an identifier for a draft document.
- [static func file(url: URL) throws -> FileEntityIdentifier](fileentityidentifier/file(url:).md)
  Creates and returns an identifier with the provided URL to the file on disk.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [EntityIdentifierConvertible](entityidentifierconvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct EntityIdentifier](entityidentifier.md)
  A type that uniquely identifies a specific instance of an app entity.
- [protocol EntityIdentifierConvertible](entityidentifierconvertible.md)
  An interface for converting between an entity’s identifier and its string representation.
- [protocol PersistentlyIdentifiable](persistentlyidentifiable.md)
  Defines a string that uniquely identifies a type. This is useful for maintaining the identity of a type, even when its type name is changed.
- [struct SyncableEntityIdentifier](syncableentityidentifier.md)
  A type-safe wrapper you use to specify different local and stable identifiers for an entity.
- [struct AttributedEntityIdentifier](attributedentityidentifier.md)
  A unique identifier for an app entity instance within an application.
- [struct AttributedTypeIdentifier](attributedtypeidentifier.md)
  A unique identifier for an app entity or transient app entity type within an application bundle.
- [protocol AppEntityAnnotatable](appentityannotatable.md)
  An interface that system types adopt and use to manage their relationship to app entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/fileentityidentifier)*