# init(sessionID:data:)

**Framework**: Accessory Transport Extension  
**Kind**: init  
**Role**: Initializer

Initializes a transport message for a specific feature.

**Availability**:
- iOS 26.5+

## Declaration

```swift
init(sessionID: UUID, data: Data)
```

## Discussion

Create transport messages when your accessory sends data back to the data provider through [`sendMessageToDataProvider(_:)`](../accessorytransportsession/sendmessagetodataprovider%28_%29.md).

## Parameters

- `sessionID`: A unique identifier for the feature that the message belongs to, such as notifications or Live Activities. The value is fixed while the accessory remains paired through AccessorySetupKit.
- `data`: The message data to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/transportmessage/init(sessionid:data:))*