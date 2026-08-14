# IntentPerson.Name

**Framework**: App Intents  
**Kind**: enum

A type that stores name-related information for a person.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
enum Name
```

## Topics

### Getting a displayable name
- [IntentPerson.Name.displayName(_:)](intentperson/name-swift.enum/displayname(_:).md)
  The user-visible display name of this `IntentPerson`.
### Getting the name components
- [case components(PersonNameComponents)](intentperson/name-swift.enum/components(_:).md)
  Structured components of this `IntentPerson`’s name
### Enumeration Cases
- [IntentPerson.Name.unknown](intentperson/name-swift.enum/unknown.md)
  Unknown name, as in the case where the `IntentPerson` simply wraps a `Handle`.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var name: IntentPerson.Name](intentperson/name-swift.property.md)
  The name of this `IntentPerson`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/name-swift.enum)*