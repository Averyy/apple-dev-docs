# nodeTime(forPlayerTime:)

**Framework**: AVFAudio  
**Kind**: method

Converts from player time to node time.

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
func nodeTime(forPlayerTime playerTime: AVAudioTime) -> AVAudioTime?
```

#### Return Value

A node time, or `nil` if the player isn’t playing.

#### Discussion

For more information about this method and its inverse [`playerTime(forNodeTime:)`](avaudioplayernode/playertime(fornodetime:).md), see [`Player Timeline`](avaudioplayernode#Player-Timeline.md).

## Parameters

- `playerTime`: A time relative to the player’s start time.

## See Also

- [func playerTime(forNodeTime: AVAudioTime) -> AVAudioTime?](avaudioplayernode/playertime(fornodetime:).md)
  Converts from node time to player time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/nodetime(forplayertime:))*