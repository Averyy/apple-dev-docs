# Deprecated Symbols

**Framework**: AVFAudio

Review unsupported symbols and their replacements.

## Topics

### Activating an audio session
- [func setActive(Bool, withFlags: Int) throws](avaudiosession/setactive(_:withflags:).md)
  Activates or deactivates your app’s audio session; provides flags for use by other audio sessions.
### Requesting permission to record
- [var recordPermission: AVAudioSession.RecordPermission](avaudiosession/recordpermission-swift.property.md)
  The current recording permission status.
- [func requestRecordPermission((Bool) -> Void)](avaudiosession/requestrecordpermission(_:).md)
  Requests the user’s permission to record audio.
### Inspecting audio hardware
- [var currentHardwareInputNumberOfChannels: Int](avaudiosession/currenthardwareinputnumberofchannels.md)
  The number of audio hardware input channels.
- [var currentHardwareOutputNumberOfChannels: Int](avaudiosession/currenthardwareoutputnumberofchannels.md)
  The number of audio hardware output channels.
- [var currentHardwareSampleRate: Double](avaudiosession/currenthardwaresamplerate.md)
  The audio hardware sample rate, in hertz.
- [var inputIsAvailable: Bool](avaudiosession/inputisavailable.md)
  A Boolean value that indicates whether a hardware audio input path is available.
- [var preferredHardwareSampleRate: Double](avaudiosession/preferredhardwaresamplerate.md)
  The preferred hardware sample rate, in hertz.
- [func setPreferredHardwareSampleRate(Double) throws](avaudiosession/setpreferredhardwaresamplerate(_:).md)
  Sets the preferred hardware sample rate for input and output.
### Responding to audio session changes
- [var delegate: (any AVAudioSessionDelegate)?](avaudiosession/delegate.md)
  The delegate object for the audio session.
- [protocol AVAudioSessionDelegate](avaudiosessiondelegate.md)
  A protocol that defines responses to changes in state for the audio session.
### Handling audio session interruptions
- [Interruption flags](1616458-interruption-flags.md)
  Constants that indicate the state of the audio session following an interruption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/deprecated-symbols)*