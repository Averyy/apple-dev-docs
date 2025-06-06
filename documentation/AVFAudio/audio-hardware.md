# Audio hardware

**Framework**: AVFAudio

Inspect and configure audio device settings including input gain, sample rate, and channel counts.

## Topics

### Configuring sample rate
- [var sampleRate: Double](avaudiosession/samplerate.md)
  The current audio sample rate, in hertz.
- [var preferredSampleRate: Double](avaudiosession/preferredsamplerate.md)
  The preferred sample rate, in hertz.
- [func setPreferredSampleRate(Double) throws](avaudiosession/setpreferredsamplerate(_:).md)
  Sets the preferred sample rate for audio input and output.
### Setting input gain
- [var inputGain: Float](avaudiosession/inputgain.md)
  The gain applied to inputs associated with the session.
- [var isInputGainSettable: Bool](avaudiosession/isinputgainsettable.md)
  A Boolean value that indicates whether you can set the input gain.
- [func setInputGain(Float) throws](avaudiosession/setinputgain(_:).md)
  Changes the input gain to the specified value.
### Configuring I/O buffer duration
- [var ioBufferDuration: TimeInterval](avaudiosession/iobufferduration.md)
  The current I/O buffer duration, in seconds.
- [var preferredIOBufferDuration: TimeInterval](avaudiosession/preferrediobufferduration.md)
  The preferred I/O buffer duration, in seconds.
- [func setPreferredIOBufferDuration(TimeInterval) throws](avaudiosession/setpreferrediobufferduration(_:).md)
  Sets the preferred audio I/O buffer duration.
### Inspecting latency
- [var inputLatency: TimeInterval](avaudiosession/inputlatency.md)
  The latency for audio input, in seconds.
- [var outputLatency: TimeInterval](avaudiosession/outputlatency.md)
  The latency for audio output, in seconds.
### Inspecting output volume
- [var outputVolume: Float](avaudiosession/outputvolume.md)
  The systemwide output volume set by the user.
### Setting the number of input channels
- [var preferredInputNumberOfChannels: Int](avaudiosession/preferredinputnumberofchannels.md)
  The preferred number of input channels for the current route.
- [func setPreferredInputNumberOfChannels(Int) throws](avaudiosession/setpreferredinputnumberofchannels(_:).md)
  Sets the preferred number of input channels for the current route.
- [var inputNumberOfChannels: Int](avaudiosession/inputnumberofchannels.md)
  The number of audio input channels for the current route.
- [var maximumInputNumberOfChannels: Int](avaudiosession/maximuminputnumberofchannels.md)
  The maximum number of input channels available for the current audio route.
### Setting the number of output channels
- [var preferredOutputNumberOfChannels: Int](avaudiosession/preferredoutputnumberofchannels.md)
  The preferred number of output channels for the current route.
- [func setPreferredOutputNumberOfChannels(Int) throws](avaudiosession/setpreferredoutputnumberofchannels(_:).md)
  Sets the preferred number of output channels for the current route.
- [var outputNumberOfChannels: Int](avaudiosession/outputnumberofchannels.md)
  The number of audio output channels.
- [var maximumOutputNumberOfChannels: Int](avaudiosession/maximumoutputnumberofchannels.md)
  The maximum number of output channels available for the current audio route.
### Configuring multichannel support
- [var supportsMultichannelContent: Bool](avaudiosession/supportsmultichannelcontent.md)
  A Boolean value that indicates whether your app supplies multichannel audio content.
- [func setSupportsMultichannelContent(Bool) throws](avaudiosession/setsupportsmultichannelcontent(_:).md)
  Sets whether your app supplies multichannel audio content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/audio-hardware)*