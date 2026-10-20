# endSeeking()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Ends forward and backward seeking through the media content.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func endSeeking()
```

```objc
- (void) endSeeking;
```

#### Discussion

You must call this method to end a seeking operation begun by calling either the [`beginSeekingBackward()`](./beginseekingbackward%28%29.md) or [`beginSeekingForward()`](./beginseekingforward%28%29.md) method. After calling this method, the player returns to the same state it was in prior to seeking. In other words, if the item was playing before seeking began, it continues playing from the new playhead position after calling this method.

This method has no effect on streamed content.

## See Also

### Seeking within media
- [func beginSeekingBackward()](./beginseekingbackward%28%29.md)
  Begins seeking backward through the media content.
- [func beginSeekingForward()](./beginseekingforward%28%29.md)
  Begins seeking forward through the media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/endseeking())*