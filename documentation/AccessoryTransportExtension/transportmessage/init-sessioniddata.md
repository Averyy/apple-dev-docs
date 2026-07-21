# init(sessionID:data:)

**Framework**: Accessory Transport Extension  
**Kind**: init

Initializes a transport message for a specific capability session.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
init(sessionID: UUID, data: Data)
```

#### Discussion

Create transport messages when your accessory sends data back to the data provider through [`sendMessageToDataProvider(_:)`](accessorytransportsession/sendmessagetodataprovider(_:).md).

## Parameters

- `sessionID`: A unique identifier for the session capability (such as notifications or Live Activities). The system generates this identifier at feature enrollment time, and the value is fixed while the accessory remains paired through AccessorySetupKit.
- `data`: The message data to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/transportmessage/init(sessionid:data:))*