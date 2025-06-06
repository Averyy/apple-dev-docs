# IntentPerson.ParameterMode

**Framework**: App Intents  
**Kind**: enum

The type of interface to show when someone chooses a parameter that contains information about a person.

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
enum ParameterMode
```

## Topics

### Getting the interface type
- [IntentPerson.ParameterMode.contact](intentperson/parametermode/contact.md)
  The parameter shows an interface allowing the user to pick a contact
- [IntentPerson.ParameterMode.email](intentperson/parametermode/email.md)
  The parameter shows an interface allowing the user to pick an email
- [IntentPerson.ParameterMode.emailOrPhone](intentperson/parametermode/emailorphone.md)
  The parameter shows an interface allowing the user to pick an email or phone number
- [IntentPerson.ParameterMode.phone](intentperson/parametermode/phone.md)
  The parameter shows an interface allowing the user to pick a phone number
### Creating a parameter mode
- [init?(rawValue: String)](intentperson/parametermode/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](intentperson/parametermode/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [IntentPerson.ParameterMode.RawValue](intentperson/parametermode/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](intentperson/parametermode/equatable-implementations.md)
- [RawRepresentable Implementations](intentperson/parametermode/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [var handle: IntentPerson.Handle?](intentperson/handle-swift.property.md)
  The primary `Handle` used to contact this `IntentPerson`
- [var aliases: [IntentPerson.Handle]](intentperson/aliases.md)
  Other secondary `Handle`s used to contact this `IntentPerson`, if any
- [var isMe: Bool](intentperson/isme.md)
  Whether this `IntentPerson` represents the owner of the device
- [var image: DisplayRepresentation.Image?](intentperson/image.md)
  An image representing this `IntentPerson`
- [IntentPerson.Handle](intentperson/handle-swift.struct.md)
  A type that describes a single way to contact a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/parametermode)*