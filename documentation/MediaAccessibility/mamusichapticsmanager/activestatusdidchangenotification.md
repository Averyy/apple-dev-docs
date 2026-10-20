# activeStatusDidChangeNotification

**Framework**: Media Accessibility  
**Kind**: property  
**Role**: Type Property

A notification that posts when the value of the Music Haptics system setting changes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class let activeStatusDidChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const MAMusicHapticsManagerActiveStatusDidChangeNotification;
```

## See Also

### Checking if Music Haptics is on
- [var isActive: Bool](./isactive.md)
  A Boolean value that indicates whether the system setting for Music Haptics is on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/mamusichapticsmanager/activestatusdidchangenotification)*