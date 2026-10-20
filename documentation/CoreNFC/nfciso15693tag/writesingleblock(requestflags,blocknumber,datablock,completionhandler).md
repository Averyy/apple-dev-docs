# writeSingleBlock(requestFlags:blockNumber:dataBlock:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Write Single Block command (0x21 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func writeSingleBlock(requestFlags flags: NFCISO15693RequestFlag, blockNumber: UInt8, dataBlock: Data, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeSingleBlock(requestFlags flags: NFCISO15693RequestFlag, blockNumber: UInt8, dataBlock: Data) async throws
```

```objc
- (void) writeSingleBlockWithRequestFlags:(NFCISO15693RequestFlag) flags blockNumber:(uint8_t) blockNumber dataBlock:(NSData *) dataBlock completionHandler:(void (^)(NSError *error)) completionHandler;
```

## See Also

### Sending Single Block Commands
- [func readSingleBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, completionHandler: (Data, (any Error)?) -> Void)](./readsingleblock%28requestflags,blocknumber,completionhandler%29.md)
  Sends a Read Single Block command (0x20 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func lockBlock(requestFlags: NFCISO15693RequestFlag, blockNumber: UInt8, completionHandler: ((any Error)?) -> Void)](./lockblock%28requestflags,blocknumber,completionhandler%29.md)
  Sends the Lock Block command (0x22 command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/writesingleblock(requestflags:blocknumber:datablock:completionhandler:))*