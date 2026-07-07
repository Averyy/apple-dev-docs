# AttributedEntityIdentifier

**Framework**: App Intents  
**Kind**: struct

A unique identifier for an app entity instance within an application.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct AttributedEntityIdentifier
```

#### Overview

`AttributedEntityIdentifier` combines type and instance information to create a complete identifier that can uniquely identify any app entity instance. This identifier consists of two parts:

1. An entity type identifier that distinguishes different kinds of entities
2. An instance identifier that distinguishes individual instances of the same type

This structure enables the AppIntents framework to reference and retrieve specific entity instances across the system.

## Topics

### Initializers
- [init(entityType: AttributedTypeIdentifier, instanceIdentifier: String)](attributedentityidentifier/init(entitytype:instanceidentifier:).md)
  Creates an attributed entity identifier with the specified type and instance identifiers.
### Instance Properties
- [let entityType: AttributedTypeIdentifier](attributedentityidentifier/entitytype.md)
  The type identifier that defines what kind of entity this is.
- [let instanceIdentifier: String](attributedentityidentifier/instanceidentifier.md)
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
- [struct AttributedTypeIdentifier](attributedtypeidentifier.md)
  A unique identifier for an app entity or transient app entity type within an application bundle.
- [protocol AppEntityAnnotatable](appentityannotatable.md)
  An interface that system types adopt and use to manage their relationship to app entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/attributedentityidentifier)*