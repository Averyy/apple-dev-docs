# legibleMenuController(_:didChange:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
optional func legibleMenuController(_ menuController: AVLegibleMediaOptionsMenuController, didChange state: AVLegibleMediaOptionsMenuState)
```

```objc
- (void) legibleMenuController:(AVLegibleMediaOptionsMenuController *) menuController didChangeMenuState:(AVLegibleMediaOptionsMenuState) state;
```

#### Discussion

Tells the delegate, when legible media options menu state changes.

## Parameters

- `menuController`: The legible options menu controller.
- `state`: The new menu state.

## See Also

### Responding to menu changes
- [func legibleMenuController(AVLegibleMediaOptionsMenuController, didRequestCaptionPreviewForProfileID: String)](./legiblemenucontroller%28_,didrequestcaptionpreviewforprofileid%29.md)
- [func legibleMenuControllerDidRequestStoppingSubtitleCaptionPreview(AVLegibleMediaOptionsMenuController)](./legiblemenucontrollerdidrequeststoppingsubtitlecaptionpreview%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/delegate-swift.protocol/legiblemenucontroller(_:didchange:))*