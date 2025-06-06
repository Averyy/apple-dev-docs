# IOUserAudioFormatID

**Framework**: AudioDriverKit  
**Kind**: enum

An enumeration of four character codes used to identify distinct audio data formats.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
enum IOUserAudioFormatID : uint32_t;
```

#### Discussion

Some audio formats require additional configurations as indicated by the [`mFormatFlags`](audiodriverkit/iouseraudiostreambasicdescription/mformatflags.md) field of the [`IOUserAudioStreamBasicDescription`](audiodriverkit/iouseraudiostreambasicdescription.md).

## Topics

### Pulse Code Modulation Formats
- [LinearPCM](audiodriverkit/iouseraudioformatid/linearpcm.md)
  The linear Pulse-Code Modulation (PCM) format.
- [AppleIMA4](audiodriverkit/iouseraudioformatid/appleima4.md)
  The Apple implementation of IMA 4:1 Adaptive Differential Pulse-Code Modulation (ADPCM) format.
- [DVIIntelIMA](audiodriverkit/iouseraudioformatid/dviintelima.md)
  The DVI/Intel IMA Adaptive Differential Pulse-Code Modulation (ADPCM) format.
### Narrowband Formats
- [ALaw](audiodriverkit/iouseraudioformatid/alaw.md)
  The aLaw 2:1 format.
- [ULaw](audiodriverkit/iouseraudioformatid/ulaw.md)
  The µLaw 2:1 format.
- [MicrosoftGSM](audiodriverkit/iouseraudioformatid/microsoftgsm.md)
  The Microsoft GSM 6.10 format.
### AC-3 Formats
- [AC3](audiodriverkit/iouseraudioformatid/ac3.md)
  The AC-3 format.
- [AC360958](audiodriverkit/iouseraudioformatid/ac360958.md)
  The AC-3 format, packaged for transport over an IEC 60958-compliant digital audio interface.
- [EnhancedAC3](audiodriverkit/iouseraudioformatid/enhancedac3.md)
  The Enhanced AC-3 format.
### Apple Lossless Formats
- [AppleLossless](audiodriverkit/iouseraudioformatid/applelossless.md)
  The Apple Lossless format.
### AMR Speech Formats
- [AMR](audiodriverkit/iouseraudioformatid/amr.md)
  The AMR Narrow Band speech codec.
- [AMR_WB](audiodriverkit/iouseraudioformatid/amr_wb.md)
  The AMR Wide Band speech codec.
### MPEG-4 Formats
- [MPEG4AAC](audiodriverkit/iouseraudioformatid/mpeg4aac.md)
  The MPEG-4 Low Complexity AAC audio object format.
- [MPEG4AAC_HE](audiodriverkit/iouseraudioformatid/mpeg4aac_he.md)
  The MPEG-4 High Efficiency AAC audio object format.
- [MPEG4AAC_LD](audiodriverkit/iouseraudioformatid/mpeg4aac_ld.md)
  The MPEG-4 AAC Low Delay audio object format.
- [MPEG4AAC_ELD](audiodriverkit/iouseraudioformatid/mpeg4aac_eld.md)
  The MPEG-4 AAC Enhanced Low Delay audio object format.
- [MPEG4AAC_ELD_SBR](audiodriverkit/iouseraudioformatid/mpeg4aac_eld_sbr.md)
  The MPEG-4 AAC Enhanced Low Delay audio object with SBR extension layer format.
- [MPEG4AAC_HE_V2](audiodriverkit/iouseraudioformatid/mpeg4aac_he_v2.md)
  The MPEG-4 High Efficiency AAC Version 2 audio object format.
- [MPEG4AAC_ELD_V2](audiodriverkit/iouseraudioformatid/mpeg4aac_eld_v2.md)
  The MPEG-4 AAC Enhanced Low Delay Version 2 audio object format.
- [MPEG4AAC_Spatial](audiodriverkit/iouseraudioformatid/mpeg4aac_spatial.md)
  The MPEG-4 Spatial Audio audio object format.
- [MPEG4CELP](audiodriverkit/iouseraudioformatid/mpeg4celp.md)
  The MPEG-4 Code Excited Linear Prediction (CELP) audio object format.
- [MPEG4HVXC](audiodriverkit/iouseraudioformatid/mpeg4hvxc.md)
  The MPEG-4 Harmonic Vector eXcitation Coding (HVXC) audio object format.
- [MPEG4TwinVQ](audiodriverkit/iouseraudioformatid/mpeg4twinvq.md)
  MPEG-4 TwinVQ audio object format.
### Other MPEG Formats
- [MPEGLayer1](audiodriverkit/iouseraudioformatid/mpeglayer1.md)
  The MPEG-1/2, Layer 1 audio format.
- [MPEGLayer2](audiodriverkit/iouseraudioformatid/mpeglayer2.md)
  The MPEG-1/2, Layer 2 audio format.
- [MPEGLayer3](audiodriverkit/iouseraudioformatid/mpeglayer3.md)
  The MPEG-1/2, Layer 3 audio format.
- [MPEGD_USAC](audiodriverkit/iouseraudioformatid/mpegd_usac.md)
  The MPEG-D Unified Speech and Audio Coding format.
### Non-Sample Formats
- [MIDIStream](audiodriverkit/iouseraudioformatid/midistream.md)
  A format for a stream of MIDI packet lists.
- [ParameterValueStream](audiodriverkit/iouseraudioformatid/parametervaluestream.md)
  A format for a side-chain of 32-bit floating-point data.
- [TimeCode](audiodriverkit/iouseraudioformatid/timecode.md)
  A format for a stream of time stamps.
### MACE Formats
- [MACE3](audiodriverkit/iouseraudioformatid/mace3.md)
  The MACE 3:1 format.
- [MACE6](audiodriverkit/iouseraudioformatid/mace6.md)
  The MACE 6:1 format.
### QDesign Music Formats
- [QDesign](audiodriverkit/iouseraudioformatid/qdesign.md)
  The QDesign music format.
- [QDesign2](audiodriverkit/iouseraudioformatid/qdesign2.md)
  The QDesign2 music format.
### Qualcomm Formats
- [QUALCOMM](audiodriverkit/iouseraudioformatid/qualcomm.md)
  The QUALCOMM PureVoice format.
### AES-3 Formats
- [AES3](audiodriverkit/iouseraudioformatid/aes3.md)
  The AES3-2003 format.
### Other Lossless Formats
- [FLAC](audiodriverkit/iouseraudioformatid/flac.md)
  The Free Lossless Audio Codec format.
### Audiobook Formats
- [Audible](audiodriverkit/iouseraudioformatid/audible.md)
  The Audible audiobooks format.
### Open-Source Formats
- [Opus](audiodriverkit/iouseraudioformatid/opus.md)
  The Opus codec format.
- [iLBC](audiodriverkit/iouseraudioformatid/ilbc.md)
  The internet Low Bitrate Codec (iLBC) narrowband speech format.

## See Also

- [mFormatID](audiodriverkit/iouseraudiostreambasicdescription/mformatid.md)
  The audio format identifier indicating the general kind of data in the stream.
- [mFormatFlags](audiodriverkit/iouseraudiostreambasicdescription/mformatflags.md)
  Audio format flags for the stream’s format.
- [IOUserAudioFormatFlags](audiodriverkit/iouseraudioformatflags.md)
  Flag values that provide more information about the format used by an audio stream basic description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatid)*