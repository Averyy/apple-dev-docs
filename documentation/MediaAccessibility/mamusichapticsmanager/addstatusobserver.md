# addStatusObserver(_:)

**Framework**: Media Accessibility  
**Kind**: method

Adds an observer to monitor the status of haptic playback for the Now Playing song.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func addStatusObserver(_ statusHandler: @escaping (String, Bool) -> Void) -> (any NSCopying)?
```

## See Also

- [func removeStatusObserver(any NSCopying)](mamusichapticsmanager/removestatusobserver(_:).md)
  Removes the observer monitoring the status of haptic playback for the Now Playing song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/mamusichapticsmanager/addstatusobserver(_:))*