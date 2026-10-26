# initWithSampleBuffer:sessionAttributes:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Initializes the rendering frame attributes from a sample buffer read from a Cinematic metadata track.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (instancetype) initWithSampleBuffer:(CMSampleBufferRef) sampleBuffer sessionAttributes:(CNRenderingSessionAttributes *) sessionAttributes;
```

#### Return Value

An object representing the rendering frame attributes from a sample buffer read from a cinematic metadata track.

## Parameters

- `sampleBuffer`: A sample buffer read from the timed Cinematic metadata track of a cinematic asset.
- `sessionAttributes`: Rendering session attributes loaded from a Cinematic asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsessionframeattributes/initwithsamplebuffer:sessionattributes:)*