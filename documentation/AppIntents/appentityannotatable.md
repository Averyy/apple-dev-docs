# AppEntityAnnotatable

**Framework**: App Intents  
**Kind**: protocol

An interface that system types adopt and use to manage their relationship to app entities.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
protocol AppEntityAnnotatable
```

## Mentions

- [Providing contextual cues to Apple Intelligence and Siri](providing-contextual-cues-to-apple-intelligence-and-siri.md)

#### Overview

System types adopt the `AppEntityAnnotatable` protocol and use it to store a reference to an app entity. Don’t add support for this protocol to your own custom types. Instead, the system incorporates it into types like [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) to support your custom entities. The system types use the presence of an entity to improve system experiences like Apple Intelligence, Siri, and Shortcuts.

## Topics

### Instance Properties
- [var appEntityIdentifier: EntityIdentifier?](appentityannotatable/appentityidentifier.md)
  The identifier of an app entity you want to associate with a system type.

## Relationships

### Conforming Types
- [ShortcutsUIButton](shortcutsuibutton.md)
- [SiriTipUIView](siritipuiview.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentityannotatable)*