# systemVersion

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current version of the operating system.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var systemVersion: String { get }
```

```objc
@property (nonatomic, strong, readonly) NSString * systemVersion;
```

## Discussion

An example of the system version is @“1.2”.

## See Also

### Identifying the device and operating system
- [var name: String](./name.md)
  The name of the device.
- [var systemName: String](./systemname.md)
  The name of the operating system running on the device.
- [var model: String](./model.md)
  The model of the device.
- [var localizedModel: String](./localizedmodel.md)
  The model of the device as a localized string.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](./userinterfaceidiom.md)
  The style of interface to use on the current device.
- [var identifierForVendor: UUID?](./identifierforvendor.md)
  An alphanumeric string that uniquely identifies a device to the app’s vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/systemversion)*