# send(_:type:name:)

**Framework**: IOBluetooth  
**Kind**: method

Send data to a remote target

**Availability**:
- macOS ?+

## Declaration

```swift
func send(_ inData: Data!, type inType: String!, name inName: String!) -> OBEXError
```

#### Return Value

kOBEXSuccess, kOBEXSessionBusyError, or kOBEXBadArgumentError initially. Further results returned through the fileTransferServicesSendComplete: and fileTransferServicesSendProgress: delegate methods if initially successful.

#### Discussion

Use this method when you have data to send but no file to read from.

## Parameters

- `inData`: The data to be sent
- `inType`: The type of the data to be sent that will be used in the OBEX type header, usually a mime-type. For example, use “text/x-vCard” when sending vCards. This argument is optional.
- `inName`: The name of the file that the data can be referenced as.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexfiletransferservices/send(_:type:name:))*