# extendedReadMultipleBlocks(requestFlags:blockRange:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Extended Read Multiple Block command (0x33 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func extendedReadMultipleBlocks(requestFlags flags: NFCISO15693RequestFlag, blockRange: NSRange, completionHandler: @escaping @Sendable ([Data], (any Error)?) -> Void)
```

```swift
func extendedReadMultipleBlocks(requestFlags flags: NFCISO15693RequestFlag, blockRange: NSRange) async throws -> [Data]
```

```objc
- (void) extendedReadMultipleBlocksWithRequestFlags:(NFCISO15693RequestFlag) flags blockRange:(NSRange) blockRange completionHandler:(void (^)(NSArray<NSData *> *dataBlocks, NSError *error)) completionHandler;
```

## See Also

### Sending Extended Commands
- [func extendedReadSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, completionHandler: (Data, (any Error)?) -> Void)](./extendedreadsingleblock%28requestflags,blocknumber,completionhandler%29.md)
  Sends the Extended Read Single Block command (0x30 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
- [func extendedWriteSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, dataBlock: Data, completionHandler: ((any Error)?) -> Void)](./extendedwritesingleblock%28requestflags,blocknumber,datablock,completionhandler%29.md)
  Sends the Extended Write Single Block command (0x31 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
- [func extendedLockBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, completionHandler: ((any Error)?) -> Void)](./extendedlockblock%28requestflags,blocknumber,completionhandler%29.md)
  Sends the Extended Lock Single Block command (0x32 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/extendedreadmultipleblocks(requestflags:blockrange:completionhandler:))*