# delegate

**Framework**: Media Player  
**Kind**: property

The delegate for a media item picker.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
weak var delegate: (any MPMediaPickerControllerDelegate)? { get set }
```

#### Discussion

Typically, you set the delegate to be the same object that initializes and displays the media item picker.

## See Also

- [protocol MPMediaPickerControllerDelegate](mpmediapickercontrollerdelegate.md)
  The protocol you implement so that a media item picker can respond to a user making media item selections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/delegate)*