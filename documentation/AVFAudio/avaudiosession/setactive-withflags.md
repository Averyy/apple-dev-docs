# setActive(_:withFlags:)

**Framework**: AVFAudio  
**Kind**: method

Activates or deactivates your app’s audio session; provides flags for use by other audio sessions.

**Availability**:
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func setActive(_ active: Bool, withFlags flags: Int) throws
```

#### Discussion

If another app’s active audio session has higher priority than your app, and that other audio session doesn’t allow mixing with other apps, attempting to activate your audio session might fail.

## Parameters

- `active`: Use   to activate your app’s audio session or   to deactivate it.
- `flags`: A bitmapped value containing one or more flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setactive(_:withflags:))*