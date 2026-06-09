# AppEntityIdentifier

**Framework**: App Intents  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct AppEntityIdentifier
```

## Topics

### Initializers
- [init(entityType: AttributedTypeIdentifier, instanceIdentifier: String)](appentityidentifier/init(entitytype:instanceidentifier:).md)
  Creates an attributed entity identifier with the specified type and instance identifiers.
### Instance Properties
- [let entityType: AttributedTypeIdentifier](appentityidentifier/entitytype.md)
  The type identifier that defines what kind of entity this is.
- [let instanceIdentifier: String](appentityidentifier/instanceidentifier.md)
  The string that uniquely identifies this specific entity instance.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct EntityIdentifier](entityidentifier.md)
  A type that uniquely identifies a specific instance of an app entity.
- [protocol EntityIdentifierConvertible](entityidentifierconvertible.md)
  An interface for converting between an entity’s identifier and its string representation.
- [struct FileEntityIdentifier](fileentityidentifier.md)
  An identifier for an app entity that refers to a document or other file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentityidentifier)*