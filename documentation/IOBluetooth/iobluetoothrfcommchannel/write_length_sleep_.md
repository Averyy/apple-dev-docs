# write:length:sleep:

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

Sends a block of data in the channel syncronously.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

## Declaration

```objc
- (IOReturn) write:(void *) data length:(UInt16) length sleep:(BOOL) sleep;
```

## Return Value

An error code value. 0 if successful.

## Discussion

***WARNING*** This method is being deprecated in favor of -writeSync:… and -writeAsync:… Sends data through the channel. The number of bytes to be sent must not exceed the channel MTU. If the return value is an error condition none of the data was sent.

## Parameters

- `data`: Is a pointer to the data buffer to be sent.
- `length`: The length of the buffer to be sent (in bytes).
- `sleep`: Is a boolean if set to TRUE the call will wait until it is possible to send data. If set to FALSE and it is not possible to send data the method will return immediately with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/write:length:sleep:)*