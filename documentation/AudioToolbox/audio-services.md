# Audio Services

**Framework**: Audio Toolbox

Play short sounds or trigger a vibration effect on iOS devices with the appropriate hardware.

#### Overview

System Sound Services provides a C interface for playing short sounds and for invoking vibration on iOS devices that support vibration.

You can use System Sound Services to play short (30 seconds or shorter) sounds. The interface does not provide level, positioning, looping, or timing control, and does not support simultaneous playback: You can play only one sound at a time. You can use System Sound Services to provide audible alerts. On some iOS devices, alerts can include vibration.

## Topics

### Creating and Disposing of System Sound Objects
- [func AudioServicesCreateSystemSoundID(CFURL, UnsafeMutablePointer<SystemSoundID>) -> OSStatus](audioservicescreatesystemsoundid(_:_:).md)
  Creates a system sound object.
- [func AudioServicesDisposeSystemSoundID(SystemSoundID) -> OSStatus](audioservicesdisposesystemsoundid(_:).md)
  Disposes of a system sound object and associated resources.
- [typealias SystemSoundID](systemsoundid.md)
  A system sound object, identified with a sound file you want to play.
- [System Sounds](1405222-system-sounds.md)
- [Alert Sound Identifiers](1618202-alert-sound-identifiers.md)
  Identifiers for alert sounds and alternatives to sounds, for use with the [`AudioServicesPlayAlertSound(_:)`](audioservicesplayalertsound(_:).md) function.
### Playing Sounds
- [func AudioServicesPlayAlertSoundWithCompletion(SystemSoundID, (() -> Void)?)](audioservicesplayalertsoundwithcompletion(_:_:).md)
- [func AudioServicesPlaySystemSoundWithCompletion(SystemSoundID, (() -> Void)?)](audioservicesplaysystemsoundwithcompletion(_:_:).md)
- [func AudioServicesPlayAlertSound(SystemSoundID)](audioservicesplayalertsound(_:).md)
  Plays a system sound as an alert.
- [func AudioServicesPlaySystemSound(SystemSoundID)](audioservicesplaysystemsound(_:).md)
  Plays a system sound object.
### Adding and Removing System Sound Callbacks
- [func AudioServicesAddSystemSoundCompletion(SystemSoundID, CFRunLoop?, CFString?, AudioServicesSystemSoundCompletionProc, UnsafeMutableRawPointer?) -> OSStatus](audioservicesaddsystemsoundcompletion(_:_:_:_:_:).md)
  Registers a callback function that is invoked when a specified system sound finishes playing.
- [func AudioServicesRemoveSystemSoundCompletion(SystemSoundID)](audioservicesremovesystemsoundcompletion(_:).md)
  Unregisters any completion callback functions that were registered for a specified system sound.
- [typealias AudioServicesSystemSoundCompletionProc](audioservicessystemsoundcompletionproc.md)
  A function the system invokes when a system sound finishes playing.
### Managing System Sound Services Properties
- [func AudioServicesGetPropertyInfo(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audioservicesgetpropertyinfo(_:_:_:_:_:).md)
  Gets information about a System Sound Services property.
- [func AudioServicesGetProperty(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](audioservicesgetproperty(_:_:_:_:_:).md)
  Gets a specified System Sound Services property value.
- [func AudioServicesSetProperty(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UInt32, UnsafeRawPointer) -> OSStatus](audioservicessetproperty(_:_:_:_:_:).md)
  Sets the value for a specified System Sound Services property.
- [typealias AudioServicesPropertyID](audioservicespropertyid.md)
  The data type for a system sound property identifier.
- [System Sound Services Property Identifiers](1405268-system-sound-services-property-i.md)
  Property identifiers used when playing alerts with System Sound Services.
- [Audio Hardware Services Properties](1405208-audio-hardware-services-properti.md)
  Property identifiers that apply to HAL audio objects only when accessed via the Audio Hardware Services.
### Getting Error Codes
- [Audio Services Errors](1405232-audio-services-errors.md)
- [var kAudioServicesNoError: OSStatus](kaudioservicesnoerror.md)
  No error has occurred.
- [var kAudioServicesUnsupportedPropertyError: OSStatus](kaudioservicesunsupportedpropertyerror.md)
  The property is not supported.
- [var kAudioServicesBadPropertySizeError: OSStatus](kaudioservicesbadpropertysizeerror.md)
  The size of the property data was not correct.
- [var kAudioServicesBadSpecifierSizeError: OSStatus](kaudioservicesbadspecifiersizeerror.md)
  The size of the specifier data was not correct.
- [var kAudioServicesSystemSoundUnspecifiedError: OSStatus](kaudioservicessystemsoundunspecifiederror.md)
  An unspecified error has occurred.
- [var kAudioServicesSystemSoundClientTimedOutError: OSStatus](kaudioservicessystemsoundclienttimedouterror.md)
  System sound client message timed out.

## See Also

- [Audio Queue Services](audio-queue-services.md)
  Connect to audio hardware and manage the recording or playback process.
- [Music Player](music-player.md)
  Create and play a sequence of tracks, and manage aspects of playback in response to standard events.
- [Anchoring sound to a window or volume](spatializing-sound-from-a-uiscene.md)
  Provide unique app experiences by attaching sounds to windows and volumes in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-services)*