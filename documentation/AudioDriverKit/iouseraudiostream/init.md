# init

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Initializes an instance of the audio stream class.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual bool init(IOUserAudioDriver *in_driver, IOUserAudioStreamDirection in_direction, IOMemoryDescriptor *in_io_memory_descriptor);
```

#### Return Value

`true` if initialization succeeded; `false` otherwise.

## Parameters

- `in_driver`: The [`IOUserAudioDriver`](../iouseraudiodriver.md) that owns this object.
- `in_direction`: A `IOUserAudioStreamDirection` for the stream’s direction: input or output.
- `in_io_memory_descriptor`: A pointer to a [`IOMemoryDescriptor`](../../DriverKit/iomemorydescriptor.md). The stream maps the descriptor’s buffer to the Host for doing audio I/O.

## See Also

### Creating an Audio Stream
- [Create](./create.md)
  Allocates and initializes an instance of the audio stream class.
- [IOUserAudioDriver](../iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/init)*