# removeStatusObserver(_:)

**Framework**: Media Accessibility  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeStatusObserver:(id<NSCopying>) registrationToken;
```

## See Also

### Observing haptic playback
- [func addStatusObserver((String, Bool) -> Void) -> (any NSCopying)?](./addstatusobserver%28_%29.md)
  Adds an observer to monitor the status of haptic playback for the Now Playing song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/mamusichapticsmanager/removestatusobserver(_:))*