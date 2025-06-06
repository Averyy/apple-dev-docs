# playerViewController(_:didSelect:in:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate when the user selects a media option from a media selection group.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, didSelect mediaSelectionOption: AVMediaSelectionOption?, in mediaSelectionGroup: AVMediaSelectionGroup)
```

## Parameters

- `playerViewController`: The player view controller.
- `mediaSelectionOption`: The user’s selected media option, which may be  .
- `mediaSelectionGroup`: The media selection group in which the selected media option exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:didselect:in:))*