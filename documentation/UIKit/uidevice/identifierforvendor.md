# identifierForVendor

**Framework**: UIKit  
**Kind**: property

An alphanumeric string that uniquely identifies a device to the app’s vendor.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var identifierForVendor: UUID? { get }
```

#### Discussion

The value of this property is the same for apps that come from the same vendor running on the same device. A different value is returned for apps on the same device that come from different vendors, and for apps on different devices regardless of vendor.

Normally, the vendor is determined by data provided by the App Store. If the app wasn’t installed from the app store (such as enterprise apps and apps still in development), then a vendor identifier is calculated based on the app’s bundle ID. The bundle ID is assumed to be in reverse-DNS format.

- In iOS 6, the first two components of the bundle ID are used to generate the vendor ID. If the bundle ID only has a single component, then the entire bundle ID is used.
- In IOS 7, all components of the bundle except for the last component are used to generate the vendor ID. If the bundle ID only has a single component, then the entire bundle ID is used.

The following table shows a collection of bundle IDs and which portions of the bundle ID the system uses to calculate the vendor ID.

| Bundle ID | iOS 6.x | iOS 7.x |
| --- | --- | --- |
| Com.example.app1 | .app1 | .app1 |
| Com.example.app2 | .app2 | .app2 |
| Com.example.app.app1 | .app.app1 | .app1 |
| Com.example.app.app2 | .app.app2 | .app2 |
| Example |  |  |

For example, `com.example.app1` and `com.example.app2` would appear to have the same vendor ID.

If the value is `nil`, wait and get the value again later. This happens, for example, after the device has been restarted but before the user has unlocked the device.

The value in this property remains the same while the app (or another app from the same vendor) is installed on the iOS device. The value changes when the user deletes all of that vendor’s apps from the device and subsequently reinstalls one or more of them. The value can also change when installing test builds using Xcode or when installing an app on a device using ad-hoc distribution. Therefore, if your app stores the value of this property anywhere, you should gracefully handle situations where the identifier changes.

## See Also

- [var name: String](uidevice/name.md)
  The name of the device.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/identifierforvendor)*