# GetNumberAvailableStreamFormats

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the number of available stream formats.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
size_t GetNumberAvailableStreamFormats();
```

## Return Value

The number of available stream formats, as a [`size_t`](../../kernel/size_t.md).

## Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Working with Stream Formats
- [SetCurrentStreamFormat](./setcurrentstreamformat.md)
  Sets the current stream format to a given audio stream basic description.
- [GetCurrentStreamFormat](./getcurrentstreamformat.md)
  Returns the current stream format, as an audio stream basic description.
- [SetAvailableStreamFormats](./setavailablestreamformats.md)
  Sets the available stream formats to an array of audio stream basic descriptions.
- [GetAvailableStreamFormats](./getavailablestreamformats.md)
  Returns the available stream formats as an array of audio stream basic descriptions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/getnumberavailablestreamformats)*