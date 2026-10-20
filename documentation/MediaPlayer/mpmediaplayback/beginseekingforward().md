# beginSeekingForward()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Begins seeking forward through the media content.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func beginSeekingForward()
```

```objc
- (void) beginSeekingForward;
```

#### Discussion

Use this method to move the current playback position forward in time at an accelerated rate. Seeking begins when you call this method and continues until you call the [`endSeeking()`](./endseeking%28%29.md) method.

This method has no effect on streamed content.

## See Also

### Seeking within media
- [func beginSeekingBackward()](./beginseekingbackward%28%29.md)
  Begins seeking backward through the media content.
- [func endSeeking()](./endseeking%28%29.md)
  Ends forward and backward seeking through the media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/beginseekingforward())*