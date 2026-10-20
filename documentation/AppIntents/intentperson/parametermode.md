# IntentPerson.ParameterMode

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

The type of interface to show when someone chooses a parameter that contains information about a person.

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
enum ParameterMode
```

## Topics

### Getting the interface type
- [IntentPerson.ParameterMode.contact](./parametermode/contact.md)
  The parameter shows an interface allowing the user to pick a contact
- [IntentPerson.ParameterMode.email](./parametermode/email.md)
  The parameter shows an interface allowing the user to pick an email
- [IntentPerson.ParameterMode.emailOrPhone](./parametermode/emailorphone.md)
  The parameter shows an interface allowing the user to pick an email or phone number
- [IntentPerson.ParameterMode.phone](./parametermode/phone.md)
  The parameter shows an interface allowing the user to pick a phone number

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Getting identifying information
- [var handle: IntentPerson.Handle?](./handle-swift.property.md)
  The primary `Handle` used to contact this `IntentPerson`
- [var aliases: [IntentPerson.Handle]](./aliases.md)
  Other secondary `Handle`s used to contact this `IntentPerson`, if any
- [var isMe: Bool](./isme.md)
  Whether this `IntentPerson` represents the owner of the device
- [var image: DisplayRepresentation.Image?](./image.md)
  An image representing this `IntentPerson`
- [IntentPerson.Handle](./handle-swift.struct.md)
  A type that describes a single way to contact a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/parametermode)*