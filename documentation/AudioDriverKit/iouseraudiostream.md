# IOUserAudioStream

**Framework**: AudioDriverKit  
**Kind**: class

An audio object that performs I/O for an audio device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
class IOUserAudioStream;
```

#### Overview

[`IOUserAudioStream`](iouseraudiostream.md) allocates memory descriptors that the host uses for running I/O. An [`IOUserAudioDevice`](iouseraudiodevice.md) uses an [`IOUserAudioStream`](iouseraudiostream.md) instance to perform I/O. Changes to the device that owns a stream may update formats on the underlying stream, which you handle by overriding [`HandleChangeCurrentStreamFormat`](iouseraudiostream/handlechangecurrentstreamformat.md) and [`HandleChangeStreamIsActive`](iouseraudiostream/handlechangestreamisactive.md).

## Topics

### Creating an Audio Stream
- [Create](iouseraudiostream/create.md)
  Allocates and initializes an instance of the audio stream class.
- [init](iouseraudiostream/init.md)
  Initializes an instance of the audio stream class.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.
### Freeing an Audio Stream
- [free](iouseraudiostream/free.md)
  Frees the audio stream.
### Getting Information About the Class
- [GetClassID](iouseraudiostream/getclassid.md)
  Gets the audio class identifier of the object.
- [GetBaseClassID](iouseraudiostream/getbaseclassid.md)
  Gets the audio class identifier of the base class object.
- [IOUserAudioClassID](audiodriverkit/iouseraudioclassid.md)
  An identifier for the type of audio object.
### Performing I/O
- [StartIO](iouseraudiostream/startio.md)
  Tells the stream to start I/O.
- [StopIO](iouseraudiostream/stopio.md)
  Tells the stream to stop I/O.
- [IOUserAudioStartStopFlags](audiodriverkit/iouseraudiostartstopflags.md)
  Values that indicate I/O starts or stops.
### Working with Stream Formats
- [SetCurrentStreamFormat](iouseraudiostream/setcurrentstreamformat.md)
  Sets the current stream format to a given audio stream basic description.
- [GetCurrentStreamFormat](iouseraudiostream/getcurrentstreamformat.md)
  Returns the current stream format, as an audio stream basic description.
- [SetAvailableStreamFormats](iouseraudiostream/setavailablestreamformats.md)
  Sets the available stream formats to an array of audio stream basic descriptions.
- [GetAvailableStreamFormats](iouseraudiostream/getavailablestreamformats.md)
  Returns the available stream formats as an array of audio stream basic descriptions.
- [GetNumberAvailableStreamFormats](iouseraudiostream/getnumberavailablestreamformats.md)
  Returns the number of available stream formats.
- [IOUserAudioStreamBasicDescription](audiodriverkit/iouseraudiostreambasicdescription.md)
  A structure that encapsulates all of the information for describing the basic format properties of a stream of audio data.
- [GetStreamDirection](iouseraudiostream/getstreamdirection.md)
  Gets the direction of the stream: input or output.
- [IOUserAudioStreamDirection](audiodriverkit/iouseraudiostreamdirection.md)
  A type representing the direction of audio flow.
- [SetStreamIsActive](iouseraudiostream/setstreamisactive.md)
  Sets a Boolean value that indicates whether the stream is active and doing I/O.
- [GetStreamIsActive](iouseraudiostream/getstreamisactive.md)
  Gets a value that indicates whether the stream is active and doing I/O.
### Working with Stream Terminals
- [SetTerminalType](iouseraudiostream/setterminaltype.md)
  Sets the terminal type of the stream.
- [GetTerminalType](iouseraudiostream/getterminaltype.md)
  Gets the terminal type of the stream.
- [IOUserAudioStreamTerminalType](audiodriverkit/iouseraudiostreamterminaltype.md)
  Constants that describe the terminal type of an audio stream.
### Working with Memory Descriptors
- [GetIOMemoryDescriptor](iouseraudiostream/getiomemorydescriptor.md)
  Gets the memory descriptor the stream uses for I/O.
- [SetIOMemoryDescriptor](iouseraudiostream/setiomemorydescriptor.md)
  Sets the memory descriptor the stream uses for I/O.
### Managing Stream Changes
- [HandleChangeCurrentStreamFormat](iouseraudiostream/handlechangecurrentstreamformat.md)
  Tells the stream the format is changing.
- [HandleChangeStreamIsActive](iouseraudiostream/handlechangestreamisactive.md)
  Tells the stream the activity state is changing.
- [DeviceSampleRateChanged](iouseraudiostream/devicesampleratechanged.md)
  Updates stream formats, in response to the owning audio device changing its sample rate.
### Instance Methods
- [GetLatency](iouseraudiostream/getlatency.md)
- [GetStartingChannel](iouseraudiostream/getstartingchannel.md)
- [SetLatency](iouseraudiostream/setlatency.md)
- [SetStartingChannel](iouseraudiostream/setstartingchannel.md)

## Relationships

### Inherits From
- [IOUserAudioObject](iouseraudioobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream)*