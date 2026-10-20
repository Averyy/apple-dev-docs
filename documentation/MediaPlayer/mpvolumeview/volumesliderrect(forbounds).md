# volumeSliderRect(forBounds:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Returns the drawing rectangle for the slider’s track.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func volumeSliderRect(forBounds bounds: CGRect) -> CGRect
```

```objc
- (CGRect) volumeSliderRectForBounds:(CGRect) bounds;
```

#### Return Value

The computed drawing rectangle for the volume slider track. This rectangle corresponds to the entire length of the track between the minimum and maximum value images.

#### Discussion

The system uses the rectangle to scale the track and thumb images during drawing.

## Parameters

- `bounds`: The bounding rectangle of the receiver.

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
- [func volumeThumbImage(for: UIControl.State) -> UIImage?](./volumethumbimage%28for%29.md)
  Returns the thumb image associated with the specified control state.
- [func volumeThumbRect(forBounds: CGRect, volumeSliderRect: CGRect, value: Float) -> CGRect](./volumethumbrect%28forbounds,volumesliderrect,value%29.md)
  Returns the drawing rectangle for the volume slider’s thumb image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/volumesliderrect(forbounds:))*