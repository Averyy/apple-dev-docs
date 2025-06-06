# IntentPerson.Identifier

**Framework**: App Intents  
**Kind**: enum

A type that manages a unique identifier for a person.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
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
### Operators
- [static func == (IntentPerson.Identifier, IntentPerson.Identifier) -> Bool](intentperson/identifier-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [IntentPerson.Identifier.unknown](intentperson/identifier-swift.enum/unknown.md)
  Unknown identifier, as in the case where the `IntentPerson` simply wraps a `Handle`.
### Instance Properties
- [var hashValue: Int](intentperson/identifier-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intentperson/identifier-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Decodable Implementations](intentperson/identifier-swift.enum/decodable-implementations.md)
- [Encodable Implementations](intentperson/identifier-swift.enum/encodable-implementations.md)
- [Equatable Implementations](intentperson/identifier-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var identifier: IntentPerson.Identifier](intentperson/identifier-swift.property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/identifier-swift.enum)*