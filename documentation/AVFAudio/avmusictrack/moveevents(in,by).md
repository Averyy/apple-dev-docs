# moveEvents(in:by:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Moves the beat location of all events in the given beat range by the amount you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func moveEvents(in range: AVBeatRange, by beatAmount: AVMusicTimeStamp)
```

```objc
- (void) moveEventsInRange:(AVBeatRange) range byAmount:(AVMusicTimeStamp) beatAmount;
```

## Parameters

- `range`: The range of beats.
- `beatAmount`: The amount of beats to shift each event.

## See Also

### Adding and clearing events
- [func addEvent(AVMusicEvent, at: AVMusicTimeStamp)](./addevent%28_,at%29.md)
  Adds a music event to a track at the time you specify.
- [func clearEvents(in: AVBeatRange)](./clearevents%28in%29.md)
  Removes all events in the given beat range from the music track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/moveevents(in:by:))*