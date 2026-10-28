# CMAudioClockCreate(allocator:clockOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern OSStatus CMAudioClockCreate(CFAllocatorRef allocator, CMClockRef*clockOut);
```

## Discussion

This clock doesn’t drift from audio output, but may drift from [`CMClockGetHostTimeClock()`](./cmclockgethosttimeclock%28%29.md). When audio output is completely stopped, the clock continues to advance, tracking `CMClockGetHostTimeClock` until audio output starts up again.

> ❗ **Important**:  In Objective-C, you’re responsible for calling [`CFRelease`](../CoreFoundation/cfrelease.md) to release the returned `clockOut`.

You can use this clock as the [`sourceClock`](../AVFoundation/avplayer/sourceclock.md) of an [`AVPlayer`](../AVFoundation/avplayer.md) instance when synchronizing video-only playback with audio played through other APIs or objects.

> **Note**:  For Mac apps built with Mac Catalyst, use [`CMAudioDeviceClockCreate(allocator:deviceUID:clockOut:)`](./cmaudiodeviceclockcreate%28allocator,deviceuid,clockout%29.md) or [`CMAudioDeviceClockCreateFromAudioDeviceID(allocator:deviceID:clockOut:)`](./cmaudiodeviceclockcreatefromaudiodeviceid%28allocator,deviceid,clockout%29.md) to target a specific, nondefault audio device.

## Parameters

- `allocator`: Allocator for the new clock; pass [`kCFAllocatorDefault`](../CoreFoundation/kcfallocatordefault.md) or `nil` to use the default allocator.
- `clockOut`: Upon return, a pointer to the newly created clock.

## See Also

### Creating Audio Clocks
- [func CMAudioDeviceClockCreate(allocator: CFAllocator?, deviceUID: CFString?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](./cmaudiodeviceclockcreate%28allocator,deviceuid,clockout%29.md)
  Creates a clock that tracks playback through a Core Audio device with the specified unique identifier.
- [func CMAudioDeviceClockCreateFromAudioDeviceID(allocator: CFAllocator?, deviceID: AudioDeviceID, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](./cmaudiodeviceclockcreatefromaudiodeviceid%28allocator,deviceid,clockout%29.md)
  Creates a clock that tracks playback through a Core Audio device with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudioclockcreate(allocator:clockout:))*