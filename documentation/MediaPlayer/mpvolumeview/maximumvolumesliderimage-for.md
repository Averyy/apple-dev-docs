# maximumVolumeSliderImage(for:)

**Framework**: Media Player  
**Kind**: method

Returns the maximum volume image associated with the specified control state.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func maximumVolumeSliderImage(for state: UIControl.State) -> UIImage?
```

#### Return Value

The maximum volume image associated with the specified state, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if an appropriate image could not be retrieved. This method might return [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if you specify multiple control states in the `state` parameter.

#### Discussion

For a description of slider and thumb images, see [`Customizing the volume slider’s appearance`](mpvolumeview#Customizing-the-volume-sliders-appearance.md).

## Parameters

- `state`: The control state whose maximum volume image you want. You should specify only one control state value for this parameter.

## See Also

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
- [func volumeThumbRect(forBounds: CGRect, volumeSliderRect: CGRect, value: Float) -> CGRect](mpvolumeview/volumethumbrect(forbounds:volumesliderrect:value:).md)
  Returns the drawing rectangle for the volume slider’s thumb image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/maximumvolumesliderimage(for:))*