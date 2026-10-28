# SetAvailableStreamFormats

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the available stream formats to an array of audio stream basic descriptions.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetAvailableStreamFormats(const IOUserAudioStreamBasicDescription *in_formats, uint32_t in_num_formats);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

If successful, changing the available formats sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_formats`: A pointer to a buffer of `IOUserAudioStreamBasicDescription` instances, with a size of `in_num_formats`.
- `in_num_formats`: The number of stream descriptions in `in_formats`.

## See Also

### Working with Stream Formats
- [SetCurrentStreamFormat](./setcurrentstreamformat.md)
  Sets the current stream format to a given audio stream basic description.
- [GetCurrentStreamFormat](./getcurrentstreamformat.md)
  Returns the current stream format, as an audio stream basic description.
- [GetAvailableStreamFormats](./getavailablestreamformats.md)
  Returns the available stream formats as an array of audio stream basic descriptions.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/setavailablestreamformats)*