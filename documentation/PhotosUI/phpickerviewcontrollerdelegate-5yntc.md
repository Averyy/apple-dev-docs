# PHPickerViewControllerDelegate

**Framework**: PhotosUI  
**Kind**: protocol  
**Role**: Protocol

A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency protocol PHPickerViewControllerDelegate : AnyObject
```

## Topics

### Instance Methods
- [func picker(PHPickerViewController, didFinishPicking: [PHPickerResult])](./phpickerviewcontrollerdelegate-5yntc/picker%28_,didfinishpicking%29.md)
  Called when the user completes a selection or dismisses `PHPickerViewController` using the cancel button.

## See Also

### Photos picker for UIKit, AppKit
- [Selecting Photos and Videos in iOS](../PhotoKit/selecting-photos-and-videos-in-ios.md)
  Improve the user experience of finding and selecting assets by using the Photos picker.
- [class PHPickerViewController](./phpickerviewcontroller.md)
  A view controller that provides the user interface for choosing assets from the photo library.
- [struct PHPickerConfiguration](./phpickerconfiguration-swift.struct.md)
  An object that contains information about how to configure a picker view controller.
- [struct PHPickerFilter](./phpickerfilter-swift.struct.md)
  A type that defines the filter to apply to the photo library.
- [struct PHPickerResult](./phpickerresult-swift.struct.md)
  Types that represent a selected asset from a person’s photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerviewcontrollerdelegate-5yntc)*