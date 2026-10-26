# audioVolume

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The audio gain to apply to the processed Live Photo.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var audioVolume: Float { get set }
```

```objc
@property float audioVolume;
```

#### Discussion

Values must be between `0.0` and `1.0`, inclusive. A value of `1.0` (the default) leaves the audio content of the Live Photo unchanged. A value of `0.0` mutes all audio in the output Live Photo.

Setting this property does not process the Live Photo content; instead, it sets the audio gain to be applied when you later process the Live Photo using one of the methods listed in Processing an Editing Context’s Live Photo.

## See Also

### Preparing an Editing Context for Processing
- [var frameProcessor: PHLivePhotoFrameProcessingBlock?](./frameprocessor.md)
  A block to be called by Photos for processing each frame of the Live Photo’s visual content.
- [typealias PHLivePhotoFrameProcessingBlock](../phlivephotoframeprocessingblock.md)
  The signature for a block Photos calls to process Live Photo frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotoeditingcontext/audiovolume)*