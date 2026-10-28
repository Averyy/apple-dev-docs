# isSelected

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the button is in a selected state.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var isSelected: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isSelected) BOOL selected;
```

## Discussion

When this property is set to [`true`](../../Swift/true.md), CarPlay draws the button with a selected appearance to indicate its selected state. You can only update this property manually on instances of [`CPNowPlayingImageButton`](../cpnowplayingimagebutton.md). All system-provided buttons—for example, [`CPNowPlayingShuffleButton`](../cpnowplayingshufflebutton.md) or [`CPNowPlayingRepeatButton`](../cpnowplayingrepeatbutton.md)—manage their own selected states internally.

The default value is [`false`](../../Swift/false.md).

## See Also

### Managing the Button State
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the button is in an enabled state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingbutton/isselected)*