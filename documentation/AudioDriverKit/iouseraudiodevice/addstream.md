# AddStream

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Adds an audio stream to the device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t AddStream(IOUserAudioStream *in_stream);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

If adding the stream succeeds, the stream’s reference count increments by one.

## Parameters

- `in_stream`: The stream to add to the device.

## See Also

### Working with Audio Streams
- [RemoveStream](./removestream.md)
  Removes an audio stream from the device.
- [IOUserAudioStream](../iouseraudiostream.md)
  An audio object that performs I/O for an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/addstream)*