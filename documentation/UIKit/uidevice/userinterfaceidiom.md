# userInterfaceIdiom

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The style of interface to use on the current device.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var userInterfaceIdiom: UIUserInterfaceIdiom { get }
```

```objc
@property (nonatomic, readonly) UIUserInterfaceIdiom userInterfaceIdiom;
```

#### Discussion

For universal applications, you can use this property to tailor the behavior of your application for a specific type of device. For example, iPhone and iPad devices have different screen sizes, so you might want to create different views and controls based on the type of the current device.

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
- [var localizedModel: String](./localizedmodel.md)
  The model of the device as a localized string.
- [var identifierForVendor: UUID?](./identifierforvendor.md)
  An alphanumeric string that uniquely identifies a device to the app’s vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/userinterfaceidiom)*