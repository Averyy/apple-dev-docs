# playerTime(forNodeTime:)

**Framework**: AVFAudio  
**Kind**: method

Converts from node time to player time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func playerTime(forNodeTime nodeTime: AVAudioTime) -> AVAudioTime?
```

#### Return Value

A time relative to the player’s start time, or `nil` if the player isn’t playing.

#### Discussion

For more information about this method and its inverse [`nodeTime(forPlayerTime:)`](avaudioplayernode/nodetime(forplayertime:).md), see [`Player Timeline`](avaudioplayernode#Player-Timeline.md).

## Parameters

- `nodeTime`: The node time.

## See Also

- [func nodeTime(forPlayerTime: AVAudioTime) -> AVAudioTime?](avaudioplayernode/nodetime(forplayertime:).md)
  Converts from player time to node time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/playertime(fornodetime:))*