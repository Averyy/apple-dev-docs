# CMAudioDeviceClockCreate(allocator:deviceUID:clockOut:)

**Framework**: Core Media  
**Kind**: func

Creates a clock that tracks playback through a Core Audio device with the specified unique identifier.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func CMAudioDeviceClockCreate(allocator: CFAllocator?, deviceUID: CFString?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus
```

#### Discussion

When the associated device is completely stopped, the clock continues to advance, tracking [`CMClockGetHostTimeClock()`](cmclockgethosttimeclock().md) until the audio device starts up again.

> ❗ **Important**:  In Objective-C, you’re responsible for calling [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) to release the returned `clockOut`.

## Parameters

- `allocator`: Allocator for the new clock; pass   or   to use the default allocator.
- `deviceUID`: The unique ID of the device for which to create a clock. Pass   to create a clock that tracks the default device.
- `clockOut`: Upon return, a pointer to the newly created clock.

## See Also

- [func CMAudioClockCreate(allocator: CFAllocator?, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](cmaudioclockcreate(allocator:clockout:).md)
  Creates a clock that advances at the same rate as audio output.
- [func CMAudioDeviceClockCreateFromAudioDeviceID(allocator: CFAllocator?, deviceID: AudioDeviceID, clockOut: UnsafeMutablePointer<CMClock?>) -> OSStatus](cmaudiodeviceclockcreatefromaudiodeviceid(allocator:deviceid:clockout:).md)
  Creates a clock that tracks playback through a Core Audio device with the specified identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmaudiodeviceclockcreate(allocator:deviceuid:clockout:))*