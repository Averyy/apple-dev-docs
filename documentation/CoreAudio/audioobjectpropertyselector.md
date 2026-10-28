# AudioObjectPropertySelector

**Framework**: Core Audio  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
typealias AudioObjectPropertySelector = UInt32
```

```c
typedef UInt32 AudioObjectPropertySelector;
```

## Discussion

An AudioObjectPropertySelector is a four char code that identifies, along with the AudioObjectPropertyScope and AudioObjectPropertyElement, a specific piece of information about an AudioObject.

The property selector specifies the general classification of the property such as volume, stream format, latency, etc. Note that each class has a different set of selectors. A subclass inherits its super class’s set of selectors, although it may not implement them all.

## See Also

### Data Types
- [typealias AudioClassID](./audioclassid.md)
- [typealias AudioDeviceID](./audiodeviceid.md)
- [typealias AudioDeviceIOBlock](./audiodeviceioblock.md)
- [typealias AudioDeviceIOProc](./audiodeviceioproc.md)
- [typealias AudioDeviceIOProcID](./audiodeviceioprocid.md)
- [typealias AudioDevicePropertyID](./audiodevicepropertyid.md)
- [typealias AudioDevicePropertyListenerProc](./audiodevicepropertylistenerproc.md)
- [typealias AudioHardwarePropertyID](./audiohardwarepropertyid.md)
- [typealias AudioHardwarePropertyListenerProc](./audiohardwarepropertylistenerproc.md)
- [typealias AudioObjectID](./audioobjectid.md)
- [typealias AudioObjectPropertyElement](./audioobjectpropertyelement.md)
- [typealias AudioObjectPropertyListenerBlock](./audioobjectpropertylistenerblock.md)
- [typealias AudioObjectPropertyListenerProc](./audioobjectpropertylistenerproc.md)
- [typealias AudioObjectPropertyScope](./audioobjectpropertyscope.md)
- [typealias AudioStreamID](./audiostreamid.md)
- [AudioDriverPlugInDevicePropertyChangedProc](./audiodriverplugindevicepropertychangedproc.md)
- [AudioDriverPlugInStreamPropertyChangedProc](./audiodriverpluginstreampropertychangedproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioobjectpropertyselector)*