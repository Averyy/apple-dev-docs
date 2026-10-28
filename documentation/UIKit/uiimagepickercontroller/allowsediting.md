# allowsEditing

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user is allowed to edit a selected still image or movie.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var allowsEditing: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsEditing;
```

## Discussion

If you allow the user to edit still images or movies, the delegate may receive a dictionary with information about the edits that were made. The protocol for the delegate is described in [`UIImagePickerControllerDelegate`](../uiimagepickercontrollerdelegate.md).

This property is set to [`false`](../../Swift/false.md) by default.

## See Also

### Configuring the picker
- [var mediaTypes: [String]](./mediatypes.md)
  An array that indicates the media types to access by the media picker controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/allowsediting)*