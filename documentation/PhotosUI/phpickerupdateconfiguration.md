# PHPickerUpdateConfiguration

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

An object that defines the aspects of a photo picker’s appearance that can change while it’s presented.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@interface PHPickerUpdateConfiguration : NSObject
```

## Overview

While a photos picker is visible, you can use an instance of this object to change its [`edgesWithoutContentMargins`](./phpickerconfiguration-c.class/edgeswithoutcontentmargins.md) or [`selectionLimit`](./phpickerconfiguration-swift.struct/selectionlimit.md) properties. To do that, create and configure an instance of this object and pass it to the [`PHPickerViewController`](./phpickerviewcontroller.md) method [`updatePickerUsingConfiguration:`](./phpickerviewcontroller/updatepickerusingconfiguration_.md).

## Topics

### Adjusting selection limits
- [selectionLimit](./phpickerupdateconfiguration/selectionlimit.md)
  The maximum number of selections the user can make.
### Adjusting content margins
- [edgesWithoutContentMargins](./phpickerupdateconfiguration/edgeswithoutcontentmargins.md)
  The portions of a photo picker’s permiter that are borderless.
### Instance Properties
- [searchText](./phpickerupdateconfiguration/searchtext.md)
  The search text for the picker.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Customizing picker appearance and behavior
- [mode](./phpickerconfiguration-c.class/mode.md)
  A layout type for the photos in the picker’s view.
- [PHPickerMode](./phpickermode-c.enum.md)
  Layout options that determine how the picker orders photos visually.
- [disabledCapabilities](./phpickerconfiguration-c.class/disabledcapabilities.md)
  The aspects of a photo picker’s default appearance that your app can disable.
- [struct PHPickerCapabilities](./phpickercapabilities.md)
  Options that customize the look and behavior of the photos picker.
- [edgesWithoutContentMargins](./phpickerconfiguration-c.class/edgeswithoutcontentmargins.md)
  The portions of a photo picker’s perimeter that are borderless.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerupdateconfiguration)*