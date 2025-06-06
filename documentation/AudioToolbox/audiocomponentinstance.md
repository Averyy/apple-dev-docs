# AudioComponentInstance

**Framework**: Audio Toolbox  
**Kind**: typealias

A component instance, or object, is an audio unit or audio codec.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioComponentInstance = UnsafeMutablePointer<ComponentInstanceRecord>
```

## See Also

- [func AudioComponentRegister(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioComponentFactoryFunction) -> AudioComponent](audiocomponentregister(_:_:_:_:).md)
- [func AudioComponentCount(UnsafePointer<AudioComponentDescription>) -> UInt32](audiocomponentcount(_:).md)
  Returns the number of audio components that match a specified `AudioComponentDescription` structure.
- [func AudioComponentFindNext(AudioComponent?, UnsafePointer<AudioComponentDescription>) -> AudioComponent?](audiocomponentfindnext(_:_:).md)
  Finds the next component that matches a specified `AudioComponentDescription` structure after a specified audio component.
- [func AudioComponentInstanceGetComponent(AudioComponentInstance) -> AudioComponent](audiocomponentinstancegetcomponent(_:).md)
  Retrieves a reference to an audio component from an instance of that audio component.
- [struct AudioComponentDescription](audiocomponentdescription.md)
  Identifying information for an audio component.
- [struct AudioComponentFlags](audiocomponentflags.md)
- [typealias AudioComponentFactoryFunction](audiocomponentfactoryfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstance)*