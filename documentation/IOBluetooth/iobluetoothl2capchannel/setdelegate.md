# setDelegate(_:)

**Framework**: IOBluetooth  
**Kind**: method

Allows an object to register itself as client of the L2CAP channel.

**Availability**:
- macOS ?+

## Declaration

```swift
func setDelegate(_ channelDelegate: Any!) -> IOReturn
```

#### Return Value

Returns kIOReturnSuccess if the delegate is successfully registered.

#### Discussion

A channel delegate is the object the L2CAP channel uses as target for data and events. The developer will implement only the the methods he/she is interested in. A list of the possible methods is at the end of this file in the definition of the informal protocol IOBluetoothL2CAPChannelDelegate. A newly opened L2CAP channel will not complete its configuration process until the client that opened it registers a connectionHandler. This prevents that case where incoming data is received before the client is ready.

NOTE: This method is only available in macOS 10.2.5 (Bluetooth v1.2) or later.

## Parameters

- `channelDelegate`: The object that will play the role of channel delegate [NOTE the l2cap channel will retain the delegate].


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/setdelegate(_:))*