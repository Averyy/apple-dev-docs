# getSystemInfoAndUIDWithRequestFlag:completionHandler:

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```objc
- (void) getSystemInfoAndUIDWithRequestFlag:(NFCISO15693RequestFlag) flags completionHandler:(void (^)(NSData *uid, NSInteger dsfid, NSInteger afi, NSInteger blockSize, NSInteger blockCount, NSInteger icReference, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/getsysteminfoanduidwithrequestflag:completionhandler:)*