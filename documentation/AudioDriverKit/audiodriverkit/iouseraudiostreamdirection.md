# IOUserAudioStreamDirection

**Framework**: AudioDriverKit  
**Kind**: enum

A type representing the direction of audio flow.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
enum IOUserAudioStreamDirection : uint32_t;
```

#### Discussion

Use `0` for output, and `1` for input.

## Topics

### Enumeration Cases
- [Input](audiodriverkit/iouseraudiostreamdirection/input.md)
- [Output](audiodriverkit/iouseraudiostreamdirection/output.md)

## See Also

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
- [SetStreamIsActive](iouseraudiostream/setstreamisactive.md)
  Sets a Boolean value that indicates whether the stream is active and doing I/O.
- [GetStreamIsActive](iouseraudiostream/getstreamisactive.md)
  Gets a value that indicates whether the stream is active and doing I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudiostreamdirection)*