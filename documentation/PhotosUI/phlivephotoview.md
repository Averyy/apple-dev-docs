# PHLivePhotoView

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

A view that displays a Live Photo.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHLivePhotoView
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface PHLivePhotoView : UIView
```

*macOS*

```objc
@interface PHLivePhotoView : NSView
```

## Mentions

- [Displaying Live Photos](../PhotoKit/displaying-live-photos.md)

#### Overview

Use a Live Photo view to display the photo and control playback of its motion and sound content. In iOS and tvOS, you can obtain Live Photo objects from the Photos library, using the [`PHPickerViewController`](./phpickerviewcontroller.md) or [`PHAsset`](../Photos/phasset.md) and [`PHImageManager`](../Photos/phimagemanager.md) classes, or by creating one from asset resources exported from a Photos library. In macOS, Live Photo objects are available only when editing Live Photo content in a photo editing extension that runs in the Photos app—see the [`PHContentEditingInput`](../Photos/phcontenteditinginput.md) class to access Live Photo content in an editing session.

By default, a Live Photo view uses its own gesture recognizer to allow the user to play the motion and sound content of a Live Photo with the same interactions and visual effects seen in the Photos app. To customize this gesture recognizer—for example, to install it on a different view for proper event handling in your app’s view hierarchy—use the [`playbackGestureRecognizer`](./phlivephotoview/playbackgesturerecognizer.md) property.

To animate the view briefly to hint that a picture is a Live Photo, use the [`startPlayback(with:)`](./phlivephotoview/startplayback%28with%29.md) method with the [`PHLivePhotoViewPlaybackStyle.hint`](./phlivephotoviewplaybackstyle/hint.md) option.

> 💡 **Tip**:  This class displays Live Photos in native iOS and tvOS apps and macOS photo editing extensions. To display Live Photo content on the web, use the [LivePhotosKit JS](../LivePhotosKitJS/LivePhotosKitJS.md) framework.

## Topics

### Choosing a Live Photo to Display
- [var livePhoto: PHLivePhoto?](./phlivephotoview/livephoto.md)
  The Live Photo displayed in the view.
### Managing Playback
- [var playbackGestureRecognizer: UIGestureRecognizer](./phlivephotoview/playbackgesturerecognizer.md)
  A gesture recognizer that controls playback of the Live Photo in the view.
- [var isMuted: Bool](./phlivephotoview/ismuted.md)
  A Boolean value that determines whether the view plays the audio content of its Live Photo.
- [var audioVolume: Float](./phlivephotoview/audiovolume.md)
  The audio gain to apply to the Live Photo’s movie content during playback.
### Responding to Playback Events
- [var delegate: (any PHLivePhotoViewDelegate)?](./phlivephotoview/delegate.md)
  An object to be notified when Live Photo playback begins or ends.
- [protocol PHLivePhotoViewDelegate](./phlivephotoviewdelegate.md)
  The [`PHLivePhotoViewDelegate`](./phlivephotoviewdelegate.md) protocol describes messages sent by a [`PHLivePhotoView`](./phlivephotoview.md) instance in response to playback events when playing the motion and sound content associated with a Live Photo. To receive these messages, implement the methods in this protocol in one of your controller objects and assign that object to the [`delegate`](./phlivephotoview/delegate.md) property of a Live Photo view.
### Manually Playing Live Photo Content
- [func startPlayback(with: PHLivePhotoViewPlaybackStyle)](./phlivephotoview/startplayback%28with%29.md)
  Begins playback of Live Photo content in the view.
- [func stopPlayback()](./phlivephotoview/stopplayback%28%29.md)
  Stops playback of a Live Photo.
- [func stopPlayback(animated: Bool)](./phlivephotoview/stopplayback%28animated%29.md)
  Stops playback of a Live Photo in an animated manner.
### Accessing User Interface Icons for Live Photos
- [class func livePhotoBadgeImage(options: PHLivePhotoBadgeOptions) -> UIImage](./phlivephotoview/livephotobadgeimage%28options%29.md)
  Returns an icon image for the specified Live Photo semantic options.
- [var livePhotoBadgeView: NSView?](./phlivephotoview/livephotobadgeview.md)
  A view for displaying Live Photo status.
### Setting the Content Mode
- [var contentMode: PHLivePhotoViewContentMode](./phlivephotoview/contentmode.md)
  The mode in which the view displays its content.
- [enum PHLivePhotoViewContentMode](./phlivephotoviewcontentmode.md)
  The enumerated Live Photo content modes.
### Constants
- [enum PHLivePhotoViewPlaybackStyle](./phlivephotoviewplaybackstyle.md)
  Options for how much of the motion and sound content of a Live Photo to play, used in the [`startPlayback(with:)`](./phlivephotoview/startplayback%28with%29.md) method and in messages to the view’s [`delegate`](./phlivephotoview/delegate.md) object.
- [struct PHLivePhotoBadgeOptions](./phlivephotobadgeoptions.md)
  Options for the semantic use and display style of icons for badging Live Photo assets, used by the [`livePhotoBadgeImage(options:)`](./phlivephotoview/livephotobadgeimage%28options%29.md) method.
### Instance Properties
- [var contentsRect: CGRect](./phlivephotoview/contentsrect.md)
- [var intrinsicContentSize: CGSize](./phlivephotoview/intrinsiccontentsize.md)

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Shared photo library
- [Delivering an Enhanced Privacy Experience in Your Photos App](../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)
  Adopt the latest privacy enhancements to deliver advanced user-privacy controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phlivephotoview)*