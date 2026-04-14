# dataEventHandler(event:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Required**: Yes

Handles events that address incoming data destined for the accessory.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
func dataEventHandler(event: AccessoryTransportSession.DataEvent)
```

#### Discussion

Implement this method to relay data to your accessory over Bluetooth or another transport mechanism.

## Parameters

- `event`: A data event that contains either plaintext or encrypted data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/eventhandler/dataeventhandler(event:))*