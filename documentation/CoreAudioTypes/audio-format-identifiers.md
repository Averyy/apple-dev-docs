# Audio Format Identifiers

**Framework**: Core Audio Types

Identifiers for supported audio formats.

#### Overview

Use these identifiers to test for the presence of audio codecs on a system. If a given codec is present, you can use its identifier to specify that codec for data encoding or decoding, according to the capabilities of the codec. For more information, see [`Core Audio`](https://developer.apple.com/documentation/CoreAudio).

## Topics

### Format identifiers
- [var kAudioFormat60958AC3: AudioFormatID](kaudioformat60958ac3.md)
  A key that specifies the AC-3 codec, which provides data packaged for transport over an IEC 60958-compliant digital audio interface, and uses standard flags.
- [var kAudioFormatAC3: AudioFormatID](kaudioformatac3.md)
  A key that specifies the AC-3 codec, and uses no flags.
- [var kAudioFormatAES3: AudioFormatID](kaudioformataes3.md)
  A key that specifies the codec defined by the AES3-2003 standard, and uses no flags.
- [var kAudioFormatALaw: AudioFormatID](kaudioformatalaw.md)
  A key that specifies the A-law 2:1 codec, and uses no flags.
- [var kAudioFormatAMR: AudioFormatID](kaudioformatamr.md)
  A key that specifies the Adaptive Multi-Rate (AMR) narrow band speech codec, and uses no flags.
- [var kAudioFormatAMR_WB: AudioFormatID](kaudioformatamr_wb.md)
  A key that specifies the AMR Wideband speech codec, and uses no flags.
- [var kAudioFormatAppleIMA4: AudioFormatID](kaudioformatappleima4.md)
  A key that specifies Apple’s implementation of the IMA 4:1 ADPCM codec, and uses no flags.
- [var kAudioFormatAppleLossless: AudioFormatID](kaudioformatapplelossless.md)
  A key that specifies the Apple Lossless codec, and uses flags to indicate the bit depth of the source material.
- [var kAudioFormatAudible: AudioFormatID](kaudioformataudible.md)
  A key that specifies the codec for Audible audio books, and uses no flags.
- [var kAudioFormatDVIIntelIMA: AudioFormatID](kaudioformatdviintelima.md)
  A key that specifies the codec defined by DVI/Intel IMA ADPCM - ACM code 17, and uses no flags.
- [var kAudioFormatEnhancedAC3: AudioFormatID](kaudioformatenhancedac3.md)
  A key that specifies the Enhanced AC-3 codec, and uses no flags.
- [var kAudioFormatFLAC: AudioFormatID](kaudioformatflac.md)
  A key that specifies the Free Lossless Audio Codec (FLAC), and uses flags to indicate the bit depth of the source material.
- [var kAudioFormatLinearPCM: AudioFormatID](kaudioformatlinearpcm.md)
  A key that specifies the linear PCM codec, and uses the standard flags.
- [var kAudioFormatMACE3: AudioFormatID](kaudioformatmace3.md)
  A key that specifies the MACE 3:1 codec, and uses no flags.
- [var kAudioFormatMACE6: AudioFormatID](kaudioformatmace6.md)
  A key that specifies the MACE C:1 codec, and uses no flags.
- [var kAudioFormatMIDIStream: AudioFormatID](kaudioformatmidistream.md)
  A key that specifies the MIDI stream codec, and uses no flags.
- [var kAudioFormatMPEG4AAC: AudioFormatID](kaudioformatmpeg4aac.md)
  A key that specifies the MPEG-4 AAC Low Complexity codec, and uses no flags.
- [var kAudioFormatMPEG4AAC_ELD: AudioFormatID](kaudioformatmpeg4aac_eld.md)
  A key that specifies the MPEG-4 Enhanced Low Delay AAC codec, and uses no flags.
- [var kAudioFormatMPEG4AAC_ELD_SBR: AudioFormatID](kaudioformatmpeg4aac_eld_sbr.md)
  A key that specifies the MPEG-4 Enhanced Low Delay AAC codec with a spectral band replication (SBR) extension layer, and uses no flags.
- [var kAudioFormatMPEG4AAC_ELD_V2: AudioFormatID](kaudioformatmpeg4aac_eld_v2.md)
  A key that specifies the MPEG-4 Enhanced Low Delay AAC version 2 codec, and uses no flags.
- [var kAudioFormatMPEG4AAC_HE: AudioFormatID](kaudioformatmpeg4aac_he.md)
  A key that specifies the MPEG-4 High-Efficiency AAC codec, and uses no flags.
- [var kAudioFormatMPEG4AAC_HE_V2: AudioFormatID](kaudioformatmpeg4aac_he_v2.md)
  A key that specifies the MPEG-4 High-Efficiency AAC version 2 codec, and uses no flags.
- [var kAudioFormatMPEG4AAC_LD: AudioFormatID](kaudioformatmpeg4aac_ld.md)
  A key that specifies the MPEG-4 Low Delay AAC codec, and uses no flags.
- [var kAudioFormatMPEG4AAC_Spatial: AudioFormatID](kaudioformatmpeg4aac_spatial.md)
  A key that specifies the MPEG-4 Spatial Audio Coding codec, and uses no flags.
- [var kAudioFormatMPEG4CELP: AudioFormatID](kaudioformatmpeg4celp.md)
  A key that specifies the MPEG-4 CELP codec, and uses flags to indicate the specific kind of data.
- [var kAudioFormatMPEG4HVXC: AudioFormatID](kaudioformatmpeg4hvxc.md)
  A key that specifies the MPEG-4 HVXC codec, and uses no flags.
- [var kAudioFormatMPEG4TwinVQ: AudioFormatID](kaudioformatmpeg4twinvq.md)
  A key that specifies the MPEG-4 TwinVQ codec, and uses no flags.
- [var kAudioFormatMPEGD_USAC: AudioFormatID](kaudioformatmpegd_usac.md)
  A key that specifies the MPEG-D Unified Speech and Audio Coding codec, and uses no flags.
- [var kAudioFormatMPEGLayer1: AudioFormatID](kaudioformatmpeglayer1.md)
  A key that specifies the MPEG-1/2, Layer I audio codec, and uses no flags.
- [var kAudioFormatMPEGLayer2: AudioFormatID](kaudioformatmpeglayer2.md)
  A key that specifies the MPEG-1/2, Layer II audio codec, and uses no flags.
- [var kAudioFormatMPEGLayer3: AudioFormatID](kaudioformatmpeglayer3.md)
  A key that specifies the MPEG-1/2, Layer III audio codec, and uses no flags.
- [var kAudioFormatMicrosoftGSM: AudioFormatID](kaudioformatmicrosoftgsm.md)
  A key that specifies the Microsoft GSM 6.10 - ACM code 49 codec, and uses no flags.
- [var kAudioFormatOpus: AudioFormatID](kaudioformatopus.md)
  A key that specifies the Opus codec, and uses no flags.
- [var kAudioFormatParameterValueStream: AudioFormatID](kaudioformatparametervaluestream.md)
  A key that specifies the A side-chain of float 32 data that an audio unit provides for sending high-density parameter value control information, and uses no flags.
- [var kAudioFormatQDesign: AudioFormatID](kaudioformatqdesign.md)
  A key that specifies the QDesign music codec, and uses no flags.
- [var kAudioFormatQDesign2: AudioFormatID](kaudioformatqdesign2.md)
  A key that specifies the QDesign 2 music codec, and uses no flags.
- [var kAudioFormatQUALCOMM: AudioFormatID](kaudioformatqualcomm.md)
  A key that specifies the Qualcomm PureVoice codec, and uses no flags.
- [var kAudioFormatTimeCode: AudioFormatID](kaudioformattimecode.md)
  A key that specifies the A stream of audio timestamp structures, and uses audio timestamp flags.
- [var kAudioFormatULaw: AudioFormatID](kaudioformatulaw.md)
  A key that specifies the μ-Law 2:1 codec, and uses no flags.
- [var kAudioFormatiLBC: AudioFormatID](kaudioformatilbc.md)
  A key that specifies the internet Low Bitrate Codec (iLBC) narrow band speech codec, and uses no flags.

## See Also

- [struct AudioStreamBasicDescription](audiostreambasicdescription.md)
  A format specification for an audio stream.
- [struct AudioStreamPacketDescription](audiostreampacketdescription.md)
  A value that describes a packet in a buffer of audio data.
- [typealias AudioFormatFlags](audioformatflags.md)
  A type definition for audio format flags.
- [Audio Format Flags](audio-format-flags.md)
  Commonly used combinations of data format flags for an audio stream description.
- [typealias AudioFormatID](audioformatid.md)
  A type definition for audio format identifiers.
- [let kAudioStreamAnyRate: Float64](kaudiostreamanyrate.md)
  A value that indicates that an audio stream can use any sample rate.
- [enum MPEG4ObjectID](mpeg4objectid.md)
  Constants that define the type of MPEG-4 audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audio-format-identifiers)*