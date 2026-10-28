# MAMusicHapticsManager

**Framework**: Media Accessibility  
**Kind**: class  
**Role**: Class

A class that reports information about the Music Haptics feature.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class MAMusicHapticsManager
```

```objc
@interface MAMusicHapticsManager : NSObject
```

## Overview

Use the [`shared`](./mamusichapticsmanager/shared.md) instance of `MAMusicHapticsManager` to check information about the Music Haptics feature so you can respond accordingly in your app. For example, you can check whether Music Haptics is on, get a notification when it turns on or off, or check whether a haptic track is currently playing along with the Now Playing item.

## Topics

### Getting the shared haptics manager
- [class var shared: MAMusicHapticsManager](./mamusichapticsmanager/shared.md)
  The shared Music Haptics manager object.
### Checking if Music Haptics is on
- [var isActive: Bool](./mamusichapticsmanager/isactive.md)
  A Boolean value that indicates whether the system setting for Music Haptics is on.
- [class let activeStatusDidChangeNotification: NSNotification.Name](./mamusichapticsmanager/activestatusdidchangenotification.md)
  A notification that posts when the value of the Music Haptics system setting changes.
### Checking haptic track availability
- [func checkHapticTrackAvailabilityForMedia(matchingCode: String, completionHandler: ((Bool) -> Void)?)](./mamusichapticsmanager/checkhaptictrackavailabilityformedia%28matchingcode,completionhandler%29.md)
  Checks whether a haptic track is available for the song with the specified International Standard Recording Code (ISRC).
### Observing haptic playback
- [func addStatusObserver((String, Bool) -> Void) -> (any NSCopying)?](./mamusichapticsmanager/addstatusobserver%28_%29.md)
  Adds an observer to monitor the status of haptic playback for the Now Playing song.
- [func removeStatusObserver(any NSCopying)](./mamusichapticsmanager/removestatusobserver%28_%29.md)
  Removes the observer monitoring the status of haptic playback for the Now Playing song.
### Supporting types
- [struct MAMusicHaptics](./mamusichaptics.md)
  A namespace for Music Haptics symbols.
### Macros
- [MediaAccessibility_MAMusicHapticsManager_h](./mediaaccessibility_mamusichapticsmanager_h.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/mamusichapticsmanager)*