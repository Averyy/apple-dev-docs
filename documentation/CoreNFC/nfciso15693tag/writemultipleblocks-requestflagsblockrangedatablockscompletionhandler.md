# writeMultipleBlocks(requestFlags:blockRange:dataBlocks:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends the Write Multiple Blocks command (0x24 command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func writeMultipleBlocks(requestFlags flags: NFCISO15693RequestFlag, blockRange: NSRange, dataBlocks: [Data]) async throws
```

## See Also

- [func readMultipleBlocks(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, completionHandler: ([Data], (any Error)?) -> Void)](nfciso15693tag/readmultipleblocks(requestflags:blockrange:completionhandler:).md)
  Sends the Read Multiple Blocks command (0x23 command code), as defined in the ISO 15693-3 specification, to the tag.
- [func getMultipleBlockSecurityStatus(requestFlags: NFCISO15693RequestFlag, blockRange: NSRange, completionHandler: ([NSNumber], (any Error)?) -> Void)](nfciso15693tag/getmultipleblocksecuritystatus(requestflags:blockrange:completionhandler:).md)
  Sends the Get Multiple Block Security Status command (0x2C command code), as defined in the ISO 15693-3 specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/writemultipleblocks(requestflags:blockrange:datablocks:completionhandler:))*