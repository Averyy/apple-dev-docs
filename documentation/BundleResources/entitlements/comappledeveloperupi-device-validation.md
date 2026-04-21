# com.apple.developer.upi-device-validation

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether your app can use UPI device enrollment for NPCI financial transactions.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+



**Type**: boolean

**Default**: `NO`

#### Discussion

The Unified Payments Interface (UPI) system, developed by the National Payments Corporation of India (NPCI), supports mobile-app financial transactions. This entitlement allows your app to display a non-editable Messages share sheet with a predefined recipient and token, and includes methods to verify the token was successfully transmitted to the carrier network.

With this entitlement, you can use [`setUPIVerificationCodeSendCompletion(_:)`](https://developer.apple.com/documentation/MessageUI/MFMessageComposeViewController/setUPIVerificationCodeSendCompletion(_:)), which configures the instance of [`MFMessageComposeViewController`](https://developer.apple.com/documentation/MessageUI/MFMessageComposeViewController) with non-editable recipients and body fields. You also need this entitlement to use [`CTCellularPlanStatus`](https://developer.apple.com/documentation/CoreTelephony/CTCellularPlanStatus).

You must be an account holder of a development team to get permission to use this entitlement. To request access, see [`UPI device validation Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/upi-device-validation). Once you’re approved, add the entitlement to your app in the Xcode property list editor. Set the entitlement’s type to Boolean, and the corresponding value to YES.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.upi-device-validation)*