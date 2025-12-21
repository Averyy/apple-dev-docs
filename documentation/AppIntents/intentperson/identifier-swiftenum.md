# IntentPerson.Identifier

**Framework**: App Intents  
**Kind**: enum

A type that manages a unique identifier for a person.

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
enum Identifier
```

## Topics

### Getting the identifier types
- [IntentPerson.Identifier.contact(_:)](intentperson/identifier-swift.enum/contact(_:).md)
  An identifier from the Contacts framework (see `CNContact.identifier`)
- [IntentPerson.Identifier.applicationDefined(_:)](intentperson/identifier-swift.enum/applicationdefined(_:).md)
  An identifier specific to your app
### Enumeration Cases
- [IntentPerson.Identifier.unknown](intentperson/identifier-swift.enum/unknown.md)
  Unknown identifier, as in the case where the `IntentPerson` simply wraps a `Handle`.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var identifier: IntentPerson.Identifier](intentperson/identifier-swift.property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/identifier-swift.enum)*