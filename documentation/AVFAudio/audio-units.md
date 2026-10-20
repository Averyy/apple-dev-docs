# Audio Unit plug-ins

**Framework**: AVFAudio  
**Role**: API Collection

Add built-in and custom Audio Unit plug-ins to an audio engine to process, generate, and play audio.

## Topics

### Audio Unit setup
- [Creating an Audio Unit extension](./creating-an-audio-unit-extension.md)
  Build an extension by using an Xcode template.
- [class AVAudioUnit](./avaudiounit.md)
  A subclass of the audio node class that, processes audio either in real time or nonreal time, depending on the type of the audio unit.
### Component management
- [class AVAudioUnitComponent](./avaudiounitcomponent.md)
  An object that provides details about an audio unit.
- [class AVAudioUnitComponentManager](./avaudiounitcomponentmanager.md)
  An object that provides a way to search and query audio components that the system registers.
### Audio effects
- [class AVAudioUnitEQ](./avaudiouniteq.md)
  An object that implements a multiband equalizer.
- [class AVAudioUnitDistortion](./avaudiounitdistortion.md)
  An object that implements a multistage distortion effect.
- [class AVAudioUnitDelay](./avaudiounitdelay.md)
  An object that implements a delay effect.
- [class AVAudioUnitReverb](./avaudiounitreverb.md)
  An object that implements a reverb effect.
- [class AVAudioUnitEffect](./avaudiouniteffect.md)
  An object that processes audio in real time.
### Time effects
- [class AVAudioUnitTimePitch](./avaudiounittimepitch.md)
  An object that provides a good-quality playback rate and pitch shifting independently of each other.
- [class AVAudioUnitVarispeed](./avaudiounitvarispeed.md)
  An object that allows control of the playback rate.
- [class AVAudioUnitTimeEffect](./avaudiounittimeeffect.md)
  An object that processes audio in nonreal time.
### Audio generation
- [class AVAudioUnitGenerator](./avaudiounitgenerator.md)
  An object that generates audio output.
### MIDI instruments
- [class AVAudioUnitMIDIInstrument](./avaudiounitmidiinstrument.md)
  An object that represents music devices or remote instruments.

## See Also

### Audio Unit plug-ins and effects
- [Creating custom audio effects](./creating-custom-audio-effects.md)
  Add custom audio-effect processing to apps like Logic Pro X and GarageBand by creating Audio Unit (AU) plug-ins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/audio-units)*