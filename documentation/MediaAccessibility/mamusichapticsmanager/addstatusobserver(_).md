# addStatusObserver(_:)

**Framework**: Media Accessibility  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (id<NSCopying>) addStatusObserver:(void (^)(NSString *internationalStandardRecordingCode, BOOL musicHapticsActive)) statusHandler;
```

## See Also

### Observing haptic playback
- [func removeStatusObserver(any NSCopying)](./removestatusobserver%28_%29.md)
  Removes the observer monitoring the status of haptic playback for the Now Playing song.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/mamusichapticsmanager/addstatusobserver(_:))*