# AVAudioUnitComponentManager

**Framework**: AVFAudio  
**Kind**: class

An object that provides a way to search and query audio components that the system registers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnitComponentManager
```

#### Overview

The component manager has methods to find various information about the audio components without opening them. Currently, you can only search audio components that are audio units.

The class supports system tags and arbitrary user tags. You can tag each audio unit as part of its definition. Audio unit hosts, such as Logic or GarageBand, can present groupings of audio units according to the tags.

You can search for audio units in the following ways:

- Using a `NSPredicate` instance that contains search strings for tags or descriptions
- Using a block to match on a custom criteria
- Using an `AudioComponentDescription`

## Topics

### Getting the unit audio component manager
- [class func shared() -> Self](avaudiounitcomponentmanager/shared.md)
  Gets the shared component manager instance.
### Getting matching audio components
- [func components(matching: AudioComponentDescription) -> [AVAudioUnitComponent]](avaudiounitcomponentmanager/components(matching:)-9qt94.md)
  Gets an array of audio component objects that match the description.
- [func components(matching: NSPredicate) -> [AVAudioUnitComponent]](avaudiounitcomponentmanager/components(matching:)-96l2c.md)
  Gets an array of audio component objects that match the search predicate.
- [func components(passingTest: (AVAudioUnitComponent, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AVAudioUnitComponent]](avaudiounitcomponentmanager/components(passingtest:).md)
  Gets an array of audio components that pass the block method.
### Getting audio unit tags
- [var standardLocalizedTagNames: [String]](avaudiounitcomponentmanager/standardlocalizedtagnames.md)
  An array of the localized standard system tags the audio units define.
- [var tagNames: [String]](avaudiounitcomponentmanager/tagnames.md)
  An array of all tags the audio unit associates with the current user, and the system tags the audio units define.
### Observing registration changes
- [class let registrationsChangedNotification: NSNotification.Name](avaudiounitcomponentmanager/registrationschangednotification.md)
  A notification the component manager generates when it updates its list of components.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioUnitComponent](avaudiounitcomponent.md)
  An object that provides details about an audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponentmanager)*