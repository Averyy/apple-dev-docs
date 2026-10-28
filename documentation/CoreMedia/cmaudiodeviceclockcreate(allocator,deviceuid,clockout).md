# CMAudioDeviceClockCreate(allocator:deviceUID:clockOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Creates a clock that tracks playback through a Core Audio device with the specified unique identifier.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func CMAudioDeviceClockCreate(allocator: CFAllocator?, deviceUID: CFString?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus
```

```c
extern OSStatus CMAudioDeviceClockCreate(CFAllocatorRef allocator, CFStringRef deviceUID, CMClockRef*clockOut);
```

## Discussion

When the associated device is completely stopped, the clock continues to advance, tracking [`CMClockGetHostTimeClock()`](./cmclockgethosttimeclock%28%29.md) until the audio device starts up again.

> ❗ **Important**:  In Objective-C, you’re responsible for calling [`CFRelease`](../CoreFoundation/cfrelease.md) to release the returned `clockOut`.

## Parameters

- `allocator`: Allocator for the new clock; pass [`kCFAllocatorDefault`](../CoreFoundation/kcfallocatordefault.md) or `NULL` to use the default allocator.
- `deviceUID`: The unique ID of the device for which to create a clock. Pass `NULL` to create a clock that tracks the default device.
- `clockOut`: Upon return, a pointer to the newly created clock.

## See Also

### Creating Audio Clocks
- [func CMAudioClockCreate(allocator: CFAllocator?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](./cmaudioclockcreate%28allocator,clockout%29.md)
  Creates a clock that advances at the same rate as audio output.
- [func CMAudioDeviceClockCreateFromAudioDeviceID(allocator: CFAllocator?, deviceID: AudioDeviceID, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](./cmaudiodeviceclockcreatefromaudiodeviceid%28allocator,deviceid,clockout%29.md)
  Creates a clock that tracks playback through a Core Audio device with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudiodeviceclockcreate(allocator:deviceuid:clockout:))*