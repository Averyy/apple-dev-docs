# beginSeekingForward()

**Framework**: Media Player  
**Kind**: method  
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

#### Discussion

Use this method to move the current playback position forward in time at an accelerated rate. Seeking begins when you call this method and continues until you call the [`endSeeking()`](mpmediaplayback/endseeking().md) method.

This method has no effect on streamed content.

## See Also

- [func beginSeekingBackward()](mpmediaplayback/beginseekingbackward.md)
  Begins seeking backward through the media content.
- [func endSeeking()](mpmediaplayback/endseeking.md)
  Ends forward and backward seeking through the media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/beginseekingforward())*