# IntentPerson.Handle

**Framework**: App Intents  
**Kind**: struct

A type that describes a single way to contact a person.

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
struct Handle
```

## Topics

### Getting the handle label
- [IntentPerson.Handle.Label](intentperson/handle-swift.struct/label-swift.enum.md)
  A location description that applies to the handle’s content, for example a work or home phone number.
### Operators
- [static func == (IntentPerson.Handle, IntentPerson.Handle) -> Bool](intentperson/handle-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(IntentPerson.Handle.Value, label: IntentPerson.Handle.Label)](intentperson/handle-swift.struct/init(_:label:).md)
- [init(applicationDefined: String, label: String?)](intentperson/handle-swift.struct/init(applicationdefined:label:).md)
- [init(emailAddress: String, label: IntentPerson.Handle.Label)](intentperson/handle-swift.struct/init(emailaddress:label:).md)
- [init(phoneNumber: String, label: IntentPerson.Handle.Label)](intentperson/handle-swift.struct/init(phonenumber:label:).md)
### Instance Properties
- [var hashValue: Int](intentperson/handle-swift.struct/hashvalue.md)
  The hash value.
- [var label: IntentPerson.Handle.Label](intentperson/handle-swift.struct/label-swift.property.md)
- [var value: IntentPerson.Handle.Value](intentperson/handle-swift.struct/value-swift.property.md)
  The string value for this `Handle`, such as the specific phone number or email address
### Instance Methods
- [func hash(into: inout Hasher)](intentperson/handle-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Enumerations
- [IntentPerson.Handle.Value](intentperson/handle-swift.struct/value-swift.enum.md)
  A type that describes the type of contact information in the handle, such as whether it is an email address, or a phone number.
### Default Implementations
- [Decodable Implementations](intentperson/handle-swift.struct/decodable-implementations.md)
- [Encodable Implementations](intentperson/handle-swift.struct/encodable-implementations.md)
- [Equatable Implementations](intentperson/handle-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var handle: IntentPerson.Handle?](intentperson/handle-swift.property.md)
  The primary `Handle` used to contact this `IntentPerson`
- [var aliases: [IntentPerson.Handle]](intentperson/aliases.md)
  Other secondary `Handle`s used to contact this `IntentPerson`, if any
- [var isMe: Bool](intentperson/isme.md)
  Whether this `IntentPerson` represents the owner of the device
- [var image: DisplayRepresentation.Image?](intentperson/image.md)
  An image representing this `IntentPerson`
- [IntentPerson.ParameterMode](intentperson/parametermode.md)
  The type of interface to show when someone chooses a parameter that contains information about a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/handle-swift.struct)*