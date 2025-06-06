# setDelegate(_:)

**Framework**: IOBluetooth  
**Kind**: method

Allows an object to register itself as a client of the RFCOMM channel.

**Availability**:
- macOS ?+

## Declaration

```swift
func setDelegate(_ delegate: Any!) -> IOReturn
```

#### Return Value

Returns kIOReturnSuccess if the delegate is successfully registered.

#### Discussion

A channel delegate is the object the RFCOMM channel uses as target for data and events. The developer will implement only the the methods he/she is interested in. A list of the possible methods is at the end of this file in the definition of the informal protocol IOBluetoothRFCOMMChannelDelegate.

NOTE: This method is only available in macOS 10.2.5 (Bluetooth v1.2) or later. NOTE: Before OS X 10.6, the delegate was retained. On 10.6 and later, it is not.

## Parameters

- `delegate`: The object that will play the role of channel delegate [NOTE the rfcomm channel will reatin the delegate].


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/setdelegate(_:))*