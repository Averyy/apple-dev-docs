# Audio Units

**Framework**: AVFAudio

The data type for a plug-in component that provides audio processing or audio data generation.

## Topics

### Essentials
- [Creating an audio unit extension](creating-an-audio-unit-extension.md)
  Build an extension by using an Xcode template.
- [Using voice processing](using-voice-processing.md)
  Add voice-processing capabilities to your app by using audio engine.
- [class AVAudioUnit](avaudiounit.md)
  A subclass of the audio node class that, processes audio either in real time or nonreal time, depending on the type of the audio unit.
### Component management
- [class AVAudioUnitComponent](avaudiounitcomponent.md)
  An object that provides details about an audio unit.
- [class AVAudioUnitComponentManager](avaudiounitcomponentmanager.md)
  An object that provides a way to search and query audio components that the system registers.
### Audio effects
- [class AVAudioUnitEffect](avaudiouniteffect.md)
  An object that processes audio in real time.
- [class AVAudioUnitEQ](avaudiouniteq.md)
  An object that implements a multiband equalizer.
- [class AVAudioUnitDistortion](avaudiounitdistortion.md)
  An object that implements a multistage distortion effect.
- [class AVAudioUnitDelay](avaudiounitdelay.md)
  An object that implements a delay effect.
- [class AVAudioUnitReverb](avaudiounitreverb.md)
  An object that implements a reverb effect.
### Time effects
- [class AVAudioUnitTimeEffect](avaudiounittimeeffect.md)
  An object that processes audio in nonreal time.
- [class AVAudioUnitTimePitch](avaudiounittimepitch.md)
  An object that provides a good-quality playback rate and pitch shifting independently of each other.
- [class AVAudioUnitVarispeed](avaudiounitvarispeed.md)
  An object that allows control of the playback rate.
### Audio generation
- [class AVAudioUnitGenerator](avaudiounitgenerator.md)
  An object that generates audio output.
### Speech synthesis
- [Creating a custom speech synthesizer](creating-a-custom-speech-synthesizer.md)
  Use your custom voices to synthesize speech by building a speech synthesis provider.
- [class AVSpeechSynthesisProviderAudioUnit](avspeechsynthesisprovideraudiounit.md)
  An object that generates speech from text.
### MIDI
- [class AVAudioUnitMIDIInstrument](avaudiounitmidiinstrument.md)
  An object that represents music devices or remote instruments.

## See Also

- [Creating custom audio effects](creating-custom-audio-effects.md)
  Add custom audio-effect processing to apps like Logic Pro X and GarageBand by creating Audio Unit (AU) plug-ins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/audio-units)*