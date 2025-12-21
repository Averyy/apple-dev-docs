# isSelected

**Framework**: CarPlay  
**Kind**: property

A Boolean value that indicates whether the button is in a selected state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
var isSelected: Bool { get set }
```

#### Discussion

When this property is set to [`true`](https://developer.apple.com/documentation/Swift/true), CarPlay draws the button with a selected appearance to indicate its selected state. You can only update this property manually on instances of [`CPNowPlayingImageButton`](cpnowplayingimagebutton.md). All system-provided buttons—for example, [`CPNowPlayingShuffleButton`](cpnowplayingshufflebutton.md) or [`CPNowPlayingRepeatButton`](cpnowplayingrepeatbutton.md)—manage their own selected states internally.

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var isEnabled: Bool](cpnowplayingbutton/isenabled.md)
  A Boolean value that indicates whether the button is in an enabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingbutton/isselected)*