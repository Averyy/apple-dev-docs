# localizedModel

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The model of the device as a localized string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var localizedModel: String { get }
```

```objc
@property (nonatomic, strong, readonly) NSString * localizedModel;
```

#### Discussion

The value of this property is a string that contains a localized version of the string returned from [`model`](./model.md).

## See Also

### Identifying the device and operating system
- [var name: String](./name.md)
  The name of the device.
- [var systemName: String](./systemname.md)
  The name of the operating system running on the device.
- [var systemVersion: String](./systemversion.md)
  The current version of the operating system.
- [var model: String](./model.md)
  The model of the device.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](./userinterfaceidiom.md)
  The style of interface to use on the current device.
- [var identifierForVendor: UUID?](./identifierforvendor.md)
  An alphanumeric string that uniquely identifies a device to the app’s vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/localizedmodel)*