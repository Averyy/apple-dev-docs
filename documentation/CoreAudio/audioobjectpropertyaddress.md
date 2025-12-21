# AudioObjectPropertyAddress

**Framework**: Core Audio  
**Kind**: struct

An AudioObjectPropertyAddress collects the three parts that identify a specific property together in a struct for easy transmission.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct AudioObjectPropertyAddress
```

#### Overview

- term: `mSelector`: The AudioObjectPropertySelector for the property.
- term: `mScope`: The AudioObjectPropertyScope for the property.
- term: `mElement`: The AudioObjectPropertyElement for the property.

## Topics

### Initializers
- [init()](audioobjectpropertyaddress/init.md)
- [init(mSelector: AudioObjectPropertySelector, mScope: AudioObjectPropertyScope, mElement: AudioObjectPropertyElement)](audioobjectpropertyaddress/init(mselector:mscope:melement:).md)
### Instance Properties
- [var mElement: AudioObjectPropertyElement](audioobjectpropertyaddress/melement.md)
- [var mScope: AudioObjectPropertyScope](audioobjectpropertyaddress/mscope.md)
- [var mSelector: AudioObjectPropertySelector](audioobjectpropertyaddress/mselector.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AudioHardwareIOProcStreamUsage](audiohardwareioprocstreamusage.md)
  This structure describes which streams a given AudioDeviceIOProc will use. It is used in conjunction with kAudioDevicePropertyIOProcStreamUsage.
- [struct AudioStreamRangedDescription](audiostreamrangeddescription.md)
  This structure allows a specific sample rate range to be associated with an AudioStreamBasicDescription that specifies its sample rate as kAudioStreamAnyRate.
- [struct UnsafeMutableAudioBufferListPointer](unsafemutableaudiobufferlistpointer.md)
  A wrapper for a pointer to an `AudioBufferList`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audioobjectpropertyaddress)*