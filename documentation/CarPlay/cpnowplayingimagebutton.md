# CPNowPlayingImageButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A custom Now Playing button that displays an image.

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

Use a `CPNowPlayingImageButton` object to add custom actions to the Now Playing interface. This button type displays the image you provide and calls your handler in response to interactions. The system displays your image with a tint color, so specify images with a single color for the best results.

Create the button and add it as one of the [`nowPlayingButtons`](./cpnowplayingtemplate/nowplayingbuttons.md) in your Now Playing template. Create this type of button only for custom actions, and don’t use it to replicate the behavior of system-provided types like [`CPNowPlayingShuffleButton`](./cpnowplayingshufflebutton.md) or [`CPNowPlayingRepeatButton`](./cpnowplayingrepeatbutton.md).

## Topics

### Creating the button
- [init(image: UIImage, handler: ((CPNowPlayingButton) -> Void)?)](./cpnowplayingimagebutton/init%28image,handler%29.md)
  Creates a button with the specified image and handler.
- [let CPNowPlayingButtonMaximumImageSize: CGSize](./cpnowplayingbuttonmaximumimagesize.md)
  The dimensions for images in custom buttons.
### Getting the button’s image
- [var image: UIImage?](./cpnowplayingimagebutton/image.md)
  The image to display for the button.

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

### Now Playing buttons
- [class CPNowPlayingShuffleButton](./cpnowplayingshufflebutton.md)
  A button for toggling shuffle mode on and off.
- [class CPNowPlayingRepeatButton](./cpnowplayingrepeatbutton.md)
  A button for cycling through the available repeat modes.
- [class CPNowPlayingPlaybackRateButton](./cpnowplayingplaybackratebutton.md)
  A button for changing the playback rate of the media.
- [class CPNowPlayingAddToLibraryButton](./cpnowplayingaddtolibrarybutton.md)
  A button for adding the current item to a collection, such as the person’s library.
- [class CPNowPlayingMoreButton](./cpnowplayingmorebutton.md)
  A button for displaying additional playback options.
- [class CPNowPlayingButton](./cpnowplayingbutton.md)
  The abstract base class for buttons in the Now Playing interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingimagebutton)*