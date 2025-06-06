# getAvailableCommandPayloadLength(_:)

**Framework**: IOBluetooth  
**Kind**: method

Determine the maximum amount of data you can send in a particular command as an OBEX client session.

**Availability**:
- macOS ?+

## Declaration

```swift
func getAvailableCommandPayloadLength(_ inOpCode: OBEXOpCode) -> OBEXMaxPacketLength
```

#### Return Value

The maximum amount of data a particular packet can handle, after accounting for any command overhead.

#### Discussion

Each OBEX Command has a certain amount of overhead. Since the negotiated max packet length does not indicate what the maximum data amount you can send in a particular command’s packet, you can use this function to determine how much data to provide in optional headers or body data headers.

## Parameters

- `inOpCode`: The opcode you are interested in sending (as a client).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/getavailablecommandpayloadlength(_:))*