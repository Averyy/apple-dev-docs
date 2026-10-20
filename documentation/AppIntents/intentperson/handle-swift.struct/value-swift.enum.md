# IntentPerson.Handle.Value

**Framework**: App Intents  
**Kind**: enum  
**Role**: Enumeration

A type that describes the type of contact information in the handle, such as whether it is an email address, or a phone number.

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
enum Value
```

## Topics

### Enumeration Cases
- [IntentPerson.Handle.Value.applicationDefined(_:)](./value-swift.enum/applicationdefined%28_%29.md)
  An application-defined point of contact, such as a username of an a social networking service
- [IntentPerson.Handle.Value.emailAddress(_:)](./value-swift.enum/emailaddress%28_%29.md)
- [IntentPerson.Handle.Value.phoneNumber(_:)](./value-swift.enum/phonenumber%28_%29.md)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the handle’s value
- [var value: IntentPerson.Handle.Value](./value-swift.property.md)
  The string value for this `Handle`, such as the specific phone number or email address


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/handle-swift.struct/value-swift.enum)*