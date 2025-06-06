# allowsEditing

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the user is allowed to edit a selected still image or movie.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsEditing: Bool { get set }
```

#### Discussion

If you allow the user to edit still images or movies, the delegate may receive a dictionary with information about the edits that were made. The protocol for the delegate is described in [`UIImagePickerControllerDelegate`](uiimagepickercontrollerdelegate.md).

This property is set to [`false`](https://developer.apple.com/documentation/swift/false) by default.

## See Also

- [var mediaTypes: [String]](uiimagepickercontroller/mediatypes.md)
  An array that indicates the media types to access by the media picker controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/allowsediting)*