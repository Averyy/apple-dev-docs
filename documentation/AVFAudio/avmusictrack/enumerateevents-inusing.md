# enumerateEvents(in:using:)

**Framework**: AVFAudio  
**Kind**: method

Iterates through the music events within the track.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func enumerateEvents(in range: AVBeatRange, using block: (AVMusicEvent, UnsafeMutablePointer<AVMusicTimeStamp>, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

Examine each event the block returns by using [`isKind(of:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isKind(of:)) to determine the subclass, and then cast and access it accordingly.

The iteration may continue after removing an event.

The event object returned through the block won’t be the same instances you add to the [`AVMusicTrack`](avmusictrack.md), though the content is identical.

## Parameters

- `range`: The range to iterate through.
- `block`: The block to call for each event.

## See Also

- [typealias AVMusicEventEnumerationBlock](avmusiceventenumerationblock.md)
  A type you use to enumerate and remove music events, if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmusictrack/enumerateevents(in:using:))*