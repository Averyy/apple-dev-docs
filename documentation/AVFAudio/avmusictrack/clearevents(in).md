# clearEvents(in:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Removes all events in the given beat range from the music track.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func clearEvents(in range: AVBeatRange)
```

```objc
- (void) clearEventsInRange:(AVBeatRange) range;
```

#### Discussion

The system won’t modify the events outside of the range you specify.

## Parameters

- `range`: The range of beats.

## See Also

### Adding and clearing events
- [func addEvent(AVMusicEvent, at: AVMusicTimeStamp)](./addevent%28_,at%29.md)
  Adds a music event to a track at the time you specify.
- [func moveEvents(in: AVBeatRange, by: AVMusicTimeStamp)](./moveevents%28in,by%29.md)
  Moves the beat location of all events in the given beat range by the amount you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/clearevents(in:))*