# AudioHardwarePropertyListenerProc

**Framework**: Core Audio  
**Kind**: typealias

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias AudioHardwarePropertyListenerProc = (AudioHardwarePropertyID, UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

The return value is currently unused and should always be 0.

#### Discussion

Clients register an AudioHardwarePropertyListenerProc with the AudioSystemObject in order to receive notifications when the properties of the object change.

Note that the same functionality is provided by AudioObjectPropertyListenerProc.

## Parameters

- `inPropertyID`: The AudioHardwarePropertyID of the property that changed.
- `inClientData`: A pointer to client data established when the listener proc was registered   with the AudioSystemObject.

## See Also

- [typealias AudioClassID](audioclassid.md)
- [typealias AudioDeviceID](audiodeviceid.md)
- [typealias AudioDeviceIOBlock](audiodeviceioblock.md)
- [typealias AudioDeviceIOProc](audiodeviceioproc.md)
- [typealias AudioDeviceIOProcID](audiodeviceioprocid.md)
- [typealias AudioDevicePropertyID](audiodevicepropertyid.md)
- [typealias AudioDevicePropertyListenerProc](audiodevicepropertylistenerproc.md)
- [typealias AudioHardwarePropertyID](audiohardwarepropertyid.md)
- [typealias AudioObjectID](audioobjectid.md)
- [typealias AudioObjectPropertyElement](audioobjectpropertyelement.md)
- [typealias AudioObjectPropertyListenerBlock](audioobjectpropertylistenerblock.md)
- [typealias AudioObjectPropertyListenerProc](audioobjectpropertylistenerproc.md)
- [typealias AudioObjectPropertyScope](audioobjectpropertyscope.md)
- [typealias AudioObjectPropertySelector](audioobjectpropertyselector.md)
- [typealias AudioStreamID](audiostreamid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwarepropertylistenerproc)*