# updateNowPlayingButtons(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Updates the app-specific playback controls that appear in the lower region of the Now Playing interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func updateNowPlayingButtons(_ nowPlayingButtons: [CPNowPlayingButton])
```

```objc
- (void) updateNowPlayingButtons:(NSArray<__kindof CPNowPlayingButton *> *) nowPlayingButtons;
```

## Discussion

The template arranges the buttons in the same order as they appear in the array, starting from the leading edge of the interface.

## Parameters

- `nowPlayingButtons`: The array of buttons to display. Specify a maximum of five buttons in this array, and specify the buttons in the order you want them to appear.

## See Also

### Adding app-specific controls
- [var nowPlayingButtons: [CPNowPlayingButton]](./nowplayingbuttons.md)
  Additional app-specific playback controls to display in the lower region of the Now Playing interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingtemplate/updatenowplayingbuttons(_:))*