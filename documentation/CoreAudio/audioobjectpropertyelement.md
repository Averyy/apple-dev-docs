# AudioObjectPropertyElement

**Framework**: Core Audio  
**Kind**: typealias

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias AudioObjectPropertyElement = UInt32
```

#### Discussion

An AudioObjectPropertyElement is an integer that identifies, along with the AudioObjectPropertySelector and AudioObjectPropertyScope, a specific piece of information about an AudioObject.

The element selects one of possibly many items in the section of the object in which to look for the property. Elements are number sequentially where 0 represents the main element. Elements are particular to an instance of a class, meaning that two instances can have different numbers of elements in the same scope. There is no inheritance of elements.

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
- [typealias AudioObjectPropertyListenerBlock](audioobjectpropertylistenerblock.md)
- [typealias AudioObjectPropertyListenerProc](audioobjectpropertylistenerproc.md)
- [typealias AudioObjectPropertyScope](audioobjectpropertyscope.md)
- [typealias AudioObjectPropertySelector](audioobjectpropertyselector.md)
- [typealias AudioStreamID](audiostreamid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioobjectpropertyelement)*