# readSingleBlock(requestFlags:blockNumber:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends a Read Single Block command (0x20 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func readSingleBlock(requestFlags flags: NFCISO15693RequestFlag, blockNumber: UInt8, completionHandler: @escaping @Sendable (Data, (any Error)?) -> Void)
```

```swift
func readSingleBlock(requestFlags flags: NFCISO15693RequestFlag, blockNumber: UInt8) async throws -> Data
```

```objc
- (void) readSingleBlockWithRequestFlags:(NFCISO15693RequestFlag) flags blockNumber:(uint8_t) blockNumber completionHandler:(void (^)(NSData *data, NSError *error)) completionHandler;
```

#### Discussion

This method sends the tag’s [`identifier`](./identifier.md) with the command.

## Parameters

- `flags`: The request flags. The [`RequestFlagAddress`](../nfciso15693requestflag/requestflagaddress.md) flag is enforced by default. However, using the [`RequestFlagSelect`](../nfciso15693requestflag/requestflagselect.md) flag disables the [`RequestFlagAddress`](../nfciso15693requestflag/requestflagaddress.md) flag.
- `blockNumber`: The number of the block to read. Blocks are numbered from 0 to 255 inclusively.
- `completionHandler`: A handler that the reader session invokes after the operation completes. The session calls completionHandler on the dispatch queue that you provided when creating the NFCTagReaderSession object.

  The handler has the following parameters:

  - **data**: A [`NSData`](../../Foundation/nsdata.md) object containing the blocks of data read from the tag. If the request flags include [`RequestFlagOption`](../nfciso15693requestflag/requestflagoption.md), the first byte of the data contains the associated block security status.
  - **error**: `nil` when the operation is successful; otherwise, an [`NSError`](../../Foundation/nserror.md) object indicating that a problem occurred while communicating with the tag.

  When the tag responds with a command error, the error’s [`userInfo`](../../Foundation/nserror/userinfo.md) directory contains the [`NFCISO15693TagResponseErrorKey`](../nfciso15693tagresponseerrorkey.md) and the error’s [`code`](../../Foundation/nserror/code.md) property has a value defined in the ISO15693-3 specification.

## See Also

### Sending Single Block Commands
- [func writeSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, dataBlock: Data, completionHandler: ((any Error)?) -> Void)](./writesingleblock%28requestflags,blocknumber,datablock,completionhandler%29.md)
  Sends the Write Single Block command (0x21 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func lockBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, completionHandler: ((any Error)?) -> Void)](./lockblock%28requestflags,blocknumber,completionhandler%29.md)
  Sends the Lock Block command (0x22 command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/readsingleblock(requestflags:blocknumber:completionhandler:))*