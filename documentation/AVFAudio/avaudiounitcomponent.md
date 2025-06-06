# AVAudioUnitComponent

**Framework**: AVFAudio  
**Kind**: class

An object that provides details about an audio unit.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAudioUnitComponent
```

#### Overview

Details can include information such as type, subtype, manufacturer, and location. An `AVAudioUnitComponent` can include user tags, which you can query later for display.

## Topics

### Getting the audio unit component’s audio unit
- [var audioComponent: AudioComponent](avaudiounitcomponent/audiocomponent.md)
  The underlying audio component.
### Getting audio unit component information
- [var audioComponentDescription: AudioComponentDescription](avaudiounitcomponent/audiocomponentdescription.md)
  The audio component description.
- [var availableArchitectures: [NSNumber]](avaudiounitcomponent/availablearchitectures.md)
  An array of architectures that the audio unit supports.
- [var configurationDictionary: [String : Any]](avaudiounitcomponent/configurationdictionary.md)
  The audio unit component’s configuration dictionary.
- [var hasCustomView: Bool](avaudiounitcomponent/hascustomview.md)
  A Boolean value that indicates whether the audio unit component has a custom view.
- [var hasMIDIInput: Bool](avaudiounitcomponent/hasmidiinput.md)
  A Boolean value that indicates whether the audio unit component has MIDI input.
- [var hasMIDIOutput: Bool](avaudiounitcomponent/hasmidioutput.md)
  A Boolean value that indicates whether the audio unit component has MIDI output.
- [var manufacturerName: String](avaudiounitcomponent/manufacturername.md)
  The name of the manufacturer of the audio unit component.
- [var name: String](avaudiounitcomponent/name.md)
  The name of the audio unit component.
- [var passesAUVal: Bool](avaudiounitcomponent/passesauval.md)
  A Boolean value that indicates whether the audio unit component passes the validation tests.
- [var isSandboxSafe: Bool](avaudiounitcomponent/issandboxsafe.md)
  A Boolean value that indicates whether the audio unit component is safe for sandboxing.
- [func supportsNumberInputChannels(Int, outputChannels: Int) -> Bool](avaudiounitcomponent/supportsnumberinputchannels(_:outputchannels:).md)
  Gets a Boolean value that indicates whether the audio unit component supports the specified number of input and output channels.
- [var typeName: String](avaudiounitcomponent/typename.md)
  The audio unit component type.
- [var version: Int](avaudiounitcomponent/version.md)
  The audio unit component version number.
- [var versionString: String](avaudiounitcomponent/versionstring.md)
  A string that represents the audio unit component version number.
- [var componentURL: URL?](avaudiounitcomponent/componenturl.md)
  The URL of the audio unit component.
### Getting audio unit component tags
- [var iconURL: URL?](avaudiounitcomponent/iconurl.md)
  The URL of an icon that represents the audio unit component.
- [var icon: UIImage?](avaudiounitcomponent/icon.md)
  An icon that represents the component.
- [var localizedTypeName: String](avaudiounitcomponent/localizedtypename.md)
  The localized type name of the component.
- [var allTagNames: [String]](avaudiounitcomponent/alltagnames.md)
  An array of tag names for the audio unit component.
- [var userTagNames: [String]](avaudiounitcomponent/usertagnames.md)
  An array of tags the user creates.
### Audio unit manufacturer names
- [let AVAudioUnitManufacturerNameApple: String](avaudiounitmanufacturernameapple.md)
  The audio unit manufacturer is Apple.
### Audio unit types
- [let AVAudioUnitTypeOutput: String](avaudiounittypeoutput.md)
  An audio unit type that represents an output.
- [let AVAudioUnitTypeMusicDevice: String](avaudiounittypemusicdevice.md)
  An audio unit type that represents a music device.
- [let AVAudioUnitTypeMusicEffect: String](avaudiounittypemusiceffect.md)
  An audio unit type that represents a music effect.
- [let AVAudioUnitTypeFormatConverter: String](avaudiounittypeformatconverter.md)
  An audio unit type that represents a format converter.
- [let AVAudioUnitTypeEffect: String](avaudiounittypeeffect.md)
  An audio unit type that represents an effect.
- [let AVAudioUnitTypeMixer: String](avaudiounittypemixer.md)
  An audio unit type that represents a mixer.
- [let AVAudioUnitTypePanner: String](avaudiounittypepanner.md)
  An audio unit type that represents a panner.
- [let AVAudioUnitTypeGenerator: String](avaudiounittypegenerator.md)
  An audio unit type that represents a generator.
- [let AVAudioUnitTypeOfflineEffect: String](avaudiounittypeofflineeffect.md)
  An audio unit type that represents an offline effect.
- [let AVAudioUnitTypeMIDIProcessor: String](avaudiounittypemidiprocessor.md)
  An audio unit type that represents a MIDI processor.

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

- [class AVAudioUnitComponentManager](avaudiounitcomponentmanager.md)
  An object that provides a way to search and query audio components that the system registers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponent)*