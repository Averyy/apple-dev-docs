# getAvailableCommandResponsePayloadLength(_:)

**Framework**: IOBluetooth  
**Kind**: method

Determine the maximum amount of data you can send in a particular command response as an OBEX server session.

**Availability**:
- macOS ?+

## Declaration

```swift
func getAvailableCommandResponsePayloadLength(_ inOpCode: OBEXOpCode) -> OBEXMaxPacketLength
```

#### Return Value

The maximum amount of data a particular packet can handle, after accounting for any command response overhead.

#### Discussion

Each OBEX Command response has a certain amount of overhead. Since the negotiated max packet length does not indicate what the maximum data amount you can send in a particular response’s packet, you can use this function to determine how much data to provide in optional headers or body data headers.

## Parameters

- `inOpCode`: The opcode you are interested in responding to (as a server).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/getavailablecommandresponsepayloadlength(_:))*