# MAMusicHapticsManager

**Framework**: Media Accessibility  
**Kind**: class

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

#### Overview

Use the [`shared`](mamusichapticsmanager/shared.md) instance of `MAMusicHapticsManager` to check information about the Music Haptics feature so you can respond accordingly in your app. For example, you can check whether Music Haptics is on, get a notification when it turns on or off, or check whether a haptic track is currently playing along with the Now Playing item.

## Topics

### Getting the shared haptics manager
- [class var shared: MAMusicHapticsManager](mamusichapticsmanager/shared.md)
  The shared Music Haptics manager object.
### Checking if Music Haptics is on
- [var isActive: Bool](mamusichapticsmanager/isactive.md)
  A Boolean value that indicates whether the system setting for Music Haptics is on.
- [class let activeStatusDidChangeNotification: NSNotification.Name](mamusichapticsmanager/activestatusdidchangenotification.md)
  A notification that posts when the value of the Music Haptics system setting changes.
### Checking haptic track availability
- [func checkHapticTrackAvailabilityForMedia(matchingCode: String, completionHandler: ((Bool) -> Void)?)](mamusichapticsmanager/checkhaptictrackavailabilityformedia(matchingcode:completionhandler:).md)
  Checks whether a haptic track is available for the song with the specified International Standard Recording Code (ISRC).
### Observing haptic playback
- [func addStatusObserver((String, Bool) -> Void) -> (any NSCopying)?](mamusichapticsmanager/addstatusobserver(_:).md)
  Adds an observer to monitor the status of haptic playback for the Now Playing song.
- [func removeStatusObserver(any NSCopying)](mamusichapticsmanager/removestatusobserver(_:).md)
  Removes the observer monitoring the status of haptic playback for the Now Playing song.
### Supporting types
- [struct MAMusicHaptics](mamusichaptics.md)
  A namespace for Music Haptics symbols.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/mamusichapticsmanager)*