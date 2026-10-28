# CPNowPlayingImageButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A button that displays an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPNowPlayingImageButton
```

```objc
@interface CPNowPlayingImageButton : CPNowPlayingButton
```

## Overview

`CPNowPlayingImageButton` is a concrete subclass of [`CPNowPlayingButton`](./cpnowplayingbutton.md). Use this class when you want to display a button that contains an image.

In iOS 17 and later, CarPlay retints the custom now playing image buttons your app provides; you need to provide images  as monocolor assets.

CarPlay doesn’t support animated images. If you provide an animated image, CarPlay uses only the first image in the animation sequence.

To properly size your image, use the display scale of the vehicle’s primary screen—see your interface controller’s [`carTraitCollection`](./cpinterfacecontroller/cartraitcollection.md) property—and make sure it is no larger than [`CPNowPlayingButtonMaximumImageSize`](./cpnowplayingbuttonmaximumimagesize.md).

## Topics

### Creating a Button
- [init(image: UIImage, handler: ((CPNowPlayingButton) -> Void)?)](./cpnowplayingimagebutton/init%28image,handler%29.md)
  Creates a Now Playing button that displays a custom image and invokes a handler.
- [let CPNowPlayingButtonMaximumImageSize: CGSize](./cpnowplayingbuttonmaximumimagesize.md)
  The maximum size CarPlay supports for a button’s image.
### Getting the Button’s Image
- [var image: UIImage?](./cpnowplayingimagebutton/image.md)
  The image that the button displays.

## Relationships

### Inherits From
- [CPNowPlayingButton](./cpnowplayingbutton.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing the Template’s Buttons
- [var nowPlayingButtons: [CPNowPlayingButton]](./cpnowplayingtemplate/nowplayingbuttons.md)
  The Now Playing template’s playback control buttons.
- [func updateNowPlayingButtons([CPNowPlayingButton])](./cpnowplayingtemplate/updatenowplayingbuttons%28_%29.md)
  Updates the playback control buttons the template displays.
- [class CPNowPlayingButton](./cpnowplayingbutton.md)
  The abstract base class that Now Playing template buttons use.
- [class CPNowPlayingAddToLibraryButton](./cpnowplayingaddtolibrarybutton.md)
  A button for adding the current playing item to a collection.
- [class CPNowPlayingMoreButton](./cpnowplayingmorebutton.md)
  A button for presenting more options to the user.
- [class CPNowPlayingPlaybackRateButton](./cpnowplayingplaybackratebutton.md)
  A button for cycling through the available playback rates.
- [class CPNowPlayingRepeatButton](./cpnowplayingrepeatbutton.md)
  A button for cycling through the available repeat modes.
- [class CPNowPlayingShuffleButton](./cpnowplayingshufflebutton.md)
  A button for cycling through the available shuffle modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingimagebutton)*