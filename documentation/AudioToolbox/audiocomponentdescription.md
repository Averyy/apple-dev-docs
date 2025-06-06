# AudioComponentDescription

**Framework**: Audio Toolbox  
**Kind**: struct

Identifying information for an audio component.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioComponentDescription
```

## Topics

### Properties
- [var componentType: OSType](audiocomponentdescription/componenttype.md)
  A unique 4-byte code identifying the interface for the component.
- [var componentSubType: OSType](audiocomponentdescription/componentsubtype.md)
  A 4-byte code that you can use to indicate the purpose of a component. For example, you could use `lpas` or `lowp` as a mnemonic indication that an audio unit is a low-pass filter.
- [var componentManufacturer: OSType](audiocomponentdescription/componentmanufacturer.md)
  The unique vendor identifier, registered with Apple, for the audio component.
- [var componentFlags: UInt32](audiocomponentdescription/componentflags.md)
  Set this value to zero.
- [var componentFlagsMask: UInt32](audiocomponentdescription/componentflagsmask.md)
  Set this value to zero.
### Initializers
- [init()](audiocomponentdescription/init.md)
- [init(componentType: OSType, componentSubType: OSType, componentManufacturer: OSType, componentFlags: UInt32, componentFlagsMask: UInt32)](audiocomponentdescription/init(componenttype:componentsubtype:componentmanufacturer:componentflags:componentflagsmask:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func AudioComponentRegister(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioComponentFactoryFunction) -> AudioComponent](audiocomponentregister(_:_:_:_:).md)
- [func AudioComponentCount(UnsafePointer<AudioComponentDescription>) -> UInt32](audiocomponentcount(_:).md)
  Returns the number of audio components that match a specified `AudioComponentDescription` structure.
- [func AudioComponentFindNext(AudioComponent?, UnsafePointer<AudioComponentDescription>) -> AudioComponent?](audiocomponentfindnext(_:_:).md)
  Finds the next component that matches a specified `AudioComponentDescription` structure after a specified audio component.
- [func AudioComponentInstanceGetComponent(AudioComponentInstance) -> AudioComponent](audiocomponentinstancegetcomponent(_:).md)
  Retrieves a reference to an audio component from an instance of that audio component.
- [typealias AudioComponentInstance](audiocomponentinstance.md)
  A component instance, or object, is an audio unit or audio codec.
- [struct AudioComponentFlags](audiocomponentflags.md)
- [typealias AudioComponentFactoryFunction](audiocomponentfactoryfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription)*