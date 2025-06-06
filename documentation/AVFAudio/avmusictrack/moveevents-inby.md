# moveEvents(in:by:)

**Framework**: AVFAudio  
**Kind**: method

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

## Parameters

- `range`: The range of beats.
- `beatAmount`: The amount of beats to shift each event.

## See Also

- [func addEvent(AVMusicEvent, at: AVMusicTimeStamp)](avmusictrack/addevent(_:at:).md)
  Adds a music event to a track at the time you specify.
- [func clearEvents(in: AVBeatRange)](avmusictrack/clearevents(in:).md)
  Removes all events in the given beat range from the music track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/moveevents(in:by:))*