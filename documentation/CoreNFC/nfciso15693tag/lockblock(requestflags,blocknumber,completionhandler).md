# lockBlock(requestFlags:blockNumber:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Lock Block command (0x22 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func lockBlock(requestFlags flags: NFCISO15693RequestFlag, blockNumber: UInt8, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func lockBlock(requestFlags flags: NFCISO15693RequestFlag, blockNumber: UInt8) async throws
```

```objc
- (void) lockBlockWithRequestFlags:(NFCISO15693RequestFlag) flags blockNumber:(uint8_t) blockNumber completionHandler:(void (^)(NSError *error)) completionHandler;
```

## See Also

### Sending Single Block Commands
- [func readSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, completionHandler: (Data, (any Error)?) -> Void)](./readsingleblock%28requestflags,blocknumber,completionhandler%29.md)
  Sends a Read Single Block command (0x20 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func writeSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, dataBlock: Data, completionHandler: ((any Error)?) -> Void)](./writesingleblock%28requestflags,blocknumber,datablock,completionhandler%29.md)
  Sends the Write Single Block command (0x21 command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/lockblock(requestflags:blocknumber:completionhandler:))*