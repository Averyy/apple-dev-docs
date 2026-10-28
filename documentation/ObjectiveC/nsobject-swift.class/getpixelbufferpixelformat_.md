# getPixelBufferPixelFormat:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.5+ - Deprecated in 10.9

## Declaration

```objc
- (void) getPixelBufferPixelFormat:(OSType *) pixelFormatOut;
```

## Discussion

This method is optional. Called once after setVideoDataSource:, if implemented.

## Parameters

- `pixelFormatOut`: The pixel format to be used for the CVPixelBufferRef instances passed to renderIntoPixelBuffer:forTime:.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/getpixelbufferpixelformat:)*