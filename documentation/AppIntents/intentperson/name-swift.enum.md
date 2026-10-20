# IntentPerson.Name

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

A type that stores name-related information for a person.

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
enum Name
```

## Topics

### Getting a displayable name
- [IntentPerson.Name.displayName(_:)](./name-swift.enum/displayname%28_%29.md)
  The user-visible display name of this `IntentPerson`.
### Getting the name components
- [case components(PersonNameComponents)](./name-swift.enum/components%28_%29.md)
  Structured components of this `IntentPerson`’s name
### Enumeration Cases
- [IntentPerson.Name.unknown](./name-swift.enum/unknown.md)
  Unknown name, as in the case where the `IntentPerson` simply wraps a `Handle`.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the person’s name
- [var name: IntentPerson.Name](./name-swift.property.md)
  The name of this `IntentPerson`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/name-swift.enum)*