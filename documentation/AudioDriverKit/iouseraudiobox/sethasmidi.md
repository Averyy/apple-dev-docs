# SetHasMIDI

**Framework**: AudioDriverKit  
**Kind**: method

Sets a Boolean value that indicates the box’s MIDI support.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t SetHasMIDI(bool in_has_midi);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

If successful, changing the MIDI support value sends a notification to the host to update the object state.

This method synchronizes by using the work queue created by the object.

## Parameters

- `in_has_midi`:   if the box supports MIDI; otherwise,  .

## See Also

- [SetHasAudio](iouseraudiobox/sethasaudio.md)
  Sets a Boolean value that indicates the box’s audio support.
- [HasAudio](iouseraudiobox/hasaudio.md)
  Returns a Boolean value that indicates the box’s audio support.
- [SetHasVideo](iouseraudiobox/sethasvideo.md)
  Sets a Boolean value that indicates the box’s video support.
- [HasVideo](iouseraudiobox/hasvideo.md)
  Returns a Boolean value that indicates the box’s video support.
- [HasMIDI](iouseraudiobox/hasmidi.md)
  Returns a Boolean value that indicates the box’s MIDI support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/sethasmidi)*