# CPNowPlayingMode

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that defines the appearance and layout of the Now Playing interface.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
@MainActor
class CPNowPlayingMode
```

```objc
@interface CPNowPlayingMode : NSObject
```

## Overview

Use the `CPNowPlayingMode` type to retrieve the default mode for the Now Playing interface. The default mode specifies a layout suitable for showing the currently playing audio track from a playlist. For example, it shows the track title, artist information, album artwork, and any custom controls to manage playback behaviors.

You don’t create an instance of this class directly. When you need to return the Now Playing interface to the default mode, retrieve the [`default`](./cpnowplayingmode/default.md) object and assign it to the [`nowPlayingMode`](./cpnowplayingtemplate/nowplayingmode.md) property of the Now Playing template. Return the interface to the default mode when you’re not actively using a different mode. For example, a sports app might return the interface to the default mode after a match finishes.

## Topics

### Creating a playing mode
- [class var `default`: CPNowPlayingMode](./cpnowplayingmode/default.md)
  The default appearance and layout for the Now Playing interface.
- [init?(coder: NSCoder)](./cpnowplayingmode/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CPNowPlayingModeSports](./cpnowplayingmodesports.md)
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

### Interface modes
- [class CPNowPlayingModeSports](./cpnowplayingmodesports.md)
  A mode that manages the sporting event details to display in the Now Playing interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingmode)*