# System Sound Services Property Identifiers

**Framework**: Audio Toolbox

Property identifiers used when playing alerts with System Sound Services.

## Topics

### Constants
- [var kAudioServicesPropertyIsUISound: AudioServicesPropertyID](kaudioservicespropertyisuisound.md)
  A `UInt32` value, where `1` means that, for the audio file specified by a system sound passed in the `inSpecifier` parameter, the System Sound server respects the user setting in the Sound Effects preference and is silent when the user turns off sound effects.
- [var kAudioServicesPropertyCompletePlaybackIfAppDies: AudioServicesPropertyID](kaudioservicespropertycompleteplaybackifappdies.md)
  A `UInt32` value, where `1` means that the audio file specified by a system sound passed in the `inSpecifier` parameter should finish playing even if the client application terminates. This could happen, for example, if the user quits or the application terminates unexpectedly while the sound is playing. The default is `0`. That is, you must explicitly set this property’s value to `1` if you want the sound to complete playing even if the application terminates.

## See Also

- [func AudioServicesGetPropertyInfo(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audioservicesgetpropertyinfo(_:_:_:_:_:).md)
  Gets information about a System Sound Services property.
- [func AudioServicesGetProperty(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](audioservicesgetproperty(_:_:_:_:_:).md)
  Gets a specified System Sound Services property value.
- [func AudioServicesSetProperty(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UInt32, UnsafeRawPointer) -> OSStatus](audioservicessetproperty(_:_:_:_:_:).md)
  Sets the value for a specified System Sound Services property.
- [typealias AudioServicesPropertyID](audioservicespropertyid.md)
  The data type for a system sound property identifier.
- [Audio Hardware Services Properties](1405208-audio-hardware-services-properti.md)
  Property identifiers that apply to HAL audio objects only when accessed via the Audio Hardware Services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1405268-system-sound-services-property-i)*