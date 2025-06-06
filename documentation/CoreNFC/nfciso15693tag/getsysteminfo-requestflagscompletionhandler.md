# getSystemInfo(requestFlags:completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends the Get System Information command (0x2B command code), as defined in the ISO 15693-3 specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func getSystemInfo(requestFlags flags: NFCISO15693RequestFlag, completionHandler: @escaping (Int, Int, Int, Int, Int, (any Error)?) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/getsysteminfo(requestflags:completionhandler:))*