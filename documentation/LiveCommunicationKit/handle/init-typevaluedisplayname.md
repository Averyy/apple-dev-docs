# init(type:value:displayName:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates a new handle that identifies a participant in a conversation.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
init(type: Handle.Kind, value: String, displayName: String? = nil)
```

## Parameters

- `type`: The type of the handle; for example, a phone number or email address.
- `value`: The raw value of the handle.
- `displayName`: The name that people see for a participant of a conversation in the conversation UI. If the   is  , the system uses   instead.

## See Also

- [init(from: any Decoder) throws](handle/init(from:).md)
  Creates a new instance by decoding from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/handle/init(type:value:displayname:))*