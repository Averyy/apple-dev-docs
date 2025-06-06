# extendedReadMultipleBlocks(requestFlags:blockRange:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends the Extended Read Multiple Block command (0x33 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func extendedReadMultipleBlocks(requestFlags flags: NFCISO15693RequestFlag, blockRange: NSRange) async throws -> [Data]
```

## See Also

- [func extendedReadSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, completionHandler: (Data, (any Error)?) -> Void)](nfciso15693tag/extendedreadsingleblock(requestflags:blocknumber:completionhandler:).md)
  Sends the Extended Read Single Block command (0x30 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
- [func extendedWriteSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, dataBlock: Data, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/extendedwritesingleblock(requestflags:blocknumber:datablock:completionhandler:).md)
  Sends the Extended Write Single Block command (0x31 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
- [func extendedLockBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/extendedlockblock(requestflags:blocknumber:completionhandler:).md)
  Sends the Extended Lock Single Block command (0x32 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/extendedreadmultipleblocks(requestflags:blockrange:completionhandler:))*