# disableLooping()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Disables looping for the player queue.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func disableLooping()
```

```objc
- (void) disableLooping;
```

## Discussion

The player looper will stop performing player queue operations for looping and let the current looping item replica play to the end. The player’s original [`actionAtItemEnd`](../avplayer/actionatitemend-swift.property.md) property will be restored afterwards.

## See Also

### Configuring looping
- [var loopingPlayerItems: [AVPlayerItem]](./loopingplayeritems.md)
  An array containing replicas of the template player item used to accomplish the looping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/disablelooping())*