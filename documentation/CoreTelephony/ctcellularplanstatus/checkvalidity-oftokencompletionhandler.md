# checkValidity(ofToken:completionHandler:)

**Framework**: Core Telephony  
**Kind**: method

Checks for a valid ICCID associated with the token.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class func checkValidity(ofToken token: String) async throws -> Bool
```

#### Discussion

This boolean returns `YES` if the ICCID associated with the token is present and turned-on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatus/checkvalidity(oftoken:completionhandler:))*