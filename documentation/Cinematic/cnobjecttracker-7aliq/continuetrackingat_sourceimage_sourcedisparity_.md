# continueTrackingAt:sourceImage:sourceDisparity:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Continues to track an object that you’ve started tracking, and adds a new detection to the detection track you’re building.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (CNBoundsPrediction *) continueTrackingAt:(CMTime) time sourceImage:(CVPixelBufferRef) sourceImage sourceDisparity:(CVPixelBufferRef) sourceDisparity;
```

## Return Value

An object representing a prediction of where the object is in the source image.

## Parameters

- `time`: The presentation time of the first frame in the detection track.
- `sourceImage`: The image buffer containing the image.
- `sourceDisparity`: The disparity buffer containing depth information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnobjecttracker-7aliq/continuetrackingat:sourceimage:sourcedisparity:)*