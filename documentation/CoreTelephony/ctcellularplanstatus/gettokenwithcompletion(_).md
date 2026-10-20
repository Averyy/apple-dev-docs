# getTokenWithCompletion(_:)

**Framework**: Core Telephony  
**Kind**: method  
**Role**: Type Method

Retrieves and stores the token associated with your app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class func getTokenWithCompletion(_ completionHandler: @escaping @Sendable (String?, (any Error)?) -> Void)
```

```swift
class func token() async throws -> String
```

```objc
+ (void) getTokenWithCompletion:(void (^)(NSString *token, NSError *error)) completionHandler;
```

#### Discussion

Your app has 30 seconds to call this method after the system generates the token before the system invalidates it. The framework maps the token to the ICCID associated with the original [`MFMessageComposeViewController`](../../MessageUI/mfmessagecomposeviewcontroller.md) instance used for UPI device validation.

## Parameters

- `completionHandler`: A closure the framework calls with the retrieved token and any error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatus/gettokenwithcompletion(_:))*