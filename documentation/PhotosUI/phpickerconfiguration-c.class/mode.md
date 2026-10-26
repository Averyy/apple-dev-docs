# mode

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

A layout type for the photos in the picker’s view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic) PHPickerMode mode;
```

#### Discussion

This property offers two ways that photos lay out in the picker:

- A linear mode ([`PHPickerModeCompact`](../phpickermode-c.enum/phpickermodecompact.md)), in which photos form a line in a smaller area in the picker
- A two-dimensional mode ([`PHPickerModeDefault`](../phpickermode-c.enum/phpickermodedefault.md)), in which photos form a grid in a larger area in the picker

## See Also

### Customizing picker appearance and behavior
- [PHPickerMode](../phpickermode-c.enum.md)
  Layout options that determine how the picker orders photos visually.
- [disabledCapabilities](./disabledcapabilities.md)
  The aspects of a photo picker’s default appearance that your app can disable.
- [struct PHPickerCapabilities](../phpickercapabilities.md)
  Options that customize the look and behavior of the photos picker.
- [edgesWithoutContentMargins](./edgeswithoutcontentmargins.md)
  The portions of a photo picker’s perimeter that are borderless.
- [PHPickerUpdateConfiguration](../phpickerupdateconfiguration.md)
  An object that defines the aspects of a photo picker’s appearance that can change while it’s presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfiguration-c.class/mode)*