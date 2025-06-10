# init(emailAddress:label:)

**Framework**: App Intents  
**Kind**: init

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
init(emailAddress emailAddressString: String, label: IntentPerson.Handle.Label = .other)
```

## See Also

- [init(phoneNumber: String, label: IntentPerson.Handle.Label)](intentperson/handle-swift.struct/init(phonenumber:label:).md)
- [init(identifier: IntentPerson.Identifier, name: IntentPerson.Name, handle: IntentPerson.Handle?, aliases: [IntentPerson.Handle], isMe: Bool, image: DisplayRepresentation.Image?)](intentperson/init(identifier:name:handle:aliases:isme:image:).md)
- [init(handle: IntentPerson.Handle)](intentperson/init(handle:).md)
  Initializes an `IntentPerson` from a raw handle, like a phone number or an email address. Use this initializer when the value is not linked to a known contact.
- [init(IntentPerson.Handle.Value, label: IntentPerson.Handle.Label)](intentperson/handle-swift.struct/init(_:label:).md)
- [init(applicationDefined: String, label: String?)](intentperson/handle-swift.struct/init(applicationdefined:label:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/handle-swift.struct/init(emailaddress:label:))*