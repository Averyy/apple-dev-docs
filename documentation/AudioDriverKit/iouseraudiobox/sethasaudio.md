# SetHasAudio

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets a Boolean value that indicates the box’s audio support.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
kern_return_t SetHasAudio(bool in_has_audio);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

## Discussion

If successful, changing the audio support value sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_has_audio`: `true` if the box supports audio; otherwise, `false`.

## See Also

### Determining Media Support
- [HasAudio](./hasaudio.md)
  Returns a Boolean value that indicates the box’s audio support.
- [SetHasVideo](./sethasvideo.md)
  Sets a Boolean value that indicates the box’s video support.
- [HasVideo](./hasvideo.md)
  Returns a Boolean value that indicates the box’s video support.
- [SetHasMIDI](./sethasmidi.md)
  Sets a Boolean value that indicates the box’s MIDI support.
- [HasMIDI](./hasmidi.md)
  Returns a Boolean value that indicates the box’s MIDI support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/sethasaudio)*