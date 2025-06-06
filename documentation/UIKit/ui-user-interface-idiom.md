# UI_USER_INTERFACE_IDIOM()

**Framework**: UIKit  
**Kind**: func

Returns the interface idiom supported by the current device (recommended for apps that run in versions of iOS earlier than 3.2).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 9.0+

## Declaration

```swift
func UI_USER_INTERFACE_IDIOM() -> UIUserInterfaceIdiom
```

#### Return Value

[`UIUserInterfaceIdiom.phone`](uiuserinterfaceidiom/phone.md) if the device is an iPhone or iPod touch or [`UIUserInterfaceIdiom.pad`](uiuserinterfaceidiom/pad.md) if the device is an iPad.

## See Also

- [enum UIUserInterfaceIdiom](uiuserinterfaceidiom.md)
  Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/ui_user_interface_idiom())*