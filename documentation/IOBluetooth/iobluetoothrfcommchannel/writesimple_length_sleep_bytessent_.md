# writeSimple:length:sleep:bytesSent:

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Sends a block of data in the channel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

## Declaration

```objc
- (IOReturn) writeSimple:(void *) data length:(UInt16) length sleep:(BOOL) sleep bytesSent:(UInt32 *) numBytesSent;
```

#### Discussion

***WARNING*** This method is being deprecated in favor of -writeSync:… and -writeAsync:… Sends data through the channel. The number of bytes to be sent is arbitrary. The caller does not have to worry about the MTU.

## Parameters

- `data`: A pointer to the data buffer to be sent.
- `length`: The length of the buffer to be sent (in bytes).
- `sleep`: A boolean if set to TRUE the call will wait until it is possible to send all the data.
- `numBytesSent`: UInt32 pointer in which the caller received the nuber of bytes sent. If set to FALSE and it is not possible to send part of the data the method will return immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/writesimple:length:sleep:bytessent:)*