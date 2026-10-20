# end()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Ends a suspension.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func end()
```

```objc
- (void) end;
```

#### Discussion

If this is the last suspension, the coordinator adjusts the timing of its playback object to match the group.

To end a suspension and simultaneously propose a new playback time to the group, call the [`end(proposingNewTime:)`](./end%28proposingnewtime%29.md) method.

## See Also

### Ending a suspension
- [func end(proposingNewTime: CMTime)](./end%28proposingnewtime%29.md)
  Ends a suspension and proposes a new playback time to the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcoordinatedplaybacksuspension/end())*