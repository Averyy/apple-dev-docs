# isSelected

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates the selected state of a custom button.

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

Use this property in [`CPNowPlayingImageButton`](../cpnowplayingimagebutton.md) objects to change the selected state of your button. Setting this property to `true` draws the button with a selected appearance. Setting the property to `false` draws the button with its unselected appearance. The default value of this property is `false`.

> **Note**: You can’t change the selected state of system-provided button types such as [`CPNowPlayingShuffleButton`](../cpnowplayingshufflebutton.md) or [`CPNowPlayingRepeatButton`](../cpnowplayingrepeatbutton.md). Those buttons manage their own selected state and ignore any attempts to change this value.

## See Also

### Managing the button state
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the button is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingbutton/isselected)*