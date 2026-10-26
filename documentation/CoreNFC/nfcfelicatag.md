# NFCFeliCaTag

**Framework**: Core NFC  
**Kind**: protocol  
**Role**: Protocol

An interface for interacting with a FeliCa™ tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol NFCFeliCaTag : NFCNDEFTag, __NFCTag
```

```objc
@protocol NFCFeliCaTag <NFCTag, NFCNDEFTag>
```

#### Overview

FeliCa is a trademark of Sony Corporation.

## Topics

### Specifying System Codes
- [ISO18092 system codes for NFC Tag Reader Session](../BundleResources/entitlements/com.apple.developer.nfc.readersession.felica.systemcodes.md)
  A list of FeliCa system codes that the app supports.
### Getting Current Information
- [var currentSystemCode: Data](./nfcfelicatag/currentsystemcode.md)
  The system code most recently selected by the reader session during a polling sequence.
- [var currentIDm: Data](./nfcfelicatag/currentidm.md)
  The manufacturer identifier for the system currently selected by the reader session.
### Polling
- [func polling(systemCode: Data, requestCode: NFCFeliCaPollingRequestCode, timeSlot: NFCFeliCaPollingTimeSlot, completionHandler: (Data, Data, (any Error)?) -> Void)](./nfcfelicatag/polling%28systemcode,requestcode,timeslot,completionhandler%29.md)
  Sends the Polling command as defined by FeliCa card specification to the tag.
- [typealias PollingRequestCode](./pollingrequestcode.md)
  Codes that specify the type of the data to request when polling.
- [typealias PollingTimeSlot](./pollingtimeslot.md)
  Constants that specify the maximum number of time slots.
### Requesting Services
- [func requestService(nodeCodeList: [Data], completionHandler: ([Data], (any Error)?) -> Void)](./nfcfelicatag/requestservice%28nodecodelist,completionhandler%29.md)
  Sends the Request Service command, as defined by the FeliCa card specification, to the tag.
- [func requestServiceV2(nodeCodeList: [Data], completionHandler: (Int, Int, NFCFeliCaEncryptionId, [Data], [Data], (any Error)?) -> Void)](./nfcfelicatag/requestservicev2%28nodecodelist,completionhandler%29.md)
  Sends the Request Service V2 command, as defined by the FeliCa card specification, to the tag.
- [typealias EncryptionId](./encryptionid.md)
  Encryption identifiers indicating the type of encryption algorithm used in the response of a Request Service V2 command.
### Requesting Responses
- [func requestResponse(completionHandler: (Int, (any Error)?) -> Void)](./nfcfelicatag/requestresponse%28completionhandler%29.md)
  Sends the Request Response command, as defined by the FeliCa card specification, to the tag.
### Requesting Specification Versions
- [func requestSpecificationVersion(completionHandler: (Int, Int, Data, Data, (any Error)?) -> Void)](./nfcfelicatag/requestspecificationversion%28completionhandler%29.md)
  Sends the Request Specification Version command, as defined by the FeliCa card specification, to the tag.
### Requesting System Codes
- [func requestSystemCode(completionHandler: ([Data], (any Error)?) -> Void)](./nfcfelicatag/requestsystemcode%28completionhandler%29.md)
  Sends the Request System Code command, as defined by the FeliCa card specification, to the tag.
### Resetting Modes
- [func resetMode(completionHandler: (Int, Int, (any Error)?) -> Void)](./nfcfelicatag/resetmode%28completionhandler%29.md)
  Sends the Reset Mode command, as defined by the FeliCa card specification, to the tag.
### Reading and Writing Without Encryption
- [func readWithoutEncryption(serviceCodeList: [Data], blockList: [Data], completionHandler: (Int, Int, [Data], (any Error)?) -> Void)](./nfcfelicatag/readwithoutencryption%28servicecodelist,blocklist,completionhandler%29.md)
  Sends the Read Without Encryption command, as defined by the FeliCa card specification, to the tag.
- [func writeWithoutEncryption(serviceCodeList: [Data], blockList: [Data], blockData: [Data], completionHandler: (Int, Int, (any Error)?) -> Void)](./nfcfelicatag/writewithoutencryption%28servicecodelist,blocklist,blockdata,completionhandler%29.md)
  Sends the Write Without Encryption command, as defined by the FeliCa card specification, to the tag.
### Sending FeliCa Commands
- [func sendFeliCaCommand(commandPacket: Data, completionHandler: (Data, (any Error)?) -> Void)](./nfcfelicatag/sendfelicacommand%28commandpacket,completionhandler%29.md)
  Sends the FeliCa command packet data to the tag.
### Instance Methods
- [func polling(systemCode: Data, requestCode: NFCFeliCaPollingRequestCode, timeSlot: NFCFeliCaPollingTimeSlot, resultHandler: (Result<NFCFeliCaPollingResponse, any Error>) -> Void)](./nfcfelicatag/polling%28systemcode,requestcode,timeslot,resulthandler%29.md)
- [func readWithoutEncryption(serviceCodeList: [Data], blockList: [Data], resultHandler: (Result<(NFCFeliCaStatusFlag, [Data]), any Error>) -> Void)](./nfcfelicatag/readwithoutencryption%28servicecodelist,blocklist,resulthandler%29.md)
- [func requestResponse(resultHandler: (Result<Int, any Error>) -> Void)](./nfcfelicatag/requestresponse%28resulthandler%29.md)
- [func requestService(nodeCodeList: [Data], resultHandler: (Result<[Data], any Error>) -> Void)](./nfcfelicatag/requestservice%28nodecodelist,resulthandler%29.md)
- [func requestServiceV2(nodeCodeList: [Data], resultHandler: (Result<NFCFeliCaRequsetServiceV2Response, any Error>) -> Void)](./nfcfelicatag/requestservicev2%28nodecodelist,resulthandler%29.md)
- [func requestSpecificationVersion(resultHandler: (Result<NFCFeliCaRequestSpecificationVersionResponse, any Error>) -> Void)](./nfcfelicatag/requestspecificationversion%28resulthandler%29.md)
- [func requestSystemCode(resultHandler: (Result<[Data], any Error>) -> Void)](./nfcfelicatag/requestsystemcode%28resulthandler%29.md)
- [func resetMode(resultHandler: (Result<NFCFeliCaStatusFlag, any Error>) -> Void)](./nfcfelicatag/resetmode%28resulthandler%29.md)
- [func sendFeliCaCommand(commandPacket: Data, resultHandler: (Result<Data, any Error>) -> Void)](./nfcfelicatag/sendfelicacommand%28commandpacket,resulthandler%29.md)
- [func writeWithoutEncryption(serviceCodeList: [Data], blockList: [Data], blockData: [Data], resultHandler: (Result<NFCFeliCaStatusFlag, any Error>) -> Void)](./nfcfelicatag/writewithoutencryption%28servicecodelist,blocklist,blockdata,resulthandler%29.md)

## Relationships

### Inherits From
- [NFCNDEFTag](./nfcndeftag.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [NFCTag](./nfctag-c.protocol.md)

## See Also

### Tag types
- [Creating NFC Tags from Your iPhone](./creating-nfc-tags-from-your-iphone.md)
  Save data to tags, and interact with them using native tag protocols.
- [protocol NFCISO7816Tag](./nfciso7816tag.md)
  An interface for interacting with an ISO 7816 tag.
- [protocol NFCISO15693Tag](./nfciso15693tag.md)
  An interface for interacting with an ISO 15693 tag.
- [protocol NFCMiFareTag](./nfcmifaretag.md)
  An interface for interacting with a MIFARE® tag.
- [protocol NFCNDEFTag](./nfcndeftag.md)
  An interface for interacting with an NDEF tag.
- [enum NFCTag](./nfctag-swift.enum.md)
  An object that represents an NFC tag object.
- [class NFCTagCommandConfiguration](./nfctagcommandconfiguration.md)
  A set of parameters you use to define the configuration of an NFC tag command.
- [NFCTag](./nfctag-c.protocol.md)
  An interface for interacting with an NFC or RFID tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag)*