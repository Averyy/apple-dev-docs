# Create

**Framework**: AudioDriverKit  
**Kind**: method

Allocates and initializes an instance of the audio stream class.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
static OSSharedPtr<IOUserAudioStream> Create(IOUserAudioDriver * in_driver, IOUserAudioStreamDirection in_direction, IOMemoryDescriptor * in_io_memory_descriptor);
```

#### Return Value

A poiner to an [`IOUserAudioStream`](iouseraudiostream.md), if allocation and initialization succeeded.

#### Discussion

If you subclass [`IOUserAudioStream`](iouseraudiostream.md) to override this class’ behavior, don’t use [`Create`](iouseraudiostream/create.md) to allocate and initialize the custom subclass.

## Parameters

- `in_driver`: The   that owns this object.
- `in_direction`: A   for the stream’s direction: input or output.
- `in_io_memory_descriptor`: A pointer to a  . The stream maps the descriptor’s buffer to the host for doing audio I/O.

## See Also

- [init](iouseraudiostream/init.md)
  Initializes an instance of the audio stream class.
- [IOUserAudioDriver](iouseraudiodriver.md)
  A DriverKit provider object that manages communications with an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiostream/create)*