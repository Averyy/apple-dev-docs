# CPNowPlayingButton

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

The abstract base class for buttons in the Now Playing interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class CPNowPlayingButton
```

```objc
@interface CPNowPlayingButton : NSObject
```

## Overview

`CPNowPlayingButton` is an abstract base class that provides common behavior for buttons you add to a [`CPNowPlayingTemplate`](./cpnowplayingtemplate.md) object. Don’t instantiate this class directly or define any custom subclasses. Instead, use the properties of this class to affect the behavior of concrete subclasses such as [`CPNowPlayingImageButton`](./cpnowplayingimagebutton.md) or [`CPNowPlayingShuffleButton`](./cpnowplayingshufflebutton.md).

## Topics

### Creating a button
- [init(handler: ((CPNowPlayingButton) -> Void)?)](./cpnowplayingbutton/init%28handler%29.md)
  Creates a button and sets its action to the provided handler.
### Managing the button state
- [var isEnabled: Bool](./cpnowplayingbutton/isenabled.md)
  A Boolean value that indicates whether the button is enabled.
- [var isSelected: Bool](./cpnowplayingbutton/isselected.md)
  A Boolean value that indicates the selected state of a custom button.
### Initializers
- [init?(coder: NSCoder)](./cpnowplayingbutton/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CPNowPlayingAddToLibraryButton](./cpnowplayingaddtolibrarybutton.md)
- [CPNowPlayingImageButton](./cpnowplayingimagebutton.md)
- [CPNowPlayingMoreButton](./cpnowplayingmorebutton.md)
- [CPNowPlayingPlaybackRateButton](./cpnowplayingplaybackratebutton.md)
- [CPNowPlayingRepeatButton](./cpnowplayingrepeatbutton.md)
- [CPNowPlayingShuffleButton](./cpnowplayingshufflebutton.md)
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
- [class CPNowPlayingImageButton](./cpnowplayingimagebutton.md)
  A custom Now Playing button that displays an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingbutton)*