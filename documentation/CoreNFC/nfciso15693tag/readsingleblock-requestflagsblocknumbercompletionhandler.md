# readSingleBlock(requestFlags:blockNumber:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends a Read Single Block command (0x20 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func readSingleBlock(requestFlags flags: NFCISO15693RequestFlag, blockNumber: UInt8) async throws -> Data
```

#### Discussion

This method sends the tag’s [`identifier`](nfciso15693tag/identifier.md) with the command.

## Parameters

- `flags`: The request flags. The [`RequestFlagAddress`](nfciso15693requestflag/requestflagaddress.md) flag is enforced by default. However, using the [`RequestFlagSelect`](nfciso15693requestflag/requestflagselect.md) flag disables the [`RequestFlagAddress`](nfciso15693requestflag/requestflagaddress.md) flag.
- `blockNumber`: The number of the block to read. Blocks are numbered from 0 to 255 inclusively.
- `completionHandler`: A handler that the reader session invokes after the operation completes. The session calls completionHandler on the dispatch queue that you provided when creating the NFCTagReaderSession object. The handler has the following parameters: - **data**: A [`NSData`](https://developer.apple.com/documentation/foundation/nsdata) object containing the blocks of data read from the tag. If the request flags include [`RequestFlagOption`](nfciso15693requestflag/requestflagoption.md), the first byte of the data contains the associated block security status.
- **error**: `nil` when the operation is successful; otherwise, an [`NSError`](https://developer.apple.com/documentation/foundation/nserror) object indicating that a problem occurred while communicating with the tag. When the tag responds with a command error, the error’s [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/userinfo) directory contains the [`NFCISO15693TagResponseErrorKey`](nfciso15693tagresponseerrorkey.md) and the error’s [`code`](https://developer.apple.com/documentation/foundation/nserror/code) property has a value defined in the ISO15693-3 specification.

## See Also

- [func writeSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, dataBlock: Data, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/writesingleblock(requestflags:blocknumber:datablock:completionhandler:).md)
  Sends the Write Single Block command (0x21 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func lockBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/lockblock(requestflags:blocknumber:completionhandler:).md)
  Sends the Lock Block command (0x22 command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/readsingleblock(requestflags:blocknumber:completionhandler:))*