# playerViewController:didSelectExternalSubtitleOptionLanguage:

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the user selects a specific subtitle option.

**Availability**:
- tvOS 9.0+

## Declaration

```objc
- (void) playerViewController:(AVPlayerViewController *) playerViewController didSelectExternalSubtitleOptionLanguage:(NSString *) language;
```

#### Discussion

The framework calls this method only for external subtitle languages specified by the player item’s [`externalSubtitleOptionLanguages`](../../AVFoundation/avplayeritem/externalsubtitleoptionlanguages.md) property. For all other options, the framework calls [`playerViewController(_:didSelect:in:)`](./playerviewcontroller%28_,didselect,in%29.md) instead. The delegate is responsible for displaying the corresponding subtitles.

## Parameters

- `playerViewController`: The player view controller.
- `language`: The IETF BCP 47 language code.

## See Also

### Responding to media selection
- [func playerViewController(AVPlayerViewController, didSelect: AVMediaSelectionOption?, in: AVMediaSelectionGroup)](./playerviewcontroller%28_,didselect,in%29.md)
  Tells the delegate when the user selects a media option from a media selection group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller:didselectexternalsubtitleoptionlanguage:)*