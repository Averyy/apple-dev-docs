# setProtocolForProxy:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the methods known to be handled by the receiver to those in a given protocol.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (void) setProtocolForProxy:(Protocol *) proto;
```

## Discussion

Setting a protocol for a remote proxy reduces network traffic needed to determine method argument and return types.

In order to encode a message’s arguments for transmission over the network, the types of those arguments must be known in advance. When they’re not known, the distributed objects system must send an initial message just to get those types, doubling the network traffic for every new message sent. Setting a protocol alleviates this need for methods defined by the protocol. You can still send messages that aren’t declared in `proto`—in this case the initial message is sent to determine the types, and then the real message is sent.

## Parameters

- `proto`: The protocol for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdistantobject/setprotocolforproxy:)*