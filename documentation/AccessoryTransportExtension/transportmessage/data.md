# data

**Framework**: Accessory Transport Extension  
**Kind**: property

A data object that contains the message content.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
let data: Data
```

#### Discussion

For messages from the system containing sensitive data, this data is encrypted and ready for transmission to your accessory. For messages from your accessory containing sensitive data, encrypt this data before creating the transport message.

## See Also

- [let sessionID: UUID](transportmessage/sessionid.md)
  A unique identifier for the message’s capability session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/transportmessage/data)*