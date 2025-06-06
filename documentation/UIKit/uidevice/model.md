# model

**Framework**: UIKit  
**Kind**: property

The model of the device.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var model: String { get }
```

#### Discussion

Possible examples of model strings are “iPhone” and “iPod touch”.

## See Also

- [var name: String](uidevice/name.md)
  The name of the device.
- [var systemName: String](uidevice/systemname.md)
  The name of the operating system running on the device.
- [var systemVersion: String](uidevice/systemversion.md)
  The current version of the operating system.
- [var localizedModel: String](uidevice/localizedmodel.md)
  The model of the device as a localized string.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](uidevice/userinterfaceidiom.md)
  The style of interface to use on the current device.
- [var identifierForVendor: UUID?](uidevice/identifierforvendor.md)
  An alphanumeric string that uniquely identifies a device to the app’s vendor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidevice/model)*