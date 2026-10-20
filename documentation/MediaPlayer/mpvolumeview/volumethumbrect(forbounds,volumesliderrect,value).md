# volumeThumbRect(forBounds:volumeSliderRect:value:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Returns the drawing rectangle for the volume slider’s thumb image.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func volumeThumbRect(forBounds bounds: CGRect, volumeSliderRect rect: CGRect, value: Float) -> CGRect
```

```objc
- (CGRect) volumeThumbRectForBounds:(CGRect) bounds volumeSliderRect:(CGRect) rect value:(float) value;
```

#### Return Value

The computed drawing rectangle for the thumb image.

#### Discussion

The rectangle you return should reflect the size of your thumb image and its current position on the slider’s track.

## Parameters

- `bounds`: The bounding rectangle of the thumb image.
- `rect`: The drawing rectangle for the receiver’s track, as returned by the [`volumeSliderRect(forBounds:)`](./volumesliderrect%28forbounds%29.md) method.
- `value`: The current value of the volume slider.

## See Also

### Customizing the volume slider
- [func maximumVolumeSliderImage(for: UIControl.State) -> UIImage?](./maximumvolumesliderimage%28for%29.md)
  Returns the maximum volume image associated with the specified control state.
- [func minimumVolumeSliderImage(for: UIControl.State) -> UIImage?](./minimumvolumesliderimage%28for%29.md)
  Returns the minimum volume image associated with the specified control state.
- [func setMaximumVolumeSliderImage(UIImage?, for: UIControl.State)](./setmaximumvolumesliderimage%28_,for%29.md)
  Assigns a maximum volume slider image to the specified control states.
- [func setMinimumVolumeSliderImage(UIImage?, for: UIControl.State)](./setminimumvolumesliderimage%28_,for%29.md)
  Assigns a minimum volume slider image to the specified control states.
- [func setVolumeThumbImage(UIImage?, for: UIControl.State)](./setvolumethumbimage%28_,for%29.md)
  Assigns a thumb image to the specified control states.
- [func volumeSliderRect(forBounds: CGRect) -> CGRect](./volumesliderrect%28forbounds%29.md)
  Returns the drawing rectangle for the slider’s track.
- [func volumeThumbImage(for: UIControl.State) -> UIImage?](./volumethumbimage%28for%29.md)
  Returns the thumb image associated with the specified control state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/volumethumbrect(forbounds:volumesliderrect:value:))*