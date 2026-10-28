# minimumVolumeSliderImage(for:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Returns the minimum volume image associated with the specified control state.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func minimumVolumeSliderImage(for state: UIControl.State) -> UIImage?
```

```objc
- (UIImage *) minimumVolumeSliderImageForState:(UIControlState) state;
```

## Return Value

The maximum volume image associated with the specified state, or [`nil`](../../ObjectiveC/nil-227m0.md) if an appropriate image could not be retrieved. This method might return [`nil`](../../ObjectiveC/nil-227m0.md) if you specify multiple control states in the `state` parameter.

## Discussion

For a description of slider and thumb images, see [Customizing the volume slider’s appearance](../mpvolumeview.md#Customizing-the-volume-sliders-appearance).

## Parameters

- `state`: The control state whose minimum volume image you want. You should specify only one control state value for this parameter.

## See Also

### Customizing the volume slider
- [func maximumVolumeSliderImage(for: UIControl.State) -> UIImage?](./maximumvolumesliderimage%28for%29.md)
  Returns the maximum volume image associated with the specified control state.
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
- [func volumeThumbRect(forBounds: CGRect, volumeSliderRect: CGRect, value: Float) -> CGRect](./volumethumbrect%28forbounds,volumesliderrect,value%29.md)
  Returns the drawing rectangle for the volume slider’s thumb image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/minimumvolumesliderimage(for:))*