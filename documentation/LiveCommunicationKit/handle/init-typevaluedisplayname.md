# init(type:value:displayName:)

**Framework**: LiveCommunicationKit  
**Kind**: init

Creates a new `Handle`.

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

- `type`: The type of handle (e.g. a phone number or email address)
- `value`: The raw value of the handle.
- `displayName`: The value that should be displayed to the user at the UI layer. If the given   is   then the   is used instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livecommunicationkit/handle/init(type:value:displayname:))*