# getSystemInfo(requestFlags:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends the Get System Information command (0x2B command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0
- iPadOS 13.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0

## Declaration

```swift
func getSystemInfo(requestFlags flags: NFCISO15693RequestFlag, completionHandler: @escaping (Int, Int, Int, Int, Int, (any Error)?) -> Void)
```

```objc
- (void) getSystemInfoWithRequestFlag:(NFCISO15693RequestFlag) flags completionHandler:(void (^)(NSInteger dsfid, NSInteger afi, NSInteger blockSize, NSInteger blockCount, NSInteger icReference, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/getsysteminfo(requestflags:completionhandler:))*