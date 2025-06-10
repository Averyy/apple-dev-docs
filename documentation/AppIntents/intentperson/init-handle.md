# init(handle:)

**Framework**: App Intents  
**Kind**: init

Initializes an `IntentPerson` from a raw handle, like a phone number or an email address. Use this initializer when the value is not linked to a known contact.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(handle: IntentPerson.Handle)
```

## See Also

- [init(emailAddress: String, label: IntentPerson.Handle.Label)](intentperson/handle-swift.struct/init(emailaddress:label:).md)
- [init(phoneNumber: String, label: IntentPerson.Handle.Label)](intentperson/handle-swift.struct/init(phonenumber:label:).md)
- [init(identifier: IntentPerson.Identifier, name: IntentPerson.Name, handle: IntentPerson.Handle?, aliases: [IntentPerson.Handle], isMe: Bool, image: DisplayRepresentation.Image?)](intentperson/init(identifier:name:handle:aliases:isme:image:).md)
- [init(IntentPerson.Handle.Value, label: IntentPerson.Handle.Label)](intentperson/handle-swift.struct/init(_:label:).md)
- [init(applicationDefined: String, label: String?)](intentperson/handle-swift.struct/init(applicationdefined:label:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/init(handle:))*