# userInterfaceIdiom

**Framework**: UIKit  
**Kind**: property

The style of interface to use on the current device.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var userInterfaceIdiom: UIUserInterfaceIdiom { get }
```

#### Discussion

For universal applications, you can use this property to tailor the behavior of your application for a specific type of device. For example, iPhone and iPad devices have different screen sizes, so you might want to create different views and controls based on the type of the current device.

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
- [var identifierForVendor: UUID?](uidevice/identifierforvendor.md)
  An alphanumeric string that uniquely identifies a device to the app’s vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/userinterfaceidiom)*