# Audio Toolbox Debugging

**Framework**: Audio Toolbox  
**Role**: API Collection

Obtain the internal state of Core Audio objects during the development and debugging of your code.

## Overview

The `AudioToolbox.h` header file provides auxiliary functions for obtaining the internal state of a Core Audio object. Use these functions during development and debugging.

## Topics

### Audio Toolbox Debugging Functions
- [func CAShow(UnsafeMutableRawPointer)](./cashow%28_%29.md)
  Prints the internal state of an object to `stdio`.
- [func CAShowFile(UnsafeMutableRawPointer, UnsafeMutablePointer<FILE>)](./cashowfile%28_,_%29.md)
  Prints the internal state of an object to a file.
### Instrument Functions
- [func CopyNameFromSoundBank(CFURL, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./copynamefromsoundbank%28_,_%29.md)
  Copies the name of a sound bank from a sound bank file at a specified URL.
- [func CopyInstrumentInfoFromSoundBank(CFURL, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](./copyinstrumentinfofromsoundbank%28_,_%29.md)
- [var kInstrumentInfoKey_LSB: String](./kinstrumentinfokey_lsb.md)
- [var kInstrumentInfoKey_MSB: String](./kinstrumentinfokey_msb.md)
- [var kInstrumentInfoKey_Name: String](./kinstrumentinfokey_name.md)
- [var kInstrumentInfoKey_Program: String](./kinstrumentinfokey_program.md)
- [GetNameFromSoundBank](./getnamefromsoundbank.md)
  Gets the name of a sound bank from a sound bank file.
### Constants
- [var AUDIO_TOOLBOX_VERSION: Int32](./audio_toolbox_version.md)

## See Also

### Utilities
- [Analyzing audio performance with Instruments](./analyzing-audio-performance-with-instruments.md)
  Ensure a smooth and immersive audio experience in your apps using Audio System Trace.
- [Audio Converter Services](./audio-converter-services.md)
  Convert between linear PCM audio formats, and between linear PCM and compressed formats.
- [Audio Session Support](./audio-session-support.md)
  Describe the properties that you associate with audio sessions and audio routes.
- [Workgroup Management](./workgroup-management.md)
  Coordinate the activity of custom real-time audio threads with those of the system and other processes.
- [Audio Codec](./audio-codec.md)
  Translate audio data from one format to another.
- [Clock Utilities](./clock-utilities.md)
  Manage time-related information associated with audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-toolbox-debugging)*