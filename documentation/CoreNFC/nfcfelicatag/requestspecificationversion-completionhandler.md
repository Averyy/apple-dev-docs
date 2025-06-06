# requestSpecificationVersion(completionHandler:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Sends the Request Specification Version command, as defined by the FeliCa card specification, to the tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func requestSpecificationVersion() async throws -> (Int, Int, Data, Data)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcfelicatag/requestspecificationversion(completionhandler:))*