# AudioConverterNew(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Creates a new audio converter object based on specified audio formats.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioConverterNew(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ outAudioConverter: UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus
```

#### Return Value

A  result code.

#### Discussion

For a pair of linear PCM formats, the following conversions are supported:

- Addition and removal of channels, when the input and output format `mChannelsPerFrame` fields do not match. Channels may also be reordered and removed using the `kAudioConverterChannelMap` property.
- Sample rate conversion.
- Interleaving and deinterleaving, when the input and output format `(mFormatFlags & kAudioFormatFlagIsNonInterleaved)` values do not match.
- Conversion between any pair of the following formats:
- 8-bit integer, signed or unsigned.
- 16-, 24-, or 32-bit integer, big- or little-endian. Other integral bit depths, if high-aligned and nonpacked, are also supported
- 32- and 64-bit floating point, big- or little-endian.

Encoding and decoding between linear PCM and compressed formats is supported. Functions in Audio Format Services (`AudioToolbox/AudioFormat.h`) return information about the formats supported on a system. When using a codec, you can use any supported PCM format. The converter object performs any necessary additional conversion between your PCM format and the one created or consumed by the codec.

## Parameters

- `inSourceFormat`: The format of the source audio to be converted.
- `inDestinationFormat`: The destination format to which the audio is to be converted.
- `outAudioConverter`: On return, a new audio converter object.

## See Also

- [func AudioConverterNewSpecific(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UInt32, UnsafePointer<AudioClassDescription>, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](audioconverternewspecific(_:_:_:_:_:).md)
  Creates a new audio converter object using a specified codec.
- [func AudioConverterReset(AudioConverterRef) -> OSStatus](audioconverterreset(_:).md)
  Resets an audio converter object, clearing and flushing its buffers.
- [func AudioConverterDispose(AudioConverterRef) -> OSStatus](audioconverterdispose(_:).md)
  Disposes of an audio converter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverternew(_:_:_:))*