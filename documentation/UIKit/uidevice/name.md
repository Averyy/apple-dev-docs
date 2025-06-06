# name

**Framework**: Uikit  
**Kind**: property

The name of the device.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var name: String { get }
```

#### Discussion

The default value of this property varies according to the device’s operating system version number:

| OS | Default value | Example |
| --- | --- | --- |
| iOS 15 and earlier | User-assigned device name | `"Ravi’s iPhone 13 Pro"` |
| iOS 16 and later | Generic device name | `"iPhone"` |

In iOS, the  is available in the Settings app under General > About > Name. To access the user-assigned device name through this property in iOS 16 and later, your app must meet certain criteria and be assigned an entitlement. For information, see [`com.apple.developer.device-information.user-assigned-device-name`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.device-information.user-assigned-device-name).

> **Note**:  Session 10096: [`What’s new in privacy`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10096) Session 10068: [`What’s new in UIKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10068)

## See Also

- [var systemName: String](uidevice/systemname.md)
  The name of the operating system running on the device.
- [var systemVersion: String](uidevice/systemversion.md)
  The current version of the operating system.
- [var model: String](uidevice/model.md)
  The model of the device.
- [var localizedModel: String](uidevice/localizedmodel.md)
  The model of the device as a localized string.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](uidevice/userinterfaceidiom.md)
  The style of interface to use on the current device.
- [var identifierForVendor: UUID?](uidevice/identifierforvendor.md)
  An alphanumeric string that uniquely identifies a device to the app’s vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/name)*