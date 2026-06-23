# checkValidity(ofToken:completionHandler:)

**Framework**: Core Telephony  
**Kind**: method

Checks the validity of the ICCID associated with the token.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class func checkValidity(ofToken token: String) async throws -> Bool
```

#### Discussion

The `isValid` parameter in the completion handler is `true` when the ICCID associated with the token is present and turned on.

## Parameters

- `token`: The token to validate.
- `completionHandler`: A closure the framework calls with a Boolean indicating whether the ICCID is present and turned on, and any error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatus/checkvalidity(oftoken:completionhandler:))*