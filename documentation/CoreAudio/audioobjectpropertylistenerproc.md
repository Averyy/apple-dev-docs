# AudioObjectPropertyListenerProc

**Framework**: Core Audio  
**Kind**: typealias

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias AudioObjectPropertyListenerProc = (AudioObjectID, UInt32, UnsafePointer<AudioObjectPropertyAddress>, UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

The return value is currently unused and should always be 0.

#### Discussion

Clients register an AudioObjectPropertyListenerProc with an AudioObject in order to receive notifications when the properties of the object change.

Listeners will be called when possibly many properties have changed. Consequently, the implementation of a listener must go through the array of addresses to see what exactly has changed. Note that the array of addresses will always have at least one address in it for which the listener is signed up to receive notifications about but may contain addresses for properties for which the listener is not signed up to receive notifications.

## Parameters

- `inObjectID`: The AudioObject whose properties have changed.
- `inNumberAddresses`: The number of elements in the inAddresses array.
- `inAddresses`: An array of AudioObjectPropertyAddresses indicating which properties   changed.
- `inClientData`: A pointer to client data established when the listener proc was registered   with the AudioObject.

## See Also

- [typealias AudioClassID](audioclassid.md)
- [typealias AudioDeviceID](audiodeviceid.md)
- [typealias AudioDeviceIOBlock](audiodeviceioblock.md)
- [typealias AudioDeviceIOProc](audiodeviceioproc.md)
- [typealias AudioDeviceIOProcID](audiodeviceioprocid.md)
- [typealias AudioDevicePropertyID](audiodevicepropertyid.md)
- [typealias AudioDevicePropertyListenerProc](audiodevicepropertylistenerproc.md)
- [typealias AudioHardwarePropertyID](audiohardwarepropertyid.md)
- [typealias AudioHardwarePropertyListenerProc](audiohardwarepropertylistenerproc.md)
- [typealias AudioObjectID](audioobjectid.md)
- [typealias AudioObjectPropertyElement](audioobjectpropertyelement.md)
- [typealias AudioObjectPropertyListenerBlock](audioobjectpropertylistenerblock.md)
- [typealias AudioObjectPropertyScope](audioobjectpropertyscope.md)
- [typealias AudioObjectPropertySelector](audioobjectpropertyselector.md)
- [typealias AudioStreamID](audiostreamid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioobjectpropertylistenerproc)*