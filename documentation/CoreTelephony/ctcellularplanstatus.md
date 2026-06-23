# CTCellularPlanStatus

**Framework**: Core Telephony  
**Kind**: class

An object that validates tokens for UPI device verification or checks the availability of cellular plans for a phone number.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class CTCellularPlanStatus
```

#### Overview

This class provides UPI device validation or cellular plan availability checking.

#### Perform Upi Device Validation

To check if the Integrated Circuit Card Identifier (ICCID) on a device is associated with a given token, use the [`setUPIVerificationCodeSendCompletion(_:)`](https://developer.apple.com/documentation/MessageUI/MFMessageComposeViewController/setUPIVerificationCodeSendCompletion(_:)) method to configure an instance of a view for Unified Payments Interface (UPI) device validation. When the person sends an SMS, the framework creates a token and maps it to the  [`MFMessageComposeViewController`](https://developer.apple.com/documentation/MessageUI/MFMessageComposeViewController) instance’s associated ICCID. Use this token to determine if changes exist to the underlying ICCID.

Call [`getTokenWithCompletion(_:)`](ctcellularplanstatus/gettokenwithcompletion(_:).md) to retrieve the token. Your app has 30 seconds from sending the SMS before the framework drops the token. If the SMS fails, the framework revokes the token.

Use [`checkValidity(ofToken:completionHandler:)`](ctcellularplanstatus/checkvalidity(oftoken:completionhandler:).md) to check the status of the token. The method returns `true` if the ICCID is present and turned on.

For more information on configuring an instance for UPI device validation, see [`setUPIVerificationCodeSendCompletion(_:)`](https://developer.apple.com/documentation/MessageUI/MFMessageComposeViewController/setUPIVerificationCodeSendCompletion(_:)).

> ❗ **Important**:  To use UPI device validation, your app needs the [`com.apple.developer.upi-device-validation`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.upi-device-validation) entitlement.

##### Check Cellular Plan Continuity

To check the status of a cellular plan, use [`requestAuthorization(forPhoneNumber:completion:)`](ctcellularplanstatus/requestauthorization(forphonenumber:completion:).md) to ask the person for permission to access status information for a phone number. Provide phone numbers in [`ITU-T E.164 international format`](https://developer.apple.comhttps://www.itu.int/rec/T-REC-E.164) (for example, `+15550001234`).

After the person grants authorization, the [`getHintForPhoneNumber(_:completion:)`](ctcellularplanstatus/gethintforphonenumber(_:completion:).md) method suggests whether an active cellular plan exists for the phone number by providing:

- **[`CTCellularPlanStatusAvailability`](ctcellularplanstatusavailability.md)**: An indicator that a cellular plan for the phone number exists on the device
- **[`CTCellularPlanStatusAvailabilityConfidence`](ctcellularplanstatusavailabilityconfidence.md)**: A confidence level that the plan is active based on recent cellular activity

After the person answers the permission prompt once, your app can query [`getAuthorizationStatus(forPhoneNumber:completion:)`](ctcellularplanstatus/getauthorizationstatus(forphonenumber:completion:).md) to check for existing authorization without presenting any UI.

## Topics

### Getting and storing a token
- [class func getTokenWithCompletion((String?, (any Error)?) -> Void)](ctcellularplanstatus/gettokenwithcompletion(_:).md)
  Retrieves and stores the token associated with your app.
### Checking the validity of the ICCID
- [class func checkValidity(ofToken: String, completionHandler: (Bool, (any Error)?) -> Void)](ctcellularplanstatus/checkvalidity(oftoken:completionhandler:).md)
  Checks the validity of the ICCID associated with the token.
### Requesting phone number authorization
- [class func requestAuthorization(forPhoneNumber: String, completion: (CTCellularPlanStatusAuthorization, (any Error)?) -> Void)](ctcellularplanstatus/requestauthorization(forphonenumber:completion:).md)
  Presents a prompt that asks the person to allow cellular plan checks for their phone number.
- [enum CTCellularPlanStatusAuthorization](ctcellularplanstatusauthorization.md)
  Constants that indicate the authorization status for accessing cellular plan information for a phone number.
### Checking authorization status
- [class func getAuthorizationStatus(forPhoneNumber: String, completion: (CTCellularPlanStatusAuthorization, (any Error)?) -> Void)](ctcellularplanstatus/getauthorizationstatus(forphonenumber:completion:).md)
  Returns the current authorization status for a phone number without presenting any UI.
### Getting a cellular plan status hint
- [class func getHintForPhoneNumber(String, completion: (CTCellularPlanStatusAvailability, CTCellularPlanStatusAvailabilityConfidence, (any Error)?) -> Void)](ctcellularplanstatus/gethintforphonenumber(_:completion:).md)
  Provides an estimate of the system’s confidence of the existence of an active cellular plan for the device’s phone number.
- [enum CTCellularPlanStatusAvailability](ctcellularplanstatusavailability.md)
  Constants that indicate whether the device has a cellular plan for the given phone number.
- [enum CTCellularPlanStatusAvailabilityConfidence](ctcellularplanstatusavailabilityconfidence.md)
  Constants that indicate the system’s confidence that the device has a cellular plan for a given phone number.

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