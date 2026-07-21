# sessionID

**Framework**: Accessory Transport Extension  
**Kind**: property

A unique identifier for the message’s capability session.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
let sessionID: UUID
```

#### Discussion

This identifier correlates messages with their capability (such as notifications or Live Activities). The system generates the session ID at feature enrollment time, and the value is fixed while the accessory remains paired through AccessorySetupKit.

## See Also

- [let data: Data](transportmessage/data.md)
  A data object that contains the message content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/transportmessage/sessionid)*