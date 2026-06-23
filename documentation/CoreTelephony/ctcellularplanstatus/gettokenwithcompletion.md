# getTokenWithCompletion(_:)

**Framework**: Core Telephony  
**Kind**: method

Retrieves and stores the token associated with your app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class func token() async throws -> String
```

#### Discussion

Your app has 30 seconds to call this method after the system generates the token before the system invalidates it. The framework maps the token to the ICCID associated with the original [`MFMessageComposeViewController`](https://developer.apple.com/documentation/MessageUI/MFMessageComposeViewController) instance used for UPI device validation.

## Parameters

- `completionHandler`: A closure the framework calls with the retrieved token and any error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatus/gettokenwithcompletion(_:))*