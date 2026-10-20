# HasMIDI

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates the box’s MIDI support.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
bool HasMIDI();
```

#### Return Value

`true` if the box supports MIDI; `false` otherwise.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

### Determining Media Support
- [SetHasAudio](./sethasaudio.md)
  Sets a Boolean value that indicates the box’s audio support.
- [HasAudio](./hasaudio.md)
  Returns a Boolean value that indicates the box’s audio support.
- [SetHasVideo](./sethasvideo.md)
  Sets a Boolean value that indicates the box’s video support.
- [HasVideo](./hasvideo.md)
  Returns a Boolean value that indicates the box’s video support.
- [SetHasMIDI](./sethasmidi.md)
  Sets a Boolean value that indicates the box’s MIDI support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/hasmidi)*