# setMinimumVolumeSliderImage(_:for:)

**Framework**: Media Player  
**Kind**: method

Assigns a minimum volume slider image to the specified control states.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setMinimumVolumeSliderImage(_ image: UIImage?, for state: UIControl.State)
```

#### Discussion

The orientation of the track image must match the orientation of the slider control. To facilitate the stretching of the image to fill the space between the thumb and end point, track images are usually defined in three regions. A stretchable region sits between two end cap regions. The end caps define the portions of the image that remain as is and aren’t stretched. The stretchable region is a 1-point wide area between the end caps that the system can replicate to make the image appear longer.

To define the end cap sizes for a slider, assign an appropriate value to the image’s [`capInsets`](https://developer.apple.com/documentation/UIKit/UIImage/capInsets) property. For more information about how this value defines the regions of the slider, see the [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage).

For a description of slider and thumb images, see [`Customizing the volume slider’s appearance`](mpvolumeview#Customizing-the-volume-sliders-appearance.md).

## Parameters

- `image`: The minimum volume slider image to associate with the specified states.
- `state`: The control state with which to associate the image.

## See Also

- [func maximumVolumeSliderImage(for: UIControl.State) -> UIImage?](mpvolumeview/maximumvolumesliderimage(for:).md)
  Returns the maximum volume image associated with the specified control state.
- [func minimumVolumeSliderImage(for: UIControl.State) -> UIImage?](mpvolumeview/minimumvolumesliderimage(for:).md)
  Returns the minimum volume image associated with the specified control state.
- [func setMaximumVolumeSliderImage(UIImage?, for: UIControl.State)](mpvolumeview/setmaximumvolumesliderimage(_:for:).md)
  Assigns a maximum volume slider image to the specified control states.
- [func setVolumeThumbImage(UIImage?, for: UIControl.State)](mpvolumeview/setvolumethumbimage(_:for:).md)
  Assigns a thumb image to the specified control states.
- [func volumeSliderRect(forBounds: CGRect) -> CGRect](mpvolumeview/volumesliderrect(forbounds:).md)
  Returns the drawing rectangle for the slider’s track.
- [func volumeThumbImage(for: UIControl.State) -> UIImage?](mpvolumeview/volumethumbimage(for:).md)
  Returns the thumb image associated with the specified control state.
- [func volumeThumbRect(forBounds: CGRect, volumeSliderRect: CGRect, value: Float) -> CGRect](mpvolumeview/volumethumbrect(forbounds:volumesliderrect:value:).md)
  Returns the drawing rectangle for the volume slider’s thumb image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/setminimumvolumesliderimage(_:for:))*