# getMaxPacketLength()

**Framework**: IOBluetooth  
**Kind**: method

Gets current max packet length.

**Availability**:
- macOS ?+

## Declaration

```swift
func getMaxPacketLength() -> OBEXMaxPacketLength
```

#### Return Value

Max packet length.

#### Discussion

This value  change before and after a connect command has been sent or a connect command response has been received, since the recipient could negotiate a lower max packet size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/getmaxpacketlength())*