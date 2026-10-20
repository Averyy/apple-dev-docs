# init(phoneNumber:label:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

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
init(phoneNumber phoneNumberString: String, label: IntentPerson.Handle.Label = .other)
```

## See Also

### Creating a handle
- [init(emailAddress: String, label: IntentPerson.Handle.Label)](./init%28emailaddress,label%29.md)
- [init(identifier: IntentPerson.Identifier, name: IntentPerson.Name, handle: IntentPerson.Handle?, aliases: [IntentPerson.Handle], isMe: Bool, image: DisplayRepresentation.Image?)](../init%28identifier,name,handle,aliases,isme,image%29.md)
- [init(handle: IntentPerson.Handle)](../init%28handle%29.md)
  Initializes an `IntentPerson` from a raw handle, like a phone number or an email address. Use this initializer when the value is not linked to a known contact.
- [init(IntentPerson.Handle.Value, label: IntentPerson.Handle.Label)](./init%28_,label%29.md)
- [init(applicationDefined: String, label: String?)](./init%28applicationdefined,label%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/handle-swift.struct/init(phonenumber:label:))*