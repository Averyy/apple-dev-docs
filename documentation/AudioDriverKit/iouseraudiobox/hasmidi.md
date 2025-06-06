# HasMIDI

**Framework**: AudioDriverKit  
**Kind**: method

Returns a Boolean value that indicates the box’s MIDI support.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
bool HasMIDI();
```

#### Return Value

`true` if the box supports MIDI; `false` otherwise.

#### Discussion

This method synchronizes by using the work queue created by the object.

## See Also

- [SetHasAudio](iouseraudiobox/sethasaudio.md)
  Sets a Boolean value that indicates the box’s audio support.
- [HasAudio](iouseraudiobox/hasaudio.md)
  Returns a Boolean value that indicates the box’s audio support.
- [SetHasVideo](iouseraudiobox/sethasvideo.md)
  Sets a Boolean value that indicates the box’s video support.
- [HasVideo](iouseraudiobox/hasvideo.md)
  Returns a Boolean value that indicates the box’s video support.
- [SetHasMIDI](iouseraudiobox/sethasmidi.md)
  Sets a Boolean value that indicates the box’s MIDI support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiobox/hasmidi)*