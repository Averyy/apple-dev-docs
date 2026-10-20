# SetHasVideo

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets a Boolean value that indicates the box’s video support.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetHasVideo(bool in_has_video);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

If successful, changing the video support value sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_has_video`: `true` if the box supports video; otherwise, `false`.

## See Also

### Determining Media Support
- [SetHasAudio](./sethasaudio.md)
  Sets a Boolean value that indicates the box’s audio support.
- [HasAudio](./hasaudio.md)
  Returns a Boolean value that indicates the box’s audio support.
- [HasVideo](./hasvideo.md)
  Returns a Boolean value that indicates the box’s video support.
- [SetHasMIDI](./sethasmidi.md)
  Sets a Boolean value that indicates the box’s MIDI support.
- [HasMIDI](./hasmidi.md)
  Returns a Boolean value that indicates the box’s MIDI support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/sethasvideo)*