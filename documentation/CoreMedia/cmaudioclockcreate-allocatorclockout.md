# CMAudioClockCreate(allocator:clockOut:)

**Framework**: Coremedia  
**Kind**: func

Creates a clock that advances at the same rate as audio output.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMAudioClockCreate(allocator: CFAllocator?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus
```

#### Discussion

This clock doesn’t drift from audio output, but may drift from [`CMClockGetHostTimeClock()`](cmclockgethosttimeclock().md). When audio output is completely stopped, the clock continues to advance, tracking `CMClockGetHostTimeClock` until audio output starts up again.

> ❗ **Important**:  In Objective-C, you’re responsible for calling [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) to release the returned `clockOut`.

You can use this clock as the [`sourceClock`](https://developer.apple.com/documentation/AVFoundation/AVPlayer/sourceClock) of an [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) instance when synchronizing video-only playback with audio played through other APIs or objects.

> **Note**:  For Mac apps built with Mac Catalyst, use [`CMAudioDeviceClockCreate(allocator:deviceUID:clockOut:)`](cmaudiodeviceclockcreate(allocator:deviceuid:clockout:).md) or [`CMAudioDeviceClockCreateFromAudioDeviceID(allocator:deviceID:clockOut:)`](cmaudiodeviceclockcreatefromaudiodeviceid(allocator:deviceid:clockout:).md) to target a specific, nondefault audio device.

## Parameters

- `allocator`: Allocator for the new clock; pass   or   to use the default allocator.
- `clockOut`: Upon return, a pointer to the newly created clock.

## See Also

- [func CMAudioDeviceClockCreate(allocator: CFAllocator?, deviceUID: CFString?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](cmaudiodeviceclockcreate(allocator:deviceuid:clockout:).md)
  Creates a clock that tracks playback through a Core Audio device with the specified unique identifier.
- [func CMAudioDeviceClockCreateFromAudioDeviceID(allocator: CFAllocator?, deviceID: AudioDeviceID, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](cmaudiodeviceclockcreatefromaudiodeviceid(allocator:deviceid:clockout:).md)
  Creates a clock that tracks playback through a Core Audio device with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudioclockcreate(allocator:clockout:))*