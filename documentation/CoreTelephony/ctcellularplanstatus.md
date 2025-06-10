# CTCellularPlanStatus

**Framework**: Core Telephony  
**Kind**: class

An object used for retrieving and checking the validity of a token.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
class CTCellularPlanStatus
```

#### Overview

`CTCellularPlanStatus` checks if the Integrated Circuit Card Identifier (ICCID) on a device is associated with a given token. Use the [`setUPIVerificationCodeSendCompletion:`](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/4240039-setupiverificationcodesendcomple) method to configure the instance of a view for Unified Payments Interface (UPI) device validation. This process generates your token, which you can use to help determine if there are any changes to the underlying ICCID.

After you generate a token, use [`getTokenWithCompletion(_:)`](ctcellularplanstatus/gettokenwithcompletion(_:).md) to retrieve the token associated with your app. Your app has 30 seconds to call `getTokenWithCompletion` before the system invalidates the token. If called in time, the framework sends and stores a token associated with your app. The token is mapped to the ICCID associated with the original `MFMessageComposeViewController` instance.

Use [`checkValidity(ofToken:completionHandler:)`](ctcellularplanstatus/checkvalidity(oftoken:completionhandler:).md) to check the status of the token. If the ICCID is present and turned-on, `checkValidityOfToken` returns `YES`.

For more information on configuring an instance for UPI device validation, see [`setUPIVerificationCodeSendCompletion:`](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/4240039-setupiverificationcodesendcomple).

> ❗ **Important**:  To use this class you need the `com.apple.developer.upi-device-validation` entitlement. For more information, see  [`com.apple.developer.upi-device-validation`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.upi-device-validation).

## Topics

### Get and store a token
- [class func getTokenWithCompletion((String?, (any Error)?) -> Void)](ctcellularplanstatus/gettokenwithcompletion(_:).md)
  A method you use to retrieve and store the token.
### Check the validity of the ICCID associated with the token
- [class func checkValidity(ofToken: String, completionHandler: (Bool, (any Error)?) -> Void)](ctcellularplanstatus/checkvalidity(oftoken:completionhandler:).md)
  Checks for a valid ICCID associated with the token.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctcellularplanstatus)*