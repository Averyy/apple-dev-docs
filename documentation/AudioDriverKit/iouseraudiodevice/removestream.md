# RemoveStream

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Removes an audio stream from the device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t RemoveStream(IOUserAudioStream *in_stream);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

If removing the stream succeeds, the stream’s reference count decrements by one.

## Parameters

- `in_stream`: The stream to remove from the device.

## See Also

### Working with Audio Streams
- [AddStream](./addstream.md)
  Adds an audio stream to the device.
- [IOUserAudioStream](../iouseraudiostream.md)
  An audio object that performs I/O for an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/removestream)*