# UI_USER_INTERFACE_IDIOM()

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Returns the interface idiom supported by the current device (recommended for apps that run in versions of iOS earlier than 3.2).

**Availability**:
- iOS 2.0+ - Deprecated in 13.0
- iPadOS 2.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 9.0+ - Deprecated in 11.0

> **Deprecated**: If your app runs in iOS 3.2 and later, use [`userInterfaceIdiom`](./uidevice/userinterfaceidiom.md) instead.

## Declaration

```swift
func UI_USER_INTERFACE_IDIOM() -> UIUserInterfaceIdiom
```

```c
static UIUserInterfaceIdiom UI_USER_INTERFACE_IDIOM();
```

## Return Value

[`UIUserInterfaceIdiom.phone`](./uiuserinterfaceidiom/phone.md) if the device is an iPhone or iPod touch or [`UIUserInterfaceIdiom.pad`](./uiuserinterfaceidiom/pad.md) if the device is an iPad.

## See Also

### Getting the current idiom
- [enum UIUserInterfaceIdiom](./uiuserinterfaceidiom.md)
  Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/ui_user_interface_idiom())*