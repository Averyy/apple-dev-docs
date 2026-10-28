# AudioServerPlugInCustomPropertyDataType

**Framework**: Core Audio  
**Kind**: typealias  
**Role**: Type Alias

The set of data types the Host knows how to marshal between the server and the client.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef UInt32 AudioServerPlugInCustomPropertyDataType;
```

## Discussion

These are the only types supported for custom properties. See [`AudioServerPlugInCustomPropertyInfo`](./audioserverplugincustompropertyinfo.md) for more information.

- **`kAudioServerPlugInCustomPropertyDataTypeNone`**: This is used to declare that the property doesn’t have any property or qualifier data.
- **`kAudioServerPlugInCustomPropertyDataTypeCFString`**: The property/qualifier data is a CFStringRef.
- **`kAudioServerPlugInCustomPropertyDataTypeCFPropertyList`**: The property/qualifier data is a CFPropertyListRef.

## See Also

### Data Types
- [typealias AudioClassID](./audioclassid.md)
- [typealias AudioDeviceID](./audiodeviceid.md)
- [typealias AudioDeviceIOBlock](./audiodeviceioblock.md)
- [typealias AudioDeviceIOProc](./audiodeviceioproc.md)
- [typealias AudioDeviceIOProcID](./audiodeviceioprocid.md)
- [typealias AudioDevicePropertyID](./audiodevicepropertyid.md)
- [typealias AudioDevicePropertyListenerProc](./audiodevicepropertylistenerproc.md)
- [AudioDriverPlugInDevicePropertyChangedProc](./audiodriverplugindevicepropertychangedproc.md)
- [AudioDriverPlugInStreamPropertyChangedProc](./audiodriverpluginstreampropertychangedproc.md)
- [typealias AudioHardwarePropertyID](./audiohardwarepropertyid.md)
- [typealias AudioHardwarePropertyListenerProc](./audiohardwarepropertylistenerproc.md)
- [typealias AudioObjectID](./audioobjectid.md)
- [typealias AudioObjectPropertyElement](./audioobjectpropertyelement.md)
- [typealias AudioObjectPropertyListenerBlock](./audioobjectpropertylistenerblock.md)
- [typealias AudioObjectPropertyListenerProc](./audioobjectpropertylistenerproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioserverplugincustompropertydatatype)*