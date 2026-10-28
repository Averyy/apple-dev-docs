# initWithTimedMetadataGroup:sessionAttributes:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Initializes the rendering frame attributes from a timed metadata group read from a Cinematic metadata track.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (instancetype) initWithTimedMetadataGroup:(AVTimedMetadataGroup *) metadataGroup sessionAttributes:(CNRenderingSessionAttributes *) sessionAttributes;
```

## Return Value

An object representing the rendering frame attributes from a timed metadata group, read from a Cinematic metadata track.

## Parameters

- `metadataGroup`: The audio and video metadata group read from the timed Cinematic metadata track of a cinematic asset.
- `sessionAttributes`: Rendering session attributes loaded from a Cinematic asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnrenderingsessionframeattributes/initwithtimedmetadatagroup:sessionattributes:)*