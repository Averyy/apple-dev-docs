# readMultipleBlocks(requestFlags:blockRange:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Read Multiple Blocks command (0x23 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func readMultipleBlocks(requestFlags flags: NFCISO15693RequestFlag, blockRange: NSRange, completionHandler: @escaping @Sendable ([Data], (any Error)?) -> Void)
```

```swift
func readMultipleBlocks(requestFlags flags: NFCISO15693RequestFlag, blockRange: NSRange) async throws -> [Data]
```

```objc
- (void) readMultipleBlocksWithRequestFlags:(NFCISO15693RequestFlag) flags blockRange:(NSRange) blockRange completionHandler:(void (^)(NSArray<NSData *> *dataBlocks, NSError *error)) completionHandler;
```

## See Also

### Sending Multi-block Commands
- [func writeMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, dataBlocks: [Data], completionHandler: ((any Error)?) -> Void)](./writemultipleblocks%28requestflags,blockrange,datablocks,completionhandler%29.md)
  Sends the Write Multiple Blocks command (0x24 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func getMultipleBlockSecurityStatus(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, completionHandler: ([NSNumber], (any Error)?) -> Void)](./getmultipleblocksecuritystatus%28requestflags,blockrange,completionhandler%29.md)
  Sends the Get Multiple Block Security Status command (0x2C command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/readmultipleblocks(requestflags:blockrange:completionhandler:))*