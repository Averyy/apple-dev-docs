# removeStatusObserver(_:)

**Framework**: Media Accessibility  
**Kind**: method

Removes the observer monitoring the status of haptic playback for the Now Playing song.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func removeStatusObserver(_ registrationToken: any NSCopying)
```

## See Also

- [func addStatusObserver((String, Bool) -> Void) -> (any NSCopying)?](mamusichapticsmanager/addstatusobserver(_:).md)
  Adds an observer to monitor the status of haptic playback for the Now Playing song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/mamusichapticsmanager/removestatusobserver(_:))*