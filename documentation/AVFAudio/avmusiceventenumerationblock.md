# AVMusicEventEnumerationBlock

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

A type you use to enumerate and remove music events, if necessary.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias AVMusicEventEnumerationBlock = (AVMusicEvent, UnsafeMutablePointer<AVMusicTimeStamp>, UnsafeMutablePointer<ObjCBool>) -> Void
```

```c
typedef void (^)(AVMusicEvent *, double *, _Bool *) AVMusicEventEnumerationBlock;
```

## Discussion

You use this type when you use [`enumerateEvents(in:using:)`](./avmusictrack/enumerateevents%28in,using%29.md). If you modify `event` or `timeStamp`, you change the corresponding value in the track event.

## Parameters

- `event`: The music event the block returns.
- `timeStamp`: The beat position of the event in the music track.
- `removeEvent`: A value that determines whether to remove the event from the track.

## See Also

### Iterating over events
- [func enumerateEvents(in: AVBeatRange, using: (AVMusicEvent, UnsafeMutablePointer<AVMusicTimeStamp>, UnsafeMutablePointer<ObjCBool>) -> Void)](./avmusictrack/enumerateevents%28in,using%29.md)
  Iterates through the music events within the track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusiceventenumerationblock)*