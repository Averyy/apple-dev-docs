# AVMusicEventEnumerationBlock

**Framework**: AVFAudio  
**Kind**: typealias

A type you use to enumerate and remove music events, if necessary.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias AVMusicEventEnumerationBlock = (AVMusicEvent, UnsafeMutablePointer<AVMusicTimeStamp>, UnsafeMutablePointer<ObjCBool>) -> Void
```

#### Discussion

You use this type when you use [`enumerateEvents(in:using:)`](avmusictrack/enumerateevents(in:using:).md). If you modify `event` or `timeStamp`, you change the corresponding value in the track event.

## Parameters

- `event`: The music event the block returns.
- `timeStamp`: The beat position of the event in the music track.
- `removeEvent`: A value that determines whether to remove the event from the track.

## See Also

- [func enumerateEvents(in: AVBeatRange, using: (AVMusicEvent, UnsafeMutablePointer<AVMusicTimeStamp>, UnsafeMutablePointer<ObjCBool>) -> Void)](avmusictrack/enumerateevents(in:using:).md)
  Iterates through the music events within the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusiceventenumerationblock)*