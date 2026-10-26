# CNRenderingSessionFrameAttributes

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

Creates an object with the per frame attributes that control the appearance of a single frame of the Cinematic movie.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNRenderingSessionFrameAttributes : NSObject
```

#### Overview

The object exposes properties such as focus disparity and f-stop. It initializes these to the values that the original recorded movie used for that frame. However, you can change them before rendering to adjust focus and aperture.

## Topics

### Instance Properties
- [fNumber](./cnrenderingsessionframeattributes/fnumber.md)
  The f-stop value that inversely affects the aperture used to render the Cinematic image.
- [focusDisparity](./cnrenderingsessionframeattributes/focusdisparity.md)
  Represents the focus plane at which the rendered image should be in focus.
### Instance Methods
- [- initWithSampleBuffer:sessionAttributes:](./cnrenderingsessionframeattributes/initwithsamplebuffer_sessionattributes_.md)
  Initializes the rendering frame attributes from a sample buffer read from a Cinematic metadata track.
- [- initWithTimedMetadataGroup:sessionAttributes:](./cnrenderingsessionframeattributes/initwithtimedmetadatagroup_sessionattributes_.md)
  Initializes the rendering frame attributes from a timed metadata group read from a Cinematic metadata track.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)

## See Also

### Reading and rendering
- [CNAssetInfo](./cnassetinfo-8ja4t.md)
  An object that provides Cinematic-specific information about an asset, including its tracks.
- [CNCompositionInfo](./cncompositioninfo-vzoh.md)
  An object that enables you to add the appropriate number of tracks for a Cinematic asset.
- [CNRenderingSession](./cnrenderingsession-8yghc.md)
  An object representing the context in which rendering occurs.
- [CNRenderingSessionAttributes](./cnrenderingsessionattributes.md)
  A structure for movie-wide attributes required for proper rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsessionframeattributes)*