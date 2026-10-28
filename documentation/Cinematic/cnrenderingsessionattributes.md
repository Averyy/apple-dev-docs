# CNRenderingSessionAttributes

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

A structure for movie-wide attributes required for proper rendering.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNRenderingSessionAttributes : NSObject
```

## Overview

The attributes include camera intrinsics from the camera on which the video was originally recorded.

## Topics

### Instance Properties
- [renderingVersion](./cnrenderingsessionattributes/renderingversion.md)
  The primary version number used to render the original Cinematic move that determines compatibility.
### Type Methods
- [+ loadFromAsset:completionHandler:](./cnrenderingsessionattributes/loadfromasset_completionhandler_.md)
  Loads the rendering session attributes from an asset asynchronously.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Reading and rendering
- [CNAssetInfo](./cnassetinfo-8ja4t.md)
  An object that provides Cinematic-specific information about an asset, including its tracks.
- [CNCompositionInfo](./cncompositioninfo-vzoh.md)
  An object that enables you to add the appropriate number of tracks for a Cinematic asset.
- [CNRenderingSession](./cnrenderingsession-8yghc.md)
  An object representing the context in which rendering occurs.
- [CNRenderingSessionFrameAttributes](./cnrenderingsessionframeattributes.md)
  Creates an object with the per frame attributes that control the appearance of a single frame of the Cinematic movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsessionattributes)*