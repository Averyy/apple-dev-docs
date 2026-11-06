# dataEventHandler(event:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method

Handles events that address incoming data sent to the accessory.

**Availability**:
- iOS 26.4+

## Declaration

```swift
func dataEventHandler(event: AccessoryTransportSession.DataEvent)
```

## Discussion

Implement this method to relay data to your accessory over Bluetooth or another transport mechanism.

## Parameters

- `event`: A data event that contains either plaintext or encrypted data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/eventhandler/dataeventhandler(event:)-7c5yr)*