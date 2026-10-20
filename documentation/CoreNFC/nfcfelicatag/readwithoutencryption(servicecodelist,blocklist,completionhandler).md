# readWithoutEncryption(serviceCodeList:blockList:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Read Without Encryption command, as defined by the FeliCa card specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func readWithoutEncryption(serviceCodeList: [Data], blockList: [Data], completionHandler: @escaping @Sendable (Int, Int, [Data], (any Error)?) -> Void)
```

```swift
func readWithoutEncryption(serviceCodeList: [Data], blockList: [Data]) async throws -> (Int, Int, [Data])
```

```objc
- (void) readWithoutEncryptionWithServiceCodeList:(NSArray<NSData *> *) serviceCodeList blockList:(NSArray<NSData *> *) blockList completionHandler:(void (^)(NSInteger statusFlag1, NSInteger statusFlag2, NSArray<NSData *> *blockData, NSError *error)) completionHandler;
```

## See Also

### Reading and Writing Without Encryption
- [func writeWithoutEncryption(serviceCodeList: [Data], blockList: [Data], blockData: [Data], completionHandler: (Int, Int, (any Error)?) -> Void)](./writewithoutencryption%28servicecodelist,blocklist,blockdata,completionhandler%29.md)
  Sends the Write Without Encryption command, as defined by the FeliCa card specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/readwithoutencryption(servicecodelist:blocklist:completionhandler:))*