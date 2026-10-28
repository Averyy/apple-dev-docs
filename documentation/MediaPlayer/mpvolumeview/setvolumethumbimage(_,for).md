# setVolumeThumbImage(_:for:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Assigns a thumb image to the specified control states.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setVolumeThumbImage(_ image: UIImage?, for state: UIControl.State)
```

```objc
- (void) setVolumeThumbImage:(UIImage *) image forState:(UIControlState) state;
```

## Discussion

For a description of slider and thumb images, see [Customizing the volume slider’s appearance](../mpvolumeview.md#Customizing-the-volume-sliders-appearance).

## Parameters

- `image`: The thumb image to associate with the specified states.
- `state`: The control state with which to associate the image.

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
- [func volumeSliderRect(forBounds: CGRect) -> CGRect](./volumesliderrect%28forbounds%29.md)
  Returns the drawing rectangle for the slider’s track.
- [func volumeThumbImage(for: UIControl.State) -> UIImage?](./volumethumbimage%28for%29.md)
  Returns the thumb image associated with the specified control state.
- [func volumeThumbRect(forBounds: CGRect, volumeSliderRect: CGRect, value: Float) -> CGRect](./volumethumbrect%28forbounds,volumesliderrect,value%29.md)
  Returns the drawing rectangle for the volume slider’s thumb image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/setvolumethumbimage(_:for:))*