# mediaPicker(_:didPickMediaItems:)

**Framework**: Media Player  
**Kind**: method

A method that the system calls when a user selects a set of media items.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func mediaPicker(_ mediaPicker: MPMediaPickerController, didPickMediaItems mediaItemCollection: MPMediaItemCollection)
```

## Mentions

- [Displaying a media picker from your app](displaying-a-media-picker-from-your-app.md)

## Parameters

- `mediaPicker`: The media item picker to dismiss.
- `mediaItemCollection`: The selected media items.

## See Also

- [iPod Library Access Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Audio/Conceptual/iPodLibraryAccess_Guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008765)
- [func mediaPickerDidCancel(MPMediaPickerController)](mpmediapickercontrollerdelegate/mediapickerdidcancel(_:).md)
  A method that the system calls when a user taps Cancel to dismiss a media item picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontrollerdelegate/mediapicker(_:didpickmediaitems:))*