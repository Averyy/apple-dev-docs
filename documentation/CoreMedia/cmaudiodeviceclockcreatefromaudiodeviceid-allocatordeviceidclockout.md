# CMAudioDeviceClockCreateFromAudioDeviceID(allocator:deviceID:clockOut:)

**Framework**: Core Media  
**Kind**: func

Creates a clock that tracks playback through a Core Audio device with the specified identifier.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func CMAudioDeviceClockCreateFromAudioDeviceID(allocator: CFAllocator?, deviceID: AudioDeviceID, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus
```

#### Overview

> ❗ **Important**: In Objective-C, you’re responsible for calling [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) to release the clock returned in `clockOut`.

## Parameters

- `allocator`: Allocator for the new clock; pass   or   to use the default allocator.
- `deviceID`: The   of the device for which to create a clock.
- `clockOut`: Upon return, a pointer to the newly created clock.

## See Also

- [func CMAudioClockCreate(allocator: CFAllocator?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](cmaudioclockcreate(allocator:clockout:).md)
  Creates a clock that advances at the same rate as audio output.
- [func CMAudioDeviceClockCreate(allocator: CFAllocator?, deviceUID: CFString?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](cmaudiodeviceclockcreate(allocator:deviceuid:clockout:).md)
  Creates a clock that tracks playback through a Core Audio device with the specified unique identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudiodeviceclockcreatefromaudiodeviceid(allocator:deviceid:clockout:))*