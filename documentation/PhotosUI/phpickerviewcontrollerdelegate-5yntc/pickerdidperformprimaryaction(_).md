# pickerDidPerformPrimaryAction(_:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when the user taps the primary button.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func pickerDidPerformPrimaryAction(_ picker: PHPickerViewController)
```

## Discussion

The picker won’t be automatically dismissed when this method is called.

## Default Implementations

### PHPickerViewControllerDelegate Implementations
- [func pickerDidPerformPrimaryAction(PHPickerViewController)](./pickerdidperformprimaryaction%28_%29-2knz4.md)
  Called when the user taps the primary button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerviewcontrollerdelegate-5yntc/pickerdidperformprimaryaction(_:))*