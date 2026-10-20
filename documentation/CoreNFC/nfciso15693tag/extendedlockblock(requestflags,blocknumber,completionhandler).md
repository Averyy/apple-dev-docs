# extendedLockBlock(requestFlags:blockNumber:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Extended Lock Single Block command (0x32 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func extendedLockBlock(requestFlags flags: NFCISO15693RequestFlag, blockNumber: Int, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func extendedLockBlock(requestFlags flags: NFCISO15693RequestFlag, blockNumber: Int) async throws
```

```objc
- (void) extendedLockBlockWithRequestFlags:(NFCISO15693RequestFlag) flags blockNumber:(NSInteger) blockNumber completionHandler:(void (^)(NSError *error)) completionHandler;
```

## See Also

### Sending Extended Commands
- [func extendedReadSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, completionHandler: (Data, (any Error)?) -> Void)](./extendedreadsingleblock%28requestflags,blocknumber,completionhandler%29.md)
  Sends the Extended Read Single Block command (0x30 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
- [func extendedWriteSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: Int, dataBlock: Data, completionHandler: ((any Error)?) -> Void)](./extendedwritesingleblock%28requestflags,blocknumber,datablock,completionhandler%29.md)
  Sends the Extended Write Single Block command (0x31 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.
- [func extendedReadMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, completionHandler: ([Data], (any Error)?) -> Void)](./extendedreadmultipleblocks%28requestflags,blockrange,completionhandler%29.md)
  Sends the Extended Read Multiple Block command (0x33 command code), as defined in the NFC Forum Type 5 tag specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/extendedlockblock(requestflags:blocknumber:completionhandler:))*