# outputBufferDescription

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The output buffers of the video composition can be specified with the outputBufferDescription. The value is an array of CMTagCollectionRef objects that describes the output buffers.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) NSArray * outputBufferDescription;
```

## Discussion

If the video composition will output tagged buffers, the details of those buffers should be specified with CMTags. Specifically, the StereoView (eyes) and ProjectionKind must be specified. The behavior is undefined if the output tagged buffers do not match the outputBufferDescription. The default is nil, which means monoscopic output. Note that an empty array is not valid. An exception will be thrown if the objects in the array are not of type CMTagCollectionRef. Note that tagged buffers are only supported for custom compositors.

## See Also

### Configuring video composition properties
- [var frameDuration: CMTime](./frameduration.md)
  A time interval for which the video composition should render composed video frames.
- [var renderSize: CGSize](./rendersize.md)
  The size at which the video composition should render.
- [var renderScale: Float](./renderscale.md)
  The scale at which the video composition should render.
- [var animationTool: AVVideoCompositionCoreAnimationTool?](./animationtool.md)
  A video composition tool to use with Core Animation in offline rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/outputbufferdescription)*