# MPMediaPickerControllerDelegate

**Framework**: Media Player  
**Kind**: protocol

The protocol you implement so that a media item picker can respond to a user making media item selections.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

## Declaration

```swift
protocol MPMediaPickerControllerDelegate : NSObjectProtocol
```

## Mentions

- [Displaying a media picker from your app](displaying-a-media-picker-from-your-app.md)

#### Overview

The delegate for a media item picker can respond to a user making media item selections. The delegate is also responsible for dismissing the media item picker from the parent view controller. The methods in this protocol are optional.

[`MPMediaItem`](mpmediaitem.md) describes the media items and [`MPMediaPickerController`](mpmediapickercontroller.md) describes the media item pickers.

## Topics

### Responding to user actions
- [func mediaPicker(MPMediaPickerController, didPickMediaItems: MPMediaItemCollection)](mpmediapickercontrollerdelegate/mediapicker(_:didpickmediaitems:).md)
  A method that the system calls when a user selects a set of media items.
- [func mediaPickerDidCancel(MPMediaPickerController)](mpmediapickercontrollerdelegate/mediapickerdidcancel(_:).md)
  A method that the system calls when a user taps Cancel to dismiss a media item picker.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any MPMediaPickerControllerDelegate)?](mpmediapickercontroller/delegate.md)
  The delegate for a media item picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontrollerdelegate)*