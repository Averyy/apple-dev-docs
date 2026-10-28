# AudioDriverPlugInDevicePropertyChangedProc

**Framework**: Core Audio  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```c
typedef int (*)(unsigned int, unsigned int, unsigned char, unsigned int) AudioDriverPlugInDevicePropertyChangedProc;
```

## Return Value

The return value is currently unused and should always be 0.

## Discussion

A plug-in calls this routine to notify the HAL that one of its device’s properties has changed.

The HAL will notify any listeners on behalf of the plug-in. The pointer to this routine is supplied to the plug-in when it is opened.

## Parameters

- `inDevice`: The device whose property has changed.
- `inChannel`: The channel of the device the property that has changed belongs to.
- `isInput`: The section of the device the property that has changed belongs to.
- `inPropertyID`: The selector of the property that has changed.

## See Also

### Data Types
- [typealias AudioClassID](./audioclassid.md)
- [typealias AudioDeviceID](./audiodeviceid.md)
- [typealias AudioDeviceIOBlock](./audiodeviceioblock.md)
- [typealias AudioDeviceIOProc](./audiodeviceioproc.md)
- [typealias AudioDeviceIOProcID](./audiodeviceioprocid.md)
- [typealias AudioDevicePropertyID](./audiodevicepropertyid.md)
- [typealias AudioDevicePropertyListenerProc](./audiodevicepropertylistenerproc.md)
- [AudioDriverPlugInStreamPropertyChangedProc](./audiodriverpluginstreampropertychangedproc.md)
- [typealias AudioHardwarePropertyID](./audiohardwarepropertyid.md)
- [typealias AudioHardwarePropertyListenerProc](./audiohardwarepropertylistenerproc.md)
- [typealias AudioObjectID](./audioobjectid.md)
- [typealias AudioObjectPropertyElement](./audioobjectpropertyelement.md)
- [typealias AudioObjectPropertyListenerBlock](./audioobjectpropertylistenerblock.md)
- [typealias AudioObjectPropertyListenerProc](./audioobjectpropertylistenerproc.md)
- [typealias AudioObjectPropertyScope](./audioobjectpropertyscope.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiodriverplugindevicepropertychangedproc)*