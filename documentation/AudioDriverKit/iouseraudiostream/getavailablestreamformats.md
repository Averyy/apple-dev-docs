# GetAvailableStreamFormats

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the available stream formats as an array of audio stream basic descriptions.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
size_t GetAvailableStreamFormats(IOUserAudioStreamBasicDescription *out_formats, size_t in_num_formats);
```

#### Return Value

The number of descriptions populated in the `out_formats` buffer.

#### Discussion

This method synchronizes by using the work queue created by the object.

## Parameters

- `out_formats`: A pointer to a buffer of type `IOUserAudioStreamBasicDescription`, with a size of `in_num_formats`. On return, this buffer contains the available formats.
- `in_num_formats`: The size of the `out_formats` buffer.

## See Also

### Working with Stream Formats
- [SetCurrentStreamFormat](./setcurrentstreamformat.md)
  Sets the current stream format to a given audio stream basic description.
- [GetCurrentStreamFormat](./getcurrentstreamformat.md)
  Returns the current stream format, as an audio stream basic description.
- [SetAvailableStreamFormats](./setavailablestreamformats.md)
  Sets the available stream formats to an array of audio stream basic descriptions.
- [GetNumberAvailableStreamFormats](./getnumberavailablestreamformats.md)
  Returns the number of available stream formats.
- [IOUserAudioStreamBasicDescription](../audiodriverkit-page/iouseraudiostreambasicdescription.md)
  A structure that encapsulates all of the information for describing the basic format properties of a stream of audio data.
- [GetStreamDirection](./getstreamdirection.md)
  Gets the direction of the stream: input or output.
- [IOUserAudioStreamDirection](../audiodriverkit-page/iouseraudiostreamdirection.md)
  A type representing the direction of audio flow.
- [SetStreamIsActive](./setstreamisactive.md)
  Sets a Boolean value that indicates whether the stream is active and doing I/O.
- [GetStreamIsActive](./getstreamisactive.md)
  Gets a value that indicates whether the stream is active and doing I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/getavailablestreamformats)*