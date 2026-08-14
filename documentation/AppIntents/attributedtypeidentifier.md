# AttributedTypeIdentifier

**Framework**: App Intents  
**Kind**: struct

A unique identifier for an app entity or transient app entity type within an application bundle.

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
struct AttributedTypeIdentifier
```

#### Overview

Use `AttributedTypeIdentifier` to uniquely identify entity types across your application. This identifier combines a persistent identifier — typically the entity’s type name — with an optional bundle identifier to ensure uniqueness across different bundles.

The system uses these identifiers to track and reference entity types throughout the AppIntents framework, particularly when working with entity specifications, containers, and identifiers.

## Topics

### Initializers
- [init(persistentIdentifier: String, bundleIdentifier: String?)](attributedtypeidentifier/init(persistentidentifier:bundleidentifier:).md)
  Creates a new attributed type identifier.
### Instance Properties
- [let bundleIdentifier: String?](attributedtypeidentifier/bundleidentifier.md)
  The bundle identifier that contains this entity type.
- [let persistentIdentifier: String](attributedtypeidentifier/persistentidentifier.md)
  The persistent identifier for this entity type.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

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
- [protocol AppEntityAnnotatable](appentityannotatable.md)
  An interface that system types adopt and use to manage their relationship to app entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/attributedtypeidentifier)*