# NFCISO15693Tag

**Framework**: Core NFC  
**Kind**: protocol  
**Role**: Protocol

An interface for interacting with an ISO 15693 tag.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol NFCISO15693Tag : NFCNDEFTag, __NFCTag
```

```objc
@protocol NFCISO15693Tag <NFCTag, NFCNDEFTag>
```

## Overview

The [`NFCTagReaderSessionDelegate`](./nfctagreadersessiondelegate-2joku.md) receives an object that conforms to the [`NFCISO15693Tag`](./nfciso15693tag.md) protocol when the [`NFCTagReaderSession`](./nfctagreadersession.md) detects an ISO 15693-compatible tag. For the delegate to receive the tag object, your app must include the [`Near Field Communication Tag Reader Session Formats Entitlement`](../BundleResources/entitlements/com.apple.developer.nfc.readersession.formats.md).

For the reader session to read and write data to the tag, it must be available to the reader session. Use the [`isAvailable`](./nfctag-swift.enum/isavailable.md) property to check the tag’s availability.

## Topics

### Getting Tag Information
- [var icManufacturerCode: Int](./nfciso15693tag/icmanufacturercode.md)
  The IC manufacturer code of the tag.
- [var icSerialNumber: Data](./nfciso15693tag/icserialnumber.md)
  The IC serial number assigned to the tag by the manufacturer.
- [var identifier: Data](./nfciso15693tag/identifier.md)
  The unique hardware identifier of the tag.
### Selecting Request Flag Options
- [typealias RequestFlag](./requestflag.md)
  A set of bit mask options that, when combined, define the request flags to use when sending a command.
### Getting System Information
- [func getSystemInfo(requestFlags: NFCISO15693RequestFlag, completionHandler: (Int, Int, Int, Int, Int, (any Error)?) -> Void)](./nfciso15693tag/getsysteminfo%28requestflags,completionhandler%29.md)
  Sends the Get System Information command (0x2B command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Single Block Commands
- [func readSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, completionHandler: (Data, (any Error)?) -> Void)](./nfciso15693tag/readsingleblock%28requestflags,blocknumber,completionhandler%29.md)
  Sends a Read Single Block command (0x20 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func writeSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, dataBlock: Data, completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/writesingleblock%28requestflags,blocknumber,datablock,completionhandler%29.md)
  Sends the Write Single Block command (0x21 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func lockBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/lockblock%28requestflags,blocknumber,completionhandler%29.md)
  Sends the Lock Block command (0x22 command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Multi-block Commands
- [func readMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, completionHandler: ([Data], (any Error)?) -> Void)](./nfciso15693tag/readmultipleblocks%28requestflags,blockrange,completionhandler%29.md)
  Sends the Read Multiple Blocks command (0x23 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func writeMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, dataBlocks: [Data], completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/writemultipleblocks%28requestflags,blockrange,datablocks,completionhandler%29.md)
  Sends the Write Multiple Blocks command (0x24 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func getMultipleBlockSecurityStatus(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, completionHandler: ([NSNumber], (any Error)?) -> Void)](./nfciso15693tag/getmultipleblocksecuritystatus%28requestflags,blockrange,completionhandler%29.md)
  Sends the Get Multiple Block Security Status command (0x2C command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Application Family Identifier Commands
- [func writeAFI(requestFlags: NFCISO15693RequestFlag, afi: UInt8, completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/writeafi%28requestflags,afi,completionhandler%29.md)
  Sends the Write AFI command (0x27 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func lockAFI(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/lockafi%28requestflags,completionhandler%29.md)
  Sends the Lock AFI command (0x28 command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Data Storage Format Identifier Commands
- [func writeDSFID(requestFlags: NFCISO15693RequestFlag, dsfid: UInt8, completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/writedsfid%28requestflags,dsfid,completionhandler%29.md)
  Sends the Write DSFID command (0x29 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func lockDFSID(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/lockdfsid%28requestflags,completionhandler%29.md)
  Sends the Lock DSFID command (0x2A command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Reset to Ready Command
- [func resetToReady(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/resettoready%28requestflags,completionhandler%29.md)
  Sends the Reset To Ready command (0x26 command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Select Command
- [func select(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/select%28requestflags,completionhandler%29.md)
  Sends the Select command (0x25 command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Stay Quiet Command
- [func stayQuiet(completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/stayquiet%28completionhandler%29.md)
  Sends a Stay Quiet command (0x02 command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Custom Commands
- [func customCommand(requestFlags: NFCISO15693RequestFlag, customCommandCode: Int, customRequestParameters: Data, completionHandler: (Data, (any Error)?) -> Void)](./nfciso15693tag/customcommand%28requestflags,customcommandcode,customrequestparameters,completionhandler%29.md)
  Sends a custom command (0xA0 to 0xDF command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Extended Commands
- [func extendedReadSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, completionHandler: (Data, (any Error)?) -> Void)](./nfciso15693tag/extendedreadsingleblock%28requestflags,blocknumber,completionhandler%29.md)
  Sends the Extended Read Single Block command (0x30 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
- [func extendedWriteSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, dataBlock: Data, completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/extendedwritesingleblock%28requestflags,blocknumber,datablock,completionhandler%29.md)
  Sends the Extended Write Single Block command (0x31 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
- [func extendedLockBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/extendedlockblock%28requestflags,blocknumber,completionhandler%29.md)
  Sends the Extended Lock Single Block command (0x32 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
- [func extendedReadMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, completionHandler: ([Data], (any Error)?) -> Void)](./nfciso15693tag/extendedreadmultipleblocks%28requestflags,blockrange,completionhandler%29.md)
  Sends the Extended Read Multiple Block command (0x33 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
### Getting Response Errors
- [let NFCISO15693TagResponseErrorKey: String](./nfciso15693tagresponseerrorkey.md)
  A user information dictionary key indicating that a tag responded with a command error.
### Instance Methods
- [func authenticate(requestFlags: NFCISO15693RequestFlag, cryptoSuiteIdentifier: Int, message: Data) async throws -> (NFCISO15693ResponseFlag, Data)](./nfciso15693tag/authenticate%28requestflags,cryptosuiteidentifier,message%29.md)
- [func authenticate(requestFlags: NFCISO15693RequestFlag, cryptoSuiteIdentifier: Int, message: Data, resultHandler: (Result<(NFCISO15693ResponseFlag, Data), any Error>) -> Void)](./nfciso15693tag/authenticate%28requestflags,cryptosuiteidentifier,message,resulthandler%29.md)
- [func challenge(requestFlags: NFCISO15693RequestFlag, cryptoSuiteIdentifier: Int, message: Data) async throws](./nfciso15693tag/challenge%28requestflags,cryptosuiteidentifier,message%29.md)
- [func challenge(requestFlags: NFCISO15693RequestFlag, cryptoSuiteIdentifier: Int, message: Data, completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/challenge%28requestflags,cryptosuiteidentifier,message,completionhandler%29.md)
- [func customCommand(requestFlags: NFCISO15693RequestFlag, customCommandCode: Int, customRequestParameters: Data, resultHandler: (Result<Data, any Error>) -> Void)](./nfciso15693tag/customcommand%28requestflags,customcommandcode,customrequestparameters,resulthandler%29.md)
- [func extendedFastReadMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange) async throws -> [Data]](./nfciso15693tag/extendedfastreadmultipleblocks%28requestflags,blockrange%29.md)
- [func extendedFastReadMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, resultHandler: (Result<[Data], any Error>) -> Void)](./nfciso15693tag/extendedfastreadmultipleblocks%28requestflags,blockrange,resulthandler%29.md)
- [func extendedGetMultipleBlockSecurityStatus(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange) async throws -> NFCISO15693MultipleBlockSecurityStatus](./nfciso15693tag/extendedgetmultipleblocksecuritystatus%28requestflags,blockrange%29.md)
- [func extendedGetMultipleBlockSecurityStatus(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, resultHandler: (Result<NFCISO15693MultipleBlockSecurityStatus, any Error>) -> Void)](./nfciso15693tag/extendedgetmultipleblocksecuritystatus%28requestflags,blockrange,resulthandler%29.md)
- [func extendedReadSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, resultHandler: (Result<Data, any Error>) -> Void)](./nfciso15693tag/extendedreadsingleblock%28requestflags,blocknumber,resulthandler%29.md)
- [func extendedWriteMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, dataBlocks: [Data]) async throws](./nfciso15693tag/extendedwritemultipleblocks%28requestflags,blockrange,datablocks%29.md)
- [func extendedWriteMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, dataBlocks: [Data], completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/extendedwritemultipleblocks%28requestflags,blockrange,datablocks,completionhandler%29.md)
- [func fastReadMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange) async throws -> [Data]](./nfciso15693tag/fastreadmultipleblocks%28requestflags,blockrange%29.md)
- [func fastReadMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, resultHandler: (Result<[Data], any Error>) -> Void)](./nfciso15693tag/fastreadmultipleblocks%28requestflags,blockrange,resulthandler%29.md)
- [func getSystemInfo(requestFlags: NFCISO15693RequestFlag, resultHandler: (Result<NFCISO15693SystemInfo, any Error>) -> Void)](./nfciso15693tag/getsysteminfo%28requestflags,resulthandler%29.md)
- [func keyUpdate(requestFlags: NFCISO15693RequestFlag, keyIdentifier: Int, message: Data) async throws -> (NFCISO15693ResponseFlag, Data)](./nfciso15693tag/keyupdate%28requestflags,keyidentifier,message%29.md)
- [func keyUpdate(requestFlags: NFCISO15693RequestFlag, keyIdentifier: Int, message: Data, resultHandler: (Result<(NFCISO15693ResponseFlag, Data), any Error>) -> Void)](./nfciso15693tag/keyupdate%28requestflags,keyidentifier,message,resulthandler%29.md)
- [func lockDSFID(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](./nfciso15693tag/lockdsfid%28requestflags,completionhandler%29.md)
- [func readBuffer(requestFlags: NFCISO15693RequestFlag) async throws -> (NFCISO15693ResponseFlag, Data)](./nfciso15693tag/readbuffer%28requestflags%29.md)
- [func readBuffer(requestFlags: NFCISO15693RequestFlag, resultHandler: (Result<(NFCISO15693ResponseFlag, Data), any Error>) -> Void)](./nfciso15693tag/readbuffer%28requestflags,resulthandler%29.md)
- [func readMultipleBlock(readConfiguration: NFCISO15693ReadMultipleBlocksConfiguration, completionHandler: (Data, (any Error)?) -> Void)](./nfciso15693tag/readmultipleblock%28readconfiguration,completionhandler%29.md)
- [func readMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, resultHandler: (Result<[Data], any Error>) -> Void)](./nfciso15693tag/readmultipleblocks%28requestflags,blockrange,resulthandler%29.md)
- [func readSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, resultHandler: (Result<Data, any Error>) -> Void)](./nfciso15693tag/readsingleblock%28requestflags,blocknumber,resulthandler%29.md)
- [func sendCustomCommand(commandConfiguration: NFCISO15693CustomCommandConfiguration, completionHandler: (Data, (any Error)?) -> Void)](./nfciso15693tag/sendcustomcommand%28commandconfiguration,completionhandler%29.md)
- [func sendRequest(requestFlags: Int, commandCode: Int, data: Data?) async throws -> (NFCISO15693ResponseFlag, Data?)](./nfciso15693tag/sendrequest%28requestflags,commandcode,data%29.md)
- [func sendRequest(requestFlags: Int, commandCode: Int, data: Data?, resultHandler: (Result<(NFCISO15693ResponseFlag, Data?), any Error>) -> Void)](./nfciso15693tag/sendrequest%28requestflags,commandcode,data,resulthandler%29.md)
- [func systemInfo(requestFlags: NFCISO15693RequestFlag) async throws -> NFCISO15693SystemInfo](./nfciso15693tag/systeminfo%28requestflags%29.md)
- [- authenticateWithRequestFlags:cryptoSuiteIdentifier:message:completionHandler:](./nfciso15693tag/authenticatewithrequestflags_cryptosuiteidentifier_message_completionhandler_.md)
- [- challengeWithRequestFlags:cryptoSuiteIdentifier:message:completionHandler:](./nfciso15693tag/challengewithrequestflags_cryptosuiteidentifier_message_completionhandler_.md)
- [- extendedFastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:](./nfciso15693tag/extendedfastreadmultipleblockswithrequestflag_blockrange_completionhandler_.md)
- [- extendedGetMultipleBlockSecurityStatusWithRequestFlag:blockRange:completionHandler:](./nfciso15693tag/extendedgetmultipleblocksecuritystatuswithrequestflag_blockrange_completionhandler_.md)
- [- extendedWriteMultipleBlocksWithRequestFlags:blockRange:dataBlocks:completionHandler:](./nfciso15693tag/extendedwritemultipleblockswithrequestflags_blockrange_datablocks_completionhandler_.md)
- [- fastReadMultipleBlocksWithRequestFlag:blockRange:completionHandler:](./nfciso15693tag/fastreadmultipleblockswithrequestflag_blockrange_completionhandler_.md)
- [- getSystemInfoAndUIDWithRequestFlag:completionHandler:](./nfciso15693tag/getsysteminfoanduidwithrequestflag_completionhandler_.md)
- [- keyUpdateWithRequestFlags:keyIdentifier:message:completionHandler:](./nfciso15693tag/keyupdatewithrequestflags_keyidentifier_message_completionhandler_.md)
- [- readBufferWithRequestFlags:completionHandler:](./nfciso15693tag/readbufferwithrequestflags_completionhandler_.md)
- [- sendRequestWithFlag:commandCode:data:completionHandler:](./nfciso15693tag/sendrequestwithflag_commandcode_data_completionhandler_.md)

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
- [protocol NFCFeliCaTag](./nfcfelicatag.md)
  An interface for interacting with a FeliCa™ tag.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag)*