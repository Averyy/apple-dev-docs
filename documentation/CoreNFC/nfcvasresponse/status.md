# status

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

A response APDU status code.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var status: NFCVASResponse.ErrorCode { get }
```

```objc
@property (nonatomic, assign, readonly) NFCVASErrorCode status;
```

## See Also

### Getting the Response Status
- [typealias VASErrorCode](../vaserrorcode.md)
  Constants representing APDU status codes for a VAS response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcvasresponse/status)*