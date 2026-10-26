# PHPickerConfiguration.Update

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

An object that defines the aspects of a photo picker’s appearance that can change while it’s presented.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS

## Declaration

```swift
struct Update
```

#### Overview

While a photos picker is visible, you can use an instance of this structure to change its [`edgesWithoutContentMargins`](./edgeswithoutcontentmargins.md) or [`selectionLimit`](./selectionlimit.md) properties. To do that, create and configure an instance of this object and pass it to the [`PHPickerViewController`](../phpickerviewcontroller.md) method [`updatePicker(using:)`](../phpickerviewcontroller/updatepicker%28using%29.md).

## Topics

### Creating an update object
- [init()](./update/init%28%29.md)
### Adjusting selection limits
- [var selectionLimit: Int?](./update/selectionlimit.md)
  The maximum number of selections the user can make.
### Adjusting content margins
- [var edgesWithoutContentMargins: NSDirectionalRectEdge?](./update/edgeswithoutcontentmargins.md)
  The portions of a photo picker’s permiter that are borderless.
### Instance Properties
- [var searchText: PHPickerSearchText?](./update/searchtext.md)
  The search text for the picker. Default is `nil`.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing picker appearance and behavior
- [var mode: PHPickerMode](./mode.md)
  A layout type for the photos in the picker’s view.
- [struct PHPickerMode](../phpickermode-swift.struct.md)
  Layout options that determine how the picker orders photos visually.
- [var disabledCapabilities: PHPickerCapabilities](./disabledcapabilities.md)
  The aspects of a photo picker’s default appearance that your app can disable.
- [struct PHPickerCapabilities](../phpickercapabilities.md)
  Options that customize the look and behavior of the photos picker.
- [var edgesWithoutContentMargins: NSDirectionalRectEdge](./edgeswithoutcontentmargins.md)
  The portions of a photo picker’s perimeter that are borderless.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/update)*