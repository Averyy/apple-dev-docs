# EntityIdentifierConvertible

**Framework**: App Intents  
**Kind**: protocol

An interface for converting between an entity’s identifier and its string representation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol EntityIdentifierConvertible
```

## Mentions

- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)

#### Overview

Every entity provides a stable, unique identifier that the framework uses as a concrete reference to the entity while mediating between your app and other parts of the system. To enforce this requirement, the [`AppEntity`](appentity.md) protocol inherits the [`Identifiable`](https://developer.apple.com/documentation/Swift/Identifiable) protocol.

Wherever possible, use [`String`](https://developer.apple.com/documentation/Swift/String), [`Int`](https://developer.apple.com/documentation/Swift/Int), or [`UUID`](https://developer.apple.com/documentation/Foundation/UUID) for an identifier’s type. If you must use a different data type, use this protocol to extend that type and implement the required support. For example, an app that integrates with the [`MusicKit`](https://developer.apple.com/documentation/MusicKit) framework might use [`MusicItemID`](https://developer.apple.com/documentation/MusicKit/MusicItemID) as the type for an entity’s identifier.

```swift
extension MusicItemID: EntityIdentifierConvertible {
    public var entityIdentifierString: String {
        rawValue
    }

    public init?(entityIdentifierString: String) {
        self = MusicItemID(entityIdentifierString)
    }
}
```

> ❗ **Important**: Keep your [`entityIdentifierString`](entityidentifierconvertible/entityidentifierstring.md) to 4096 characters or fewer. Otherwise, the framework truncates the value, and you might not be able to convert the truncated value back to its originating type.

## Topics

### Creating an identifier string
- [static func entityIdentifier(for: String) -> Self?](entityidentifierconvertible/entityidentifier(for:).md)
  Identifiers should be able to initialize via a `String` format.
### Getting the identifier string
- [var entityIdentifierString: String](entityidentifierconvertible/entityidentifierstring.md)
  The `AppEntity`’s identifier value as a `String`.

## Relationships

### Conforming Types
- [FileEntityIdentifier](fileentityidentifier.md)

## See Also

- [protocol PersistentlyIdentifiable](persistentlyidentifiable.md)
  Defines a string that uniquely identifies a type. This is useful for maintaining the identity of a type, even when its type name is changed.
- [struct EntityIdentifier](entityidentifier.md)
  A type that uniquely identifies a specific instance of an app entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityidentifierconvertible)*