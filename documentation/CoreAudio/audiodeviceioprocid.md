# AudioDeviceIOProcID

**Framework**: Core Audio  
**Kind**: typealias

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias AudioDeviceIOProcID = AudioDeviceIOProc
```

#### Discussion

An AudioDeviceIOProcID represents both an IOProc and the client data that goes with it. Once created, an AudioDeviceIOProcID can be used everywhere one would use a regular IOProc. The purpose for an AudioDeviceIOProcID is to allow a client to register the same function pointer as an IOProc with a device multiple times provided

## See Also

- [typealias AudioClassID](audioclassid.md)
- [typealias AudioDeviceID](audiodeviceid.md)
- [typealias AudioDeviceIOBlock](audiodeviceioblock.md)
- [typealias AudioDeviceIOProc](audiodeviceioproc.md)
- [typealias AudioDevicePropertyID](audiodevicepropertyid.md)
- [typealias AudioDevicePropertyListenerProc](audiodevicepropertylistenerproc.md)
- [typealias AudioHardwarePropertyID](audiohardwarepropertyid.md)
- [typealias AudioHardwarePropertyListenerProc](audiohardwarepropertylistenerproc.md)
- [typealias AudioObjectID](audioobjectid.md)
- [typealias AudioObjectPropertyElement](audioobjectpropertyelement.md)
- [typealias AudioObjectPropertyListenerBlock](audioobjectpropertylistenerblock.md)
- [typealias AudioObjectPropertyListenerProc](audioobjectpropertylistenerproc.md)
- [typealias AudioObjectPropertyScope](audioobjectpropertyscope.md)
- [typealias AudioObjectPropertySelector](audioobjectpropertyselector.md)
- [typealias AudioStreamID](audiostreamid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodeviceioprocid)*