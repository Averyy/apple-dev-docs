# name

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The name of the device.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var name: String { get }
```

```objc
@property (nonatomic, strong, readonly) NSString * name;
```

## Discussion

The default value of this property varies according to the device’s operating system version number:

| OS | Default value | Example |
| --- | --- | --- |
| iOS 15 and earlier | User-assigned device name | `"Ravi’s iPhone 13 Pro"` |
| iOS 16 and later | Generic device name | `"iPhone"` |

In iOS, the *user-assigned device name* is available in the Settings app under General > About > Name. To access the user-assigned device name through this property in iOS 16 and later, your app must meet certain criteria and be assigned an entitlement. For information, see [`com.apple.developer.device-information.user-assigned-device-name`](../../BundleResources/entitlements/com.apple.developer.device-information.user-assigned-device-name.md).

> **Related Sessions from WWDC22**:  Session 10096: [What’s new in privacy](https://developer.apple.com/videos/play/wwdc2022/10096)
>
> Session 10068: [What’s new in UIKit](https://developer.apple.com/videos/play/wwdc2022/10068)

## See Also

### Identifying the device and operating system
- [var systemName: String](./systemname.md)
  The name of the operating system running on the device.
- [var systemVersion: String](./systemversion.md)
  The current version of the operating system.
- [var model: String](./model.md)
  The model of the device.
- [var localizedModel: String](./localizedmodel.md)
  The model of the device as a localized string.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](./userinterfaceidiom.md)
  The style of interface to use on the current device.
- [var identifierForVendor: UUID?](./identifierforvendor.md)
  An alphanumeric string that uniquely identifies a device to the app’s vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/name)*