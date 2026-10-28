# playerTime(forNodeTime:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (AVAudioTime *) playerTimeForNodeTime:(AVAudioTime *) nodeTime;
```

## Return Value

A time relative to the player’s start time, or `nil` if the player isn’t playing.

## Discussion

For more information about this method and its inverse [`nodeTime(forPlayerTime:)`](./nodetime%28forplayertime%29.md), see [Player timeline](../avaudioplayernode.md#Player-timeline).

## Parameters

- `nodeTime`: The node time.

## See Also

### Converting node and player times
- [func nodeTime(forPlayerTime: AVAudioTime) -> AVAudioTime?](./nodetime%28forplayertime%29.md)
  Converts from player time to node time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioplayernode/playertime(fornodetime:))*