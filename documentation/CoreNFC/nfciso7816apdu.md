# NFCISO7816APDU

**Framework**: Core NFC  
**Kind**: class

An object representing an ISO 7816 application protocol data unit (APDU).

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class NFCISO7816APDU
```

## Topics

### Creating an APDU Object
- [init(instructionClass: UInt8, instructionCode: UInt8, p1Parameter: UInt8, p2Parameter: UInt8, data: Data, expectedResponseLength: Int)](nfciso7816apdu/init(instructionclass:instructioncode:p1parameter:p2parameter:data:expectedresponselength:).md)
  Creates an APDU object with the instruction class and code, parameter bytes, and expected response length.
- [init?(data: Data)](nfciso7816apdu/init(data:).md)
  Creates an APDU object with the data buffer containing the full APDU.
### Getting the Instruction Bytes
- [var instructionClass: UInt8](nfciso7816apdu/instructionclass.md)
  The value of the instruction class (CLA) byte.
- [var instructionCode: UInt8](nfciso7816apdu/instructioncode.md)
  The value of the instruction code (INS) byte.
### Get the Parameter Bytes
- [var p1Parameter: UInt8](nfciso7816apdu/p1parameter.md)
  The value of the P1 parameter byte.
- [var p2Parameter: UInt8](nfciso7816apdu/p2parameter.md)
  The value of the P2 parameter byte.
### Getting the APDU Data
- [var data: Data?](nfciso7816apdu/data.md)
  The data to transmit.
### Getting the Expected Response Length
- [var expectedResponseLength: Int](nfciso7816apdu/expectedresponselength.md)
  The expected response data length (Le) in bytes.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func sendCommand(apdu: NFCISO7816APDU, resultHandler: (Result<NFCISO7816ResponseAPDU, any Error>) -> Void)](nfciso7816tag/sendcommand(apdu:resulthandler:).md)
  Sends an application protocol data unit (APDU) to the tag and receives a response APDU.
- [func sendCommand(apdu: NFCISO7816APDU, completionHandler: (Data, UInt8, UInt8, (any Error)?) -> Void)](nfciso7816tag/sendcommand(apdu:completionhandler:).md)
  Sends an application protocol data unit (APDU) to the tag and receives a response APDU.
- [struct NFCISO7816ResponseAPDU](nfciso7816responseapdu.md)
  An object containing the response from the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso7816apdu)*