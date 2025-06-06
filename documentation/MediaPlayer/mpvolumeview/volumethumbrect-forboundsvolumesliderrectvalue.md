# volumeThumbRect(forBounds:volumeSliderRect:value:)

**Framework**: Media Player  
**Kind**: method

Returns the drawing rectangle for the volume slider’s thumb image.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func volumeThumbRect(forBounds bounds: CGRect, volumeSliderRect rect: CGRect, value: Float) -> CGRect
```

#### Return Value

The computed drawing rectangle for the thumb image.

#### Discussion

The rectangle you return should reflect the size of your thumb image and its current position on the slider’s track.

## Parameters

- `bounds`: The bounding rectangle of the thumb image.
- `rect`: The drawing rectangle for the receiver’s track, as returned by the   method.
- `value`: The current value of the volume slider.

## See Also

- [func maximumVolumeSliderImage(for: UIControl.State) -> UIImage?](mpvolumeview/maximumvolumesliderimage(for:).md)
  Returns the maximum volume image associated with the specified control state.
- [func minimumVolumeSliderImage(for: UIControl.State) -> UIImage?](mpvolumeview/minimumvolumesliderimage(for:).md)
  Returns the minimum volume image associated with the specified control state.
- [func setMaximumVolumeSliderImage(UIImage?, for: UIControl.State)](mpvolumeview/setmaximumvolumesliderimage(_:for:).md)
  Assigns a maximum volume slider image to the specified control states.
- [func setMinimumVolumeSliderImage(UIImage?, for: UIControl.State)](mpvolumeview/setminimumvolumesliderimage(_:for:).md)
  Assigns a minimum volume slider image to the specified control states.
- [func setVolumeThumbImage(UIImage?, for: UIControl.State)](mpvolumeview/setvolumethumbimage(_:for:).md)
  Assigns a thumb image to the specified control states.
- [func volumeSliderRect(forBounds: CGRect) -> CGRect](mpvolumeview/volumesliderrect(forbounds:).md)
  Returns the drawing rectangle for the slider’s track.
- [func volumeThumbImage(for: UIControl.State) -> UIImage?](mpvolumeview/volumethumbimage(for:).md)
  Returns the thumb image associated with the specified control state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/volumethumbrect(forbounds:volumesliderrect:value:))*