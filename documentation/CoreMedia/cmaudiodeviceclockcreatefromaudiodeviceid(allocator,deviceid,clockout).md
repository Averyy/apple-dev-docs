# CMAudioDeviceClockCreateFromAudioDeviceID(allocator:deviceID:clockOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a clock that tracks playback through a Core Audio device with the specified identifier.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func CMAudioDeviceClockCreateFromAudioDeviceID(allocator: CFAllocator?, deviceID: AudioDeviceID, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus
```

```c
extern OSStatus CMAudioDeviceClockCreateFromAudioDeviceID(CFAllocatorRef allocator, AudioDeviceID deviceID, CMClockRef*clockOut);
```

#### Overview

> ❗ **Important**: In Objective-C, you’re responsible for calling [`CFRelease`](../CoreFoundation/cfrelease.md) to release the clock returned in `clockOut`.

## Parameters

- `allocator`: Allocator for the new clock; pass [`kCFAllocatorDefault`](../CoreFoundation/kcfallocatordefault.md) or `NULL` to use the default allocator.
- `deviceID`: The [`AudioDeviceID`](../CoreAudio/audiodeviceid.md) of the device for which to create a clock.
- `clockOut`: Upon return, a pointer to the newly created clock.

## See Also

### Creating Audio Clocks
- [func CMAudioClockCreate(allocator: CFAllocator?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](./cmaudioclockcreate%28allocator,clockout%29.md)
  Creates a clock that advances at the same rate as audio output.
- [func CMAudioDeviceClockCreate(allocator: CFAllocator?, deviceUID: CFString?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](./cmaudiodeviceclockcreate%28allocator,deviceuid,clockout%29.md)
  Creates a clock that tracks playback through a Core Audio device with the specified unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudiodeviceclockcreatefromaudiodeviceid(allocator:deviceid:clockout:))*