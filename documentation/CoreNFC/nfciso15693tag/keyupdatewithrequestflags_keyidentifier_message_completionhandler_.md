# keyUpdateWithRequestFlags:keyIdentifier:message:completionHandler:

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```objc
- (void) keyUpdateWithRequestFlags:(NFCISO15693RequestFlag) flags keyIdentifier:(NSInteger) keyIdentifier message:(NSData *) message completionHandler:(void (^)(NFCISO15693ResponseFlag responseFlag, NSData *response, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/keyupdatewithrequestflags:keyidentifier:message:completionhandler:)*