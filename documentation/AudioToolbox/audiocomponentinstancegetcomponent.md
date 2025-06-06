# AudioComponentInstanceGetComponent(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Retrieves a reference to an audio component from an instance of that audio component.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentInstanceGetComponent(_ inInstance: AudioComponentInstance) -> AudioComponent
```

#### Return Value

A reference to the desired audio component. If the value provided in the `inInstance` parameter is invalid, returns `NULL`.

#### Discussion

Use this function to retrieve a reference to the audio component that was used to instantiate a given audio component instance. You can then query the component for its attributes by calling the [`AudioComponentGetDescription(_:_:)`](audiocomponentgetdescription(_:_:).md) function.

## Parameters

- `inInstance`: The component instance whose corresponding factory object you want to get. Must not be  , and you must own the instance (specifically, you must not have previously called   on the instance).

## See Also

- [func AudioComponentRegister(UnsafePointer<AudioComponentDescription>, CFString, UInt32, AudioComponentFactoryFunction) -> AudioComponent](audiocomponentregister(_:_:_:_:).md)
- [func AudioComponentCount(UnsafePointer<AudioComponentDescription>) -> UInt32](audiocomponentcount(_:).md)
  Returns the number of audio components that match a specified `AudioComponentDescription` structure.
- [func AudioComponentFindNext(AudioComponent?, UnsafePointer<AudioComponentDescription>) -> AudioComponent?](audiocomponentfindnext(_:_:).md)
  Finds the next component that matches a specified `AudioComponentDescription` structure after a specified audio component.
- [struct AudioComponentDescription](audiocomponentdescription.md)
  Identifying information for an audio component.
- [typealias AudioComponentInstance](audiocomponentinstance.md)
  A component instance, or object, is an audio unit or audio codec.
- [struct AudioComponentFlags](audiocomponentflags.md)
- [typealias AudioComponentFactoryFunction](audiocomponentfactoryfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentinstancegetcomponent(_:))*