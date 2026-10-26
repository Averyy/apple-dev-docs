# delegate

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The picker’s delegate object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency weak var delegate: (any PHPickerViewControllerDelegate)? { get set }
```

## See Also

### Responding to user selection
- [protocol PHPickerViewControllerDelegate](../phpickerviewcontrollerdelegate-5yntc.md)
  A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.
- [struct PHPickerResult](../phpickerresult-swift.struct.md)
  Types that represent a selected asset from a person’s photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerviewcontroller/delegate-3zqmt)*