# RemoveStream

**Framework**: AudioDriverKit  
**Kind**: method

Removes an audio stream from the device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t RemoveStream(IOUserAudioStream * in_stream);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If removing the stream succeeds, the stream’s reference count decrements by one.

## Parameters

- `in_stream`: The stream to remove from the device.

## See Also

- [AddStream](iouseraudiodevice/addstream.md)
  Adds an audio stream to the device.
- [IOUserAudioStream](iouseraudiostream.md)
  An audio object that performs I/O for an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/removestream)*