# init(handle:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Initializes an `IntentPerson` from a raw handle, like a phone number or an email address. Use this initializer when the value is not linked to a known contact.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(handle: IntentPerson.Handle)
```

## See Also

### Creating a handle
- [init(emailAddress: String, label: IntentPerson.Handle.Label)](./handle-swift.struct/init%28emailaddress,label%29.md)
- [init(phoneNumber: String, label: IntentPerson.Handle.Label)](./handle-swift.struct/init%28phonenumber,label%29.md)
- [init(identifier: IntentPerson.Identifier, name: IntentPerson.Name, handle: IntentPerson.Handle?, aliases: [IntentPerson.Handle], isMe: Bool, image: DisplayRepresentation.Image?)](./init%28identifier,name,handle,aliases,isme,image%29.md)
- [init(IntentPerson.Handle.Value, label: IntentPerson.Handle.Label)](./handle-swift.struct/init%28_,label%29.md)
- [init(applicationDefined: String, label: String?)](./handle-swift.struct/init%28applicationdefined,label%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentperson/init(handle:))*