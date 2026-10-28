# nodeTime(forPlayerTime:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (AVAudioTime *) nodeTimeForPlayerTime:(AVAudioTime *) playerTime;
```

## Return Value

A node time, or `nil` if the player isn’t playing.

## Discussion

For more information about this method and its inverse [`playerTime(forNodeTime:)`](./playertime%28fornodetime%29.md), see [Player timeline](../avaudioplayernode.md#Player-timeline).

## Parameters

- `playerTime`: A time relative to the player’s start time.

## See Also

### Converting node and player times
- [func playerTime(forNodeTime: AVAudioTime) -> AVAudioTime?](./playertime%28fornodetime%29.md)
  Converts from node time to player time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/nodetime(forplayertime:))*