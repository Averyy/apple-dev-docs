# requestServiceV2(nodeCodeList:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Request Service V2 command, as defined by the FeliCa card specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func requestServiceV2(nodeCodeList: [Data], completionHandler: @escaping @Sendable (Int, Int, NFCFeliCaEncryptionId, [Data], [Data], (any Error)?) -> Void)
```

```swift
func requestServiceV2(nodeCodeList: [Data]) async throws -> (Int, Int, NFCFeliCaEncryptionId, [Data], [Data])
```

```objc
- (void) requestServiceV2WithNodeCodeList:(NSArray<NSData *> *) nodeCodeList completionHandler:(void (^)(NSInteger statusFlag1, NSInteger statusFlag2, NFCFeliCaEncryptionId encryptionIdentifier, NSArray<NSData *> *nodeKeyVersionListAES, NSArray<NSData *> *nodeKeyVersionListDES, NSError *error)) completionHandler;
```

## See Also

### Requesting Services
- [func requestService(nodeCodeList: [Data], completionHandler: ([Data], (any Error)?) -> Void)](./requestservice%28nodecodelist,completionhandler%29.md)
  Sends the Request Service command, as defined by the FeliCa card specification, to the tag.
- [typealias EncryptionId](../encryptionid.md)
  Encryption identifiers indicating the type of encryption algorithm used in the response of a Request Service V2 command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/requestservicev2(nodecodelist:completionhandler:))*