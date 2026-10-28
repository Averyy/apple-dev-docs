# setActive(_:withFlags:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Activates or deactivates your app’s audio session; provides flags for use by other audio sessions.

**Availability**:
- Mac Catalyst 14.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`setActive(_:options:)`](./setactive%28_,options%29.md) instead.

## Declaration

```swift
func setActive(_ active: Bool, withFlags flags: Int) throws
```

```objc
- (BOOL) setActive:(BOOL) active withFlags:(NSInteger) flags error:(NSError **) outError;
```

## Discussion

If another app’s active audio session has higher priority than your app, and that other audio session doesn’t allow mixing with other apps, attempting to activate your audio session might fail.

## Parameters

- `active`: Use [`true`](../../Swift/true.md) to activate your app’s audio session or [`false`](../../Swift/false.md) to deactivate it.
- `flags`: A bitmapped value containing one or more flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setactive(_:withflags:))*