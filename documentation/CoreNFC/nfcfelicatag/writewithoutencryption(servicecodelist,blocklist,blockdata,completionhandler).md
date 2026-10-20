# writeWithoutEncryption(serviceCodeList:blockList:blockData:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Write Without Encryption command, as defined by the FeliCa card specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func writeWithoutEncryption(serviceCodeList: [Data], blockList: [Data], blockData: [Data], completionHandler: @escaping @Sendable (Int, Int, (any Error)?) -> Void)
```

```swift
func writeWithoutEncryption(serviceCodeList: [Data], blockList: [Data], blockData: [Data]) async throws -> (Int, Int)
```

```objc
- (void) writeWithoutEncryptionWithServiceCodeList:(NSArray<NSData *> *) serviceCodeList blockList:(NSArray<NSData *> *) blockList blockData:(NSArray<NSData *> *) blockData completionHandler:(void (^)(NSInteger statusFlag1, NSInteger statusFlag2, NSError *error)) completionHandler;
```

## See Also

### Reading and Writing Without Encryption
- [func readWithoutEncryption(serviceCodeList: [Data], blockList: [Data], completionHandler: (Int, Int, [Data], (any Error)?) -> Void)](./readwithoutencryption%28servicecodelist,blocklist,completionhandler%29.md)
  Sends the Read Without Encryption command, as defined by the FeliCa card specification, to the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/writewithoutencryption(servicecodelist:blocklist:blockdata:completionhandler:))*