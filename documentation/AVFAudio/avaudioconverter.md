# AVAudioConverter

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

An object that converts streams of audio between formats.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioConverter
```

```objc
@interface AVAudioConverter : NSObject
```

#### Overview

The audio converter class transforms audio between file formats and audio encodings.

Supported transformations include:

- PCM float, integer, or bit depth conversions
- PCM sample rate conversion
- PCM interleaving and deinterleaving
- Encoding PCM to compressed formats
- Decoding compressed formats to PCM

A single audio converter instance may perform more than one of the above transformations.

## Topics

### Creating an audio converter
- [init?(from: AVAudioFormat, to: AVAudioFormat)](./avaudioconverter/init%28from,to%29.md)
  Creates an audio converter object from the specified input and output formats.
### Converting audio formats
- [func convert(to: AVAudioBuffer, error: NSErrorPointer, withInputFrom: (AVAudioPacketCount, UnsafeMutablePointer<AVAudioConverterInputStatus>) -> AVAudioBuffer?) -> AVAudioConverterOutputStatus](./avaudioconverter/convert%28to,error,withinputfrom%29.md)
  Performs a conversion between audio formats, if the system supports it.
- [typealias AVAudioConverterInputBlock](./avaudioconverterinputblock.md)
  A block to get input data for conversion, as necessary.
- [func convert(to: AVAudioPCMBuffer, from: AVAudioPCMBuffer) throws](./avaudioconverter/convert%28to,from%29.md)
  Performs a basic conversion between audio formats that doesn’t involve converting codecs or sample rates.
- [enum AVAudioConverterInputStatus](./avaudioconverterinputstatus.md)
  An option that indicates the status of an audio converter input block.
- [enum AVAudioConverterOutputStatus](./avaudioconverteroutputstatus.md)
  An option that indicates the return status of an audio converter method.
### Resetting an audio converter
- [func reset()](./avaudioconverter/reset%28%29.md)
  Resets the converter so you can convert a new audio stream.
### Getting audio converter properties
- [var channelMap: [NSNumber]](./avaudioconverter/channelmap.md)
  An array of integers that indicates which input to derive each output from.
- [var dither: Bool](./avaudioconverter/dither.md)
  A Boolean value that indicates whether dither is on.
- [var downmix: Bool](./avaudioconverter/downmix.md)
  A Boolean value that indicates whether the framework mixes the channels instead of remapping.
- [var inputFormat: AVAudioFormat](./avaudioconverter/inputformat.md)
  The format of the input audio stream.
- [var outputFormat: AVAudioFormat](./avaudioconverter/outputformat.md)
  The format of the output audio stream.
- [var magicCookie: Data?](./avaudioconverter/magiccookie.md)
  An object that contains metadata for encoders and decoders.
- [var maximumOutputPacketSize: Int](./avaudioconverter/maximumoutputpacketsize.md)
  The maximum size of an output packet, in bytes.
### Getting bit rate properties
- [var applicableEncodeBitRates: [NSNumber]?](./avaudioconverter/applicableencodebitrates.md)
  An array of bit rates the framework applies during encoding according to the current formats and settings.
- [var availableEncodeBitRates: [NSNumber]?](./avaudioconverter/availableencodebitrates.md)
  An array of all bit rates the codec provides when encoding.
- [var availableEncodeChannelLayoutTags: [NSNumber]?](./avaudioconverter/availableencodechannellayouttags.md)
  An array of all output channel layout tags the codec provides when encoding.
- [var bitRate: Int](./avaudioconverter/bitrate.md)
  The bit rate, in bits per second.
- [var bitRateStrategy: String?](./avaudioconverter/bitratestrategy.md)
  A key value constant the framework uses during encoding.
### Getting sample rate properties
- [var sampleRateConverterQuality: Int](./avaudioconverter/samplerateconverterquality.md)
  A sample rate converter algorithm key value.
- [var sampleRateConverterAlgorithm: String?](./avaudioconverter/samplerateconverteralgorithm.md)
  The priming method the sample rate converter or decoder uses.
- [var applicableEncodeSampleRates: [NSNumber]?](./avaudioconverter/applicableencodesamplerates.md)
  An array of output sample rates that the converter applies according to the current formats and settings, when encoding.
- [var availableEncodeSampleRates: [NSNumber]?](./avaudioconverter/availableencodesamplerates.md)
  An array of all output sample rates the codec provides when encoding.
### Getting priming information
- [var primeInfo: AVAudioConverterPrimeInfo](./avaudioconverter/primeinfo.md)
  The number of priming frames the converter uses.
- [var primeMethod: AVAudioConverterPrimeMethod](./avaudioconverter/primemethod.md)
  The priming method the sample rate converter or decoder uses.
- [struct AVAudioConverterPrimeInfo](./avaudioconverterprimeinfo.md)
  Priming information for audio conversion.
- [enum AVAudioConverterPrimeMethod](./avaudioconverterprimemethod.md)
  Options for the prime method property.
### Managing packet dependencies
- [var audioSyncPacketFrequency: Int](./avaudioconverter/audiosyncpacketfrequency.md)
- [var contentSource: AVAudioContentSource](./avaudioconverter/contentsource.md)
- [enum AVAudioContentSource](./avaudiocontentsource.md)
- [var dynamicRangeControlConfiguration: AVAudioDynamicRangeControlConfiguration](./avaudioconverter/dynamicrangecontrolconfiguration.md)
- [enum AVAudioDynamicRangeControlConfiguration](./avaudiodynamicrangecontrolconfiguration.md)
### Initializers
- [init?(fromFormat: AVAudioFormat, toFormat: AVAudioFormat)](./avaudioconverter/init%28fromformat,toformat%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Audio data
- [class AVAudioFile](./avaudiofile.md)
  An object that represents an audio file that the system can open for reading or writing.
- [class AVAudioPCMBuffer](./avaudiopcmbuffer.md)
  An object that represents an audio buffer you use with PCM audio formats.
- [class AVAudioCompressedBuffer](./avaudiocompressedbuffer.md)
  An object that represents an audio buffer that you use for compressed audio formats.
- [struct AVReadOnlyAudioPCMBuffer](./avreadonlyaudiopcmbuffer.md)
  A read-only, Sendable audio buffer for safe concurrent access.
- [class AVAudioBuffer](./avaudiobuffer.md)
  An object that represents a buffer of audio data with a format.
- [class AVAudioFormat](./avaudioformat.md)
  An object that describes the representation of an audio format.
- [class AVAudioChannelLayout](./avaudiochannellayout.md)
  An object that describes the roles of a set of audio channels.
- [class AVAudioTime](./avaudiotime.md)
  An object you use to represent a moment in time.
- [Audio settings](./audio-settings.md)
  Configure audio processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverter)*