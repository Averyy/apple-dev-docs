# sendData(toTransport:dataLength:)

**Framework**: IOBluetooth  
**Kind**: method  
**Role**: Instance Method

You must override this to send data over your transport. This does nothing by default, it will return a kOBEXUnsupportedError.

**Availability**:
- macOS

## Declaration

```swift
func sendData(toTransport inDataToSend: UnsafeMutableRawPointer!, dataLength inDataLength: Int) -> OBEXError
```

```objc
- (OBEXError) sendDataToTransport:(void *) inDataToSend dataLength:(size_t) inDataLength;
```

## Discussion

Tranport subclasses must override this! When called you should send the data over the transport to the remote session.

## Parameters

- `inDataToSend`: Data to shove over the transport to a remote OBEX session.
- `inDataLength`: Length of data passed in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/senddata(totransport:datalength:))*