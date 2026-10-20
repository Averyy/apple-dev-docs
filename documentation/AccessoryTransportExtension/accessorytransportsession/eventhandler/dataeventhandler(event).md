# dataEventHandler(event:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles events that address incoming data destined for the accessory.

**Availability**:
- iOS 26.4+ - Deprecated in 26.5 (renamed: messageReceived(_:completion:))

## Declaration

```swift
func dataEventHandler(event: AccessoryTransportSession.DataEvent)
```

#### Discussion

Implement this method to relay data to your accessory over Bluetooth or another transport mechanism.

## Parameters

- `event`: A data event that contains either plaintext or encrypted data.

## Default Implementations

### AccessoryTransportSession.EventHandler Implementations
- [func dataEventHandler(event: AccessoryTransportSession.DataEvent)](./dataeventhandler%28event%29-7c5yr.md)

## See Also

### Handling data events
- [func messageReceived(TransportMessage, completion: (AccessoryMessage.Result) -> Void)](./messagereceived%28_,completion%29.md)
  Handles incoming messages for transmission to the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/eventhandler/dataeventhandler(event:))*