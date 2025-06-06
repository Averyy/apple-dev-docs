# localizedModel

**Framework**: UIKit  
**Kind**: property

The model of the device as a localized string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var localizedModel: String { get }
```

#### Discussion

The value of this property is a string that contains a localized version of the string returned from [`model`](uidevice/model.md).

## See Also

- [var name: String](uidevice/name.md)
  The name of the device.
- [var systemName: String](uidevice/systemname.md)
  The name of the operating system running on the device.
- [var systemVersion: String](uidevice/systemversion.md)
  The current version of the operating system.
- [var model: String](uidevice/model.md)
  The model of the device.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](uidevice/userinterfaceidiom.md)
  The style of interface to use on the current device.
- [var identifierForVendor: UUID?](uidevice/identifierforvendor.md)
  An alphanumeric string that uniquely identifies a device to the app’s vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/localizedmodel)*