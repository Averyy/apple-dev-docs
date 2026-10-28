# picker(_:didFinishPicking:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when the user completes a selection or dismisses `PHPickerViewController` using the cancel button.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult])
```

## Discussion

The picker won’t be automatically dismissed when this method is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerviewcontrollerdelegate-5yntc/picker(_:didfinishpicking:))*