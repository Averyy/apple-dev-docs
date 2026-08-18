# MPMediaPickerController

**Framework**: Media Player  
**Kind**: class

A specialized view controller that provides a graphical interface for selecting media items.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MPMediaPickerController
```

#### Overview

An [`MPMediaPickerController`](mpmediapickercontroller.md) object, or media item picker, is a specialized view controller that you employ to provide a graphical interface for selecting media items. To display a media item picker, present it modally on an existing view controller. Presenting an [`MPMediaPickerController`](mpmediapickercontroller.md) in non-modal mode; for example, pushing a [`MPMediaPickerController`](mpmediapickercontroller.md) onto an existing [`UINavigationController`](https://developer.apple.com/documentation/uikit/uinavigationcontroller) stack causes your app to crash. [`MPMediaItem`](mpmediaitem.md) describes media items.

To respond to user selections and to dismiss a media item picker, use the [`MPMediaPickerControllerDelegate`](mpmediapickercontrollerdelegate.md) protocol.

> **Note**:  The [`MPMediaPickerController`](mpmediapickercontroller.md) class supports portrait mode only. This class doesn’t support subclassing, and don’t modify the view hierarchy, which is private. In a compatible iPad or iPhone app in visionOS, presenting this picker displays an alert notifying the person that picking media items isn’t supported.

## Topics

### Initializing a media item picker
- [init(mediaTypes: MPMediaType)](mpmediapickercontroller/init(mediatypes:).md)
  Initializes a media item picker for specified media types.
### Responding to media item picker selections
- [var delegate: (any MPMediaPickerControllerDelegate)?](mpmediapickercontroller/delegate.md)
  The delegate for a media item picker.
- [protocol MPMediaPickerControllerDelegate](mpmediapickercontrollerdelegate.md)
  The protocol you implement so that a media item picker can respond to a user making media item selections.
### Using a media item picker
- [var allowsPickingMultipleItems: Bool](mpmediapickercontroller/allowspickingmultipleitems.md)
  A Boolean value specifying the default selection behavior for a media item picker.
- [var showsCloudItems: Bool](mpmediapickercontroller/showsclouditems.md)
  A Boolean value specifying whether to display iCloud Media Library items for a media picker.
- [var mediaTypes: MPMediaType](mpmediapickercontroller/mediatypes.md)
  The media types that media item picker presents.
- [var prompt: String?](mpmediapickercontroller/prompt.md)
  A prompt, for the user, that appears above the navigation bar buttons.
- [var showsItemsWithProtectedAssets: Bool](mpmediapickercontroller/showsitemswithprotectedassets.md)
  A Boolean value that specifies whether the media item picker displays protected assets.

## Relationships

### Inherits From
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [Displaying a media picker from your app](displaying-a-media-picker-from-your-app.md)
  Let users choose the music they want to play by displaying a media picker interface from within your app.
- [class MPVolumeView](mpvolumeview.md)
  A slider control for setting the system audio output volume, and a button for choosing the audio output route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller)*