# com.apple.developer.upi-device-validation

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app can use Unified Payments Interface (UPI) device enrollment.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

#### Discussion

With this entitlement, you can use doc://com.apple.documentation/documentation/messageui/mfmessagecomposeviewcontroller/4setupiverificationcodesendcompletion(_:), which configures the instance of [`MFMessageComposeViewController`](https://developer.apple.com/documentation/MessageUI/MFMessageComposeViewController) with non-editable recipients and body fields. You also need this entitlement to use [`CTCellularPlanStatus`](https://developer.apple.com/documentation/CoreTelephony/CTCellularPlanStatus).

You must be an account holder of a development team to get permission to use this entitlement. To request access, see [`UPI device validation Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/upi-device-validation). Add the entitlement to your app in the Xcode property list editor. Set the entitlement’s type to Boolean, and the corresponding value to YES.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.upi-device-validation)*