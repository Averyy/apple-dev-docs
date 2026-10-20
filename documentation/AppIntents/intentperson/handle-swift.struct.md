# IntentPerson.Handle

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

A type that describes a single way to contact a person.

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
struct Handle
```

## Topics

### Creating a handle
- [init(emailAddress: String, label: IntentPerson.Handle.Label)](./handle-swift.struct/init%28emailaddress,label%29.md)
- [init(phoneNumber: String, label: IntentPerson.Handle.Label)](./handle-swift.struct/init%28phonenumber,label%29.md)
- [init(identifier: IntentPerson.Identifier, name: IntentPerson.Name, handle: IntentPerson.Handle?, aliases: [IntentPerson.Handle], isMe: Bool, image: DisplayRepresentation.Image?)](./init%28identifier,name,handle,aliases,isme,image%29.md)
- [init(handle: IntentPerson.Handle)](./init%28handle%29.md)
  Initializes an `IntentPerson` from a raw handle, like a phone number or an email address. Use this initializer when the value is not linked to a known contact.
- [init(IntentPerson.Handle.Value, label: IntentPerson.Handle.Label)](./handle-swift.struct/init%28_,label%29.md)
- [init(applicationDefined: String, label: String?)](./handle-swift.struct/init%28applicationdefined,label%29.md)
### Getting the handle’s label
- [var label: IntentPerson.Handle.Label](./handle-swift.struct/label-swift.property.md)
- [IntentPerson.Handle.Label](./handle-swift.struct/label-swift.enum.md)
  A location description that applies to the handle’s content, for example a work or home phone number.
### Getting the handle’s value
- [var value: IntentPerson.Handle.Value](./handle-swift.struct/value-swift.property.md)
  The string value for this `Handle`, such as the specific phone number or email address
- [IntentPerson.Handle.Value](./handle-swift.struct/value-swift.enum.md)
  A type that describes the type of contact information in the handle, such as whether it is an email address, or a phone number.

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

### Getting identifying information
- [var handle: IntentPerson.Handle?](./handle-swift.property.md)
  The primary `Handle` used to contact this `IntentPerson`
- [var aliases: [IntentPerson.Handle]](./aliases.md)
  Other secondary `Handle`s used to contact this `IntentPerson`, if any
- [var isMe: Bool](./isme.md)
  Whether this `IntentPerson` represents the owner of the device
- [var image: DisplayRepresentation.Image?](./image.md)
  An image representing this `IntentPerson`
- [IntentPerson.ParameterMode](./parametermode.md)
  The type of interface to show when someone chooses a parameter that contains information about a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/handle-swift.struct)*