# PHPickerResult

**Framework**: PhotosUI  
**Kind**: struct  
**Role**: Structure

Types that represent a selected asset from a person’s photo library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
struct PHPickerResult
```

## Topics

### Inspecting the Result
- [var assetIdentifier: String?](./phpickerresult-swift.struct/assetidentifier.md)
  The local identifier of the selected asset.
- [let itemProvider: NSItemProvider](./phpickerresult-swift.struct/itemprovider.md)
  Representations of the selected asset.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Photos picker for UIKit, AppKit
- [Selecting Photos and Videos in iOS](../PhotoKit/selecting-photos-and-videos-in-ios.md)
  Improve the user experience of finding and selecting assets by using the Photos picker.
- [class PHPickerViewController](./phpickerviewcontroller.md)
  A view controller that provides the user interface for choosing assets from the photo library.
- [protocol PHPickerViewControllerDelegate](./phpickerviewcontrollerdelegate-5yntc.md)
  A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.
- [struct PHPickerConfiguration](./phpickerconfiguration-swift.struct.md)
  An object that contains information about how to configure a picker view controller.
- [struct PHPickerFilter](./phpickerfilter-swift.struct.md)
  A type that defines the filter to apply to the photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerresult-swift.struct)*