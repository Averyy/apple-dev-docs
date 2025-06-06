# NFCISO15693Tag

**Framework**: Core NFC  
**Kind**: protocol

An interface for interacting with an ISO 15693 tag.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol NFCISO15693Tag : NFCNDEFTag, __NFCTag
```

#### Overview

The [`NFCTagReaderSessionDelegate`](nfctagreadersessiondelegate-2joku.md) receives an object that conforms to the [`NFCISO15693Tag`](nfciso15693tag.md) protocol when the [`NFCTagReaderSession`](nfctagreadersession.md) detects an ISO 15693-compatible tag. For the delegate to receive the tag object, your app must include the [`Near Field Communication Tag Reader Session Formats Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.nfc.readersession.formats).

For the reader session to read and write data to the tag, it must be available to the reader session. Use the [`isAvailable`](nfctag-swift.enum/isavailable.md) property to check the tag’s availability.

## Topics

### Getting Tag Information
- [var icManufacturerCode: Int](nfciso15693tag/icmanufacturercode.md)
  The IC manufacturer code of the tag.
- [var icSerialNumber: Data](nfciso15693tag/icserialnumber.md)
  The IC serial number assigned to the tag by the manufacturer.
- [var identifier: Data](nfciso15693tag/identifier.md)
  The unique hardware identifier of the tag.
### Selecting Request Flag Options
- [typealias RequestFlag](requestflag.md)
  A set of bit mask options that, when combined, define the request flags to use when sending a command.
### Getting System Information
- [func getSystemInfo(requestFlags: NFCISO15693RequestFlag, completionHandler: (Int, Int, Int, Int, Int, (any Error)?) -> Void)](nfciso15693tag/getsysteminfo(requestflags:completionhandler:).md)
  Sends the Get System Information command (0x2B command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Single Block Commands
- [func readSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, completionHandler: (Data, (any Error)?) -> Void)](nfciso15693tag/readsingleblock(requestflags:blocknumber:completionhandler:).md)
  Sends a Read Single Block command (0x20 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func writeSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, dataBlock: Data, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/writesingleblock(requestflags:blocknumber:datablock:completionhandler:).md)
  Sends the Write Single Block command (0x21 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func lockBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/lockblock(requestflags:blocknumber:completionhandler:).md)
  Sends the Lock Block command (0x22 command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Multi-block Commands
- [func readMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, completionHandler: ([Data], (any Error)?) -> Void)](nfciso15693tag/readmultipleblocks(requestflags:blockrange:completionhandler:).md)
  Sends the Read Multiple Blocks command (0x23 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func writeMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, dataBlocks: [Data], completionHandler: ((any Error)?) -> Void)](nfciso15693tag/writemultipleblocks(requestflags:blockrange:datablocks:completionhandler:).md)
  Sends the Write Multiple Blocks command (0x24 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func getMultipleBlockSecurityStatus(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, completionHandler: ([NSNumber], (any Error)?) -> Void)](nfciso15693tag/getmultipleblocksecuritystatus(requestflags:blockrange:completionhandler:).md)
  Sends the Get Multiple Block Security Status command (0x2C command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Application Family Identifier Commands
- [func writeAFI(requestFlags: NFCISO15693RequestFlag, afi: UInt8, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/writeafi(requestflags:afi:completionhandler:).md)
  Sends the Write AFI command (0x27 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func lockAFI(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/lockafi(requestflags:completionhandler:).md)
  Sends the Lock AFI command (0x28 command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Data Storage Format Identifier Commands
- [func writeDSFID(requestFlags: NFCISO15693RequestFlag, dsfid: UInt8, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/writedsfid(requestflags:dsfid:completionhandler:).md)
  Sends the Write DSFID command (0x29 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func lockDFSID(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/lockdfsid(requestflags:completionhandler:).md)
  Sends the Lock DSFID command (0x2A command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Reset to Ready Command
- [func resetToReady(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/resettoready(requestflags:completionhandler:).md)
  Sends the Reset To Ready command (0x26 command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Select Command
- [func select(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/select(requestflags:completionhandler:).md)
  Sends the Select command (0x25 command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Stay Quiet Command
- [func stayQuiet(completionHandler: ((any Error)?) -> Void)](nfciso15693tag/stayquiet(completionhandler:).md)
  Sends a Stay Quiet command (0x02 command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Custom Commands
- [func customCommand(requestFlags: NFCISO15693RequestFlag, customCommandCode: Int, customRequestParameters: Data, completionHandler: (Data, (any Error)?) -> Void)](nfciso15693tag/customcommand(requestflags:customcommandcode:customrequestparameters:completionhandler:).md)
  Sends a custom command (0xA0 to 0xDF command code), as defined in the ISO 15693-3 specification, to the tag.
### Sending Extended Commands
- [func extendedReadSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, completionHandler: (Data, (any Error)?) -> Void)](nfciso15693tag/extendedreadsingleblock(requestflags:blocknumber:completionhandler:).md)
  Sends the Extended Read Single Block command (0x30 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
- [func extendedWriteSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, dataBlock: Data, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/extendedwritesingleblock(requestflags:blocknumber:datablock:completionhandler:).md)
  Sends the Extended Write Single Block command (0x31 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
- [func extendedLockBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/extendedlockblock(requestflags:blocknumber:completionhandler:).md)
  Sends the Extended Lock Single Block command (0x32 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
- [func extendedReadMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, completionHandler: ([Data], (any Error)?) -> Void)](nfciso15693tag/extendedreadmultipleblocks(requestflags:blockrange:completionhandler:).md)
  Sends the Extended Read Multiple Block command (0x33 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
### Getting Response Errors
- [let NFCISO15693TagResponseErrorKey: String](nfciso15693tagresponseerrorkey.md)
  A user information dictionary key indicating that a tag responded with a command error.
### Instance Methods
- [func authenticate(requestFlags: NFCISO15693RequestFlag, cryptoSuiteIdentifier: Int, message: Data) async throws -> (NFCISO15693ResponseFlag, Data)](nfciso15693tag/authenticate(requestflags:cryptosuiteidentifier:message:).md)
- [func authenticate(requestFlags: NFCISO15693RequestFlag, cryptoSuiteIdentifier: Int, message: Data, resultHandler: (Result<(NFCISO15693ResponseFlag, Data), any Error>) -> Void)](nfciso15693tag/authenticate(requestflags:cryptosuiteidentifier:message:resulthandler:).md)
- [func challenge(requestFlags: NFCISO15693RequestFlag, cryptoSuiteIdentifier: Int, message: Data) async throws](nfciso15693tag/challenge(requestflags:cryptosuiteidentifier:message:).md)
- [func challenge(requestFlags: NFCISO15693RequestFlag, cryptoSuiteIdentifier: Int, message: Data, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/challenge(requestflags:cryptosuiteidentifier:message:completionhandler:).md)
- [func customCommand(requestFlags: NFCISO15693RequestFlag, customCommandCode: Int, customRequestParameters: Data, resultHandler: (Result<Data, any Error>) -> Void)](nfciso15693tag/customcommand(requestflags:customcommandcode:customrequestparameters:resulthandler:).md)
- [func extendedFastReadMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange) async throws -> [Data]](nfciso15693tag/extendedfastreadmultipleblocks(requestflags:blockrange:).md)
- [func extendedFastReadMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, resultHandler: (Result<[Data], any Error>) -> Void)](nfciso15693tag/extendedfastreadmultipleblocks(requestflags:blockrange:resulthandler:).md)
- [func extendedGetMultipleBlockSecurityStatus(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange) async throws -> NFCISO15693MultipleBlockSecurityStatus](nfciso15693tag/extendedgetmultipleblocksecuritystatus(requestflags:blockrange:).md)
- [func extendedGetMultipleBlockSecurityStatus(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, resultHandler: (Result<NFCISO15693MultipleBlockSecurityStatus, any Error>) -> Void)](nfciso15693tag/extendedgetmultipleblocksecuritystatus(requestflags:blockrange:resulthandler:).md)
- [func extendedReadSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, resultHandler: (Result<Data, any Error>) -> Void)](nfciso15693tag/extendedreadsingleblock(requestflags:blocknumber:resulthandler:).md)
- [func extendedWriteMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, dataBlocks: [Data]) async throws](nfciso15693tag/extendedwritemultipleblocks(requestflags:blockrange:datablocks:).md)
- [func extendedWriteMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, dataBlocks: [Data], completionHandler: ((any Error)?) -> Void)](nfciso15693tag/extendedwritemultipleblocks(requestflags:blockrange:datablocks:completionhandler:).md)
- [func fastReadMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange) async throws -> [Data]](nfciso15693tag/fastreadmultipleblocks(requestflags:blockrange:).md)
- [func fastReadMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, resultHandler: (Result<[Data], any Error>) -> Void)](nfciso15693tag/fastreadmultipleblocks(requestflags:blockrange:resulthandler:).md)
- [func getSystemInfo(requestFlags: NFCISO15693RequestFlag, resultHandler: (Result<NFCISO15693SystemInfo, any Error>) -> Void)](nfciso15693tag/getsysteminfo(requestflags:resulthandler:).md)
- [func keyUpdate(requestFlags: NFCISO15693RequestFlag, keyIdentifier: Int, message: Data) async throws -> (NFCISO15693ResponseFlag, Data)](nfciso15693tag/keyupdate(requestflags:keyidentifier:message:).md)
- [func keyUpdate(requestFlags: NFCISO15693RequestFlag, keyIdentifier: Int, message: Data, resultHandler: (Result<(NFCISO15693ResponseFlag, Data), any Error>) -> Void)](nfciso15693tag/keyupdate(requestflags:keyidentifier:message:resulthandler:).md)
- [func lockDSFID(requestFlags: NFCISO15693RequestFlag, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/lockdsfid(requestflags:completionhandler:).md)
- [func readBuffer(requestFlags: NFCISO15693RequestFlag) async throws -> (NFCISO15693ResponseFlag, Data)](nfciso15693tag/readbuffer(requestflags:).md)
- [func readBuffer(requestFlags: NFCISO15693RequestFlag, resultHandler: (Result<(NFCISO15693ResponseFlag, Data), any Error>) -> Void)](nfciso15693tag/readbuffer(requestflags:resulthandler:).md)
- [func readMultipleBlock(readConfiguration: NFCISO15693ReadMultipleBlocksConfiguration, completionHandler: (Data, (any Error)?) -> Void)](nfciso15693tag/readmultipleblock(readconfiguration:completionhandler:).md)
- [func readMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, resultHandler: (Result<[Data], any Error>) -> Void)](nfciso15693tag/readmultipleblocks(requestflags:blockrange:resulthandler:).md)
- [func readSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, resultHandler: (Result<Data, any Error>) -> Void)](nfciso15693tag/readsingleblock(requestflags:blocknumber:resulthandler:).md)
- [func sendCustomCommand(commandConfiguration: NFCISO15693CustomCommandConfiguration, completionHandler: (Data, (any Error)?) -> Void)](nfciso15693tag/sendcustomcommand(commandconfiguration:completionhandler:).md)
- [func sendRequest(requestFlags: Int, commandCode: Int, data: Data?) async throws -> (NFCISO15693ResponseFlag, Data?)](nfciso15693tag/sendrequest(requestflags:commandcode:data:).md)
- [func sendRequest(requestFlags: Int, commandCode: Int, data: Data?, resultHandler: (Result<(NFCISO15693ResponseFlag, Data?), any Error>) -> Void)](nfciso15693tag/sendrequest(requestflags:commandcode:data:resulthandler:).md)
- [func systemInfo(requestFlags: NFCISO15693RequestFlag) async throws -> NFCISO15693SystemInfo](nfciso15693tag/systeminfo(requestflags:).md)

## Relationships

### Inherits From
- [NFCNDEFTag](nfcndeftag.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Creating NFC Tags from Your iPhone](creating-nfc-tags-from-your-iphone.md)
  Save data to tags, and interact with them using native tag protocols.
- [protocol NFCISO7816Tag](nfciso7816tag.md)
  An interface for interacting with an ISO 7816 tag.
- [protocol NFCFeliCaTag](nfcfelicatag.md)
  An interface for interacting with a FeliCa™ tag.
- [protocol NFCMiFareTag](nfcmifaretag.md)
  An interface for interacting with a MIFARE® tag.
- [protocol NFCNDEFTag](nfcndeftag.md)
  An interface for interacting with an NDEF tag.
- [enum NFCTag](nfctag-swift.enum.md)
  An object that represents an NFC tag object.
- [class NFCTagCommandConfiguration](nfctagcommandconfiguration.md)
  A set of parameters you use to define the configuration of an NFC tag command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag)*