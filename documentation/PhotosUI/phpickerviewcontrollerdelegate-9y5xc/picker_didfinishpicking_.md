# picker:didFinishPicking:

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that the user completed a selection or dismissed the picker using the cancel button.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```objc
- (void) picker:(PHPickerViewController *) picker didFinishPicking:(NSArray<PHPickerResult *> *) results;
```

## Discussion

The system doesn’t automatically dismiss the picker after calling this method.

## Parameters

- `picker`: The currently presented picker view controller.
- `results`: The results of the user’s selections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerviewcontrollerdelegate-9y5xc/picker:didfinishpicking:)*