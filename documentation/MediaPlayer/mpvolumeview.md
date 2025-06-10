# MPVolumeView

**Framework**: Media Player  
**Kind**: class

A slider control for setting the system audio output volume, and a button for choosing the audio output route.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class MPVolumeView
```

#### Overview

Use a volume view to present the user with a slider control for setting the system audio output volume, and a button for choosing the audio output route when the option is available. When first displayed, the slider’s position reflects the current system audio output volume. As the user drags the slider, the changes update the volume view. If the user presses the device volume buttons while sound is playing, the slider moves to reflect the new volume.

If there’s an Apple TV or other AirPlay-enabled device in range, the route button allows the user to choose it. If there’s only one audio output route available, the view doesn’t display the route button. The view also doesn’t display a route button when the app runs in visionOS.

> ❗ **Important**:  You can’t change the volume or choose a route with this class while testing in the Simulator. These abilities only work on a device.

Use this class by embedding an instance of it in your view hierarchy. The following code snippet assumes you’ve placed an instance of the [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) class on a view using Interface Builder, sizing and positioning it as desired to contain the volume view. Point to the [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) instance with an outlet variable—named, in the case of this example, `mpVolumeViewParentView`. You’d typically place code like that shown in the following code in your `viewDidLoad` method.

Listing 1. Adding a volume view to your view hierarchy

```swift
parentView.backgroundColor = .clear
let volumeView = MPVolumeView(frame: parentView.bounds)
parentView.addSubview(volumeView)
```

When an audio output route that doesn’t support volume control, such as a car head unit, is active, the system replaces the volume slider with the route name.

To instead display a volume slider as an alert, use the functions described in [`Global volume setting methods`](global-volume-setting-methods.md).

> **Note**:  You can’t subclass the MPVolumeView class.

##### Customizing the Volume Sliders Appearance

The volume slider is a [`UISlider`](https://developer.apple.com/documentation/UIKit/UISlider) object. Sliders are always displayed as horizontal bars and an indicator, or , notes the current value of the slider, which the user can move to change the setting.

Slider controls draw the volume slider track using two distinct images, which are customizable. The system draws the region between the thumb and the end of the track associated with the slider’s minimum value using the . The system region between the thumb and the end of the track associated with the slider’s maximum value using the . You can assign different images to customize the appearance of the slider for its various states, such as enabled, disabled, and highlighted.

You can also customize the volume thumb image for the slider.

> **Note**:  The volume slider control provides a set of default images for both the track and thumb. The system uses the default images if you don’t specify any custom images.

## Topics

### Managing visibility of controls
- [var showsVolumeSlider: Bool](mpvolumeview/showsvolumeslider.md)
  A Boolean value that indicates the volume slider is visible in the volume view.
### Customizing the volume slider
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
- [func volumeThumbRect(forBounds: CGRect, volumeSliderRect: CGRect, value: Float) -> CGRect](mpvolumeview/volumethumbrect(forbounds:volumesliderrect:value:).md)
  Returns the drawing rectangle for the volume slider’s thumb image.
### Deprecated
- [var volumeWarningSliderImage: UIImage?](mpvolumeview/volumewarningsliderimage.md)
  The image used to designate the European Union volume limit.
- [var showsRouteButton: Bool](mpvolumeview/showsroutebutton.md)
  A Boolean value that indicates whether the route button is visible in the volume view.
- [var areWirelessRoutesAvailable: Bool](mpvolumeview/arewirelessroutesavailable.md)
  A Boolean value indicating wireless routes are available.
- [var isWirelessRouteActive: Bool](mpvolumeview/iswirelessrouteactive.md)
  A Boolean value that indicates whether the wireless route is active.
- [func routeButtonImage(for: UIControl.State) -> UIImage?](mpvolumeview/routebuttonimage(for:).md)
  Returns the button image associated with the specified control state.
- [func routeButtonRect(forBounds: CGRect) -> CGRect](mpvolumeview/routebuttonrect(forbounds:).md)
  Returns the drawing rectangle for the route button.
- [func setRouteButtonImage(UIImage?, for: UIControl.State)](mpvolumeview/setroutebuttonimage(_:for:).md)
  Assigns a button image to the specified control states.

## Relationships

### Inherits From
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Displaying a media picker from your app](displaying-a-media-picker-from-your-app.md)
  Let users choose the music they want to play by displaying a media picker interface from within your app.
- [class MPMediaPickerController](mpmediapickercontroller.md)
  A specialized view controller that provides a graphical interface for selecting media items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview)*