# IntentPerson.Handle.Value

**Framework**: App Intents  
**Kind**: enum

A type that describes the type of contact information in the handle, such as whether it is an email address, or a phone number.

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
enum Value
```

## Topics

### Operators
- [static func == (IntentPerson.Handle.Value, IntentPerson.Handle.Value) -> Bool](intentperson/handle-swift.struct/value-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [IntentPerson.Handle.Value.applicationDefined(_:)](intentperson/handle-swift.struct/value-swift.enum/applicationdefined(_:).md)
  An application-defined point of contact, such as a username of an a social networking service
- [IntentPerson.Handle.Value.emailAddress(_:)](intentperson/handle-swift.struct/value-swift.enum/emailaddress(_:).md)
- [IntentPerson.Handle.Value.phoneNumber(_:)](intentperson/handle-swift.struct/value-swift.enum/phonenumber(_:).md)
### Instance Properties
- [var hashValue: Int](intentperson/handle-swift.struct/value-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](intentperson/handle-swift.struct/value-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Decodable Implementations](intentperson/handle-swift.struct/value-swift.enum/decodable-implementations.md)
- [Encodable Implementations](intentperson/handle-swift.struct/value-swift.enum/encodable-implementations.md)
- [Equatable Implementations](intentperson/handle-swift.struct/value-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/handle-swift.struct/value-swift.enum)*