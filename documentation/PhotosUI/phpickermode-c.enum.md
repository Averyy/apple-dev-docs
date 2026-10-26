# PHPickerMode

**Framework**: PhotosUI  
**Kind**: enum  
**Role**: Enumeration

Layout options that determine how the picker orders photos visually.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```c
enum PHPickerMode : NSInteger;
```

#### Overview

This structure defines the possible options for the photos picker configuration ([`PHPickerConfiguration`](./phpickerconfiguration-c.class.md)) property [`mode`](./phpickerconfiguration-swift.struct/mode.md). The option you choose determines the direction that its assets scroll in the view. In addition, the linear scrolling behavior of [`compact`](./phpickermode-swift.struct/compact.md) mode offers the best user experience in a space-constrained layout.

## Topics

### Laying out photos
- [PHPickerModeCompact](./phpickermode-c.enum/phpickermodecompact.md)
  A linear layout that’s conducive to a smaller area onscreen.
- [PHPickerModeDefault](./phpickermode-c.enum/phpickermodedefault.md)
  A grid-based layout that’s conducive to a larger area onscreen.

## See Also

### Customizing picker appearance and behavior
- [mode](./phpickerconfiguration-c.class/mode.md)
  A layout type for the photos in the picker’s view.
- [disabledCapabilities](./phpickerconfiguration-c.class/disabledcapabilities.md)
  The aspects of a photo picker’s default appearance that your app can disable.
- [struct PHPickerCapabilities](./phpickercapabilities.md)
  Options that customize the look and behavior of the photos picker.
- [edgesWithoutContentMargins](./phpickerconfiguration-c.class/edgeswithoutcontentmargins.md)
  The portions of a photo picker’s perimeter that are borderless.
- [PHPickerUpdateConfiguration](./phpickerupdateconfiguration.md)
  An object that defines the aspects of a photo picker’s appearance that can change while it’s presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickermode-c.enum)*