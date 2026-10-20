# IntentPerson.Identifier

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

A type that manages a unique identifier for a person.

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
enum Identifier
```

## Topics

### Getting the identifier types
- [IntentPerson.Identifier.contact(_:)](./identifier-swift.enum/contact%28_%29.md)
  An identifier from the Contacts framework (see `CNContact.identifier`)
- [IntentPerson.Identifier.applicationDefined(_:)](./identifier-swift.enum/applicationdefined%28_%29.md)
  An identifier specific to your app
### Enumeration Cases
- [IntentPerson.Identifier.unknown](./identifier-swift.enum/unknown.md)
  Unknown identifier, as in the case where the `IntentPerson` simply wraps a `Handle`.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting person-related identifiers
- [var identifier: IntentPerson.Identifier](./identifier-swift.property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/identifier-swift.enum)*