# playerViewController(_:didSelect:in:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user selects a media option from a media selection group.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, didSelect mediaSelectionOption: AVMediaSelectionOption?, in mediaSelectionGroup: AVMediaSelectionGroup)
```

```objc
- (void) playerViewController:(AVPlayerViewController *) playerViewController didSelectMediaSelectionOption:(AVMediaSelectionOption *) mediaSelectionOption inMediaSelectionGroup:(AVMediaSelectionGroup *) mediaSelectionGroup;
```

## Parameters

- `playerViewController`: The player view controller.
- `mediaSelectionOption`: The user’s selected media option, which may be `nil`.
- `mediaSelectionGroup`: The media selection group in which the selected media option exists.

## See Also

### Responding to media selection
- [- playerViewController:didSelectExternalSubtitleOptionLanguage:](./playerviewcontroller_didselectexternalsubtitleoptionlanguage_.md)
  Tells the delegate when the user selects a specific subtitle option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:didselect:in:))*