# sendRequestWithFlag:commandCode:data:completionHandler:

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```objc
- (void) sendRequestWithFlag:(NSInteger) flags commandCode:(NSInteger) commandCode data:(NSData *) data completionHandler:(void (^)(NFCISO15693ResponseFlag responseFlag, NSData *data, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/sendrequestwithflag:commandcode:data:completionhandler:)*