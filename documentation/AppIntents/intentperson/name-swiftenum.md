# IntentPerson.Name

**Framework**: App Intents  
**Kind**: enum

A type that stores name-related information for a person.

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
enum Name
```

## Topics

### Getting a displayable name
- [IntentPerson.Name.displayName(_:)](intentperson/name-swift.enum/displayname(_:).md)
  The user-visible display name of this `IntentPerson`.
### Getting the name components
- [case components(PersonNameComponents)](intentperson/name-swift.enum/components(_:).md)
  Structured components of this `IntentPerson`’s name
### Operators
- [static func == (IntentPerson.Name, IntentPerson.Name) -> Bool](intentperson/name-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [IntentPerson.Name.unknown](intentperson/name-swift.enum/unknown.md)
  Unknown name, as in the case where the `IntentPerson` simply wraps a `Handle`.
### Default Implementations
- [Decodable Implementations](intentperson/name-swift.enum/decodable-implementations.md)
- [Encodable Implementations](intentperson/name-swift.enum/encodable-implementations.md)
- [Equatable Implementations](intentperson/name-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var name: IntentPerson.Name](intentperson/name-swift.property.md)
  The name of this `IntentPerson`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/name-swift.enum)*