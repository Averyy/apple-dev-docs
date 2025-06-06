# IntentPerson

**Framework**: App Intents  
**Kind**: struct

Information that identifies a person participating in an intents-based interaction.

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
struct IntentPerson
```

## Mentions

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)

## Topics

### Creating a contact
- [init(identifier: IntentPerson.Identifier, name: IntentPerson.Name, handle: IntentPerson.Handle?, aliases: [IntentPerson.Handle], isMe: Bool, image: DisplayRepresentation.Image?)](intentperson/init(identifier:name:handle:aliases:isme:image:).md)
### Getting the person’s name
- [var name: IntentPerson.Name](intentperson/name-swift.property.md)
  The name of this `IntentPerson`
- [IntentPerson.Name](intentperson/name-swift.enum.md)
  A type that stores name-related information for a person.
### Getting identifying information
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
- [IntentPerson.ParameterMode](intentperson/parametermode.md)
  The type of interface to show when someone chooses a parameter that contains information about a person.
### Getting person-related identifiers
- [var identifier: IntentPerson.Identifier](intentperson/identifier-swift.property.md)
- [IntentPerson.Identifier](intentperson/identifier-swift.enum.md)
  A type that manages a unique identifier for a person.
### Initializers
- [init(handle: IntentPerson.Handle)](intentperson/init(handle:).md)
  Initializes an `IntentPerson` from a raw handle, like a phone number or an email address. Use this initializer when the value is not linked to a known contact.
### Type Aliases
- [IntentPerson.Specification](intentperson/specification.md)
- [IntentPerson.UnwrappedType](intentperson/unwrappedtype.md)
- [IntentPerson.ValueType](intentperson/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: EmptyResolverSpecification<IntentPerson>](intentperson/defaultresolverspecification.md)
### Default Implementations
- [Decodable Implementations](intentperson/decodable-implementations.md)
- [Encodable Implementations](intentperson/encodable-implementations.md)
- [Equatable Implementations](intentperson/equatable-implementations.md)
- [InstanceDisplayRepresentable Implementations](intentperson/instancedisplayrepresentable-implementations.md)
- [TypeDisplayRepresentable Implementations](intentperson/typedisplayrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [DisplayRepresentable](displayrepresentable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson)*