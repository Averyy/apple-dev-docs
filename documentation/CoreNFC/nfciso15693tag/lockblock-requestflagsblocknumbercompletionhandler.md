# lockBlock(requestFlags:blockNumber:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends the Lock Block command (0x22 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func lockBlock(requestFlags flags: NFCISO15693RequestFlag, blockNumber: UInt8) async throws
```

## See Also

- [func readSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, completionHandler: (Data, (any Error)?) -> Void)](nfciso15693tag/readsingleblock(requestflags:blocknumber:completionhandler:).md)
  Sends a Read Single Block command (0x20 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func writeSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, dataBlock: Data, completionHandler: ((any Error)?) -> Void)](nfciso15693tag/writesingleblock(requestflags:blocknumber:datablock:completionhandler:).md)
  Sends the Write Single Block command (0x21 command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/lockblock(requestflags:blocknumber:completionhandler:))*