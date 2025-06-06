# Audio Unit

**Framework**: Audio Unit  
**Kind**: module

Add sophisticated audio manipulation and processing capabilities to your app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

#### Overview

The Audio Unit framework provides interfaces for hosting either version 2 or version 3 audio units and implementing version 3 audio processing plug-ins known as Audio Unit extensions. Developers implementing version 3 audio units should subclass the [`AUAudioUnit`](https://developer.apple.com/documentation/AudioToolbox/AUAudioUnit) class.

Version 3 Audio Unit extensions can be used on iOS, tvOS, and macOS by host apps and distributed via the App Store.

## Topics

### Variables
- [var AUDIO_UNIT_VERSION: Int32](audio_unit_version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/AudioUnit)*