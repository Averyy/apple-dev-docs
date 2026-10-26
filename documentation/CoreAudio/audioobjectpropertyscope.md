# AudioObjectPropertyScope

**Framework**: Core Audio  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
typealias AudioObjectPropertyScope = UInt32
```

```c
typedef UInt32 AudioObjectPropertyScope;
```

#### Discussion

An AudioObjectPropertyScope is a four char code that identifies, along with the AudioObjectPropertySelector and AudioObjectPropertyElement, a specific piece of information about an AudioObject.

The scope specifies the section of the object in which to look for the property, such as input, output, global, etc. Note that each class has a different set of scopes. A subclass inherits its superclass’s set of scopes.

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
- [typealias AudioObjectPropertySelector](./audioobjectpropertyselector.md)
- [typealias AudioStreamID](./audiostreamid.md)
- [AudioDriverPlugInDevicePropertyChangedProc](./audiodriverplugindevicepropertychangedproc.md)
- [AudioDriverPlugInStreamPropertyChangedProc](./audiodriverpluginstreampropertychangedproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioobjectpropertyscope)*