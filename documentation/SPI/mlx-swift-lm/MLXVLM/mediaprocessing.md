---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing"
framework: "mlx-swift-lm/MLXVLM"
---

# MediaProcessing

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: enum  
**Role**: Enumeration

Collection of methods for processing media (images, video, etc.).

## Declaration

```swift
enum MediaProcessing
```

## Overview

A typical image preparation pipeline might look like this:

```swift
var image: CIImage
image = MediaProcessing.inSRGBToneCurveSpace(image)

// Apply user instructions
image = MediaProcessing.apply(image, processing: processing)

image = MediaProcessing.resampleBicubic(image, to: config.size.cgSize)
image = MediaProcessing.normalize(
    image, mean: config.imageMeanTuple, std: config.imageStdTuple)

return MediaProcessing.asMLXArray(image)
```

This is the responsibility of the `UserInputProcessor`.

## Topics

### Type Methods
- [static func apply(CIImage, processing: UserInput.Processing?) -> CIImage](./mediaprocessing/apply%28_,processing%29.md)
  Apply `UserInput.Processing`, if needed, to the image.
- [static func asCIImageSequence(AVAsset, samplesPerSecond: Int) async throws -> [CIImage]](./mediaprocessing/asciimagesequence%28_,samplespersecond%29.md)
- [static func asMLXArray(CIImage, colorSpace: CGColorSpace?) -> MLXArray](./mediaprocessing/asmlxarray%28_,colorspace%29.md)
  Convert the CIImage into a planar 3 channel MLXArray `[1, C, H, W]`
- [static func asProcessedSequence(AVAsset, maxFrames: Int, targetFPS: (CMTime) -> Double, frameProcessing: (VideoFrame) throws -> VideoFrame) async throws -> ProcessedFrames](./mediaprocessing/asprocessedsequence%28_,maxframes,targetfps,frameprocessing%29.md)
- [static func asProcessedSequence(UserInput.Video, processing: UserInput.VideoProcessing, targetFPS: ((CMTime) -> Double)?, maxFrames: Int, frameProcessing: (VideoFrame) throws -> VideoFrame) async throws -> ProcessedFrames](./mediaprocessing/asprocessedsequence%28_,processing,targetfps,maxframes,frameprocessing%29.md)
  Extract and process a sequence of video frames according to video processing configuration.
- [static func asProcessedSequence(UserInput.Video, samplesPerSecond: Int, frameProcessing: (VideoFrame) throws -> VideoFrame) async throws -> ProcessedFrames](./mediaprocessing/asprocessedsequence%28_,samplespersecond,frameprocessing%29-6y2hy.md)
  Extract and process a sequence of video frames at a constant sample rate.
- [static func asProcessedSequence(AVAsset, samplesPerSecond: Int, frameProcessing: (VideoFrame) throws -> VideoFrame) async throws -> ProcessedFrames](./mediaprocessing/asprocessedsequence%28_,samplespersecond,frameprocessing%29-7cfbh.md)
- [static func asProcessedSequence(UserInput.Video, targetFPS: (CMTime) -> Double, maxFrames: Int, frameProcessing: (VideoFrame) throws -> VideoFrame) async throws -> ProcessedFrames](./mediaprocessing/asprocessedsequence%28_,targetfps,maxframes,frameprocessing%29.md)
  Extract and process a sequence of video frames using a dynamic target FPS function.
- [static func asProcessedSequence(UserInput.Video, userProcessing: UserInput.Processing, targetFPS: ((CMTime) -> Double)?, maxFrames: Int, frameProcessing: (VideoFrame) throws -> VideoFrame) async throws -> ProcessedFrames](./mediaprocessing/asprocessedsequence%28_,userprocessing,targetfps,maxframes,frameprocessing%29.md)
  Extract and process a sequence of video frames according to `UserInput.Processing` options.
- [static func aspectRatioForResample(CIImage, size: CGSize) -> Float](./mediaprocessing/aspectratioforresample%28_,size%29.md)
- [static func bestFit(CGSize, in: CGSize) -> CGSize](./mediaprocessing/bestfit%28_,in%29.md)
  Compute the best fit size of one size in another (respecting aspect ratio).
- [static func bestFitScale(CGSize, in: CGSize) -> CGFloat](./mediaprocessing/bestfitscale%28_,in%29.md)
  Compute the best fit scale of one size in another (respecting aspect ratio).
- [static func centerCrop(CGRect, size: CGSize) -> CGRect](./mediaprocessing/centercrop%28_,size%29-3m1zd.md)
  Given an `extent` and a target `size` produce the `CGRect` that will be a center crop.
- [static func centerCrop(CIImage, size: CGSize) -> CIImage](./mediaprocessing/centercrop%28_,size%29-98ori.md)
  Given an `image` and a target `size` produce the `CIImage` that will be a center crop.
- [static func fitIn(CGSize, longestEdge: Int) -> CGSize](./mediaprocessing/fitin%28_,longestedge%29.md)
  Given a `size` and a target `longestEdge` compute a new size that respects the aspect ratio of the original `size` and is constrained by the `longestEdge`.
- [static func fitIn(CGSize, shortestEdge: Int) -> CGSize](./mediaprocessing/fitin%28_,shortestedge%29.md)
  Given a `size` and a target `shortestEdge` compute a new size that respects the aspect ratio of the original `size` and is constrained by the `shortestEdge`.
- [static func inLinearToneCurveSpace(CIImage) -> CIImage](./mediaprocessing/inlineartonecurvespace%28_%29.md)
  Inverse of [`inSRGBToneCurveSpace(_:)`](./mediaprocessing/insrgbtonecurvespace%28_%29.md) (for completeness).
- [static func inSRGBToneCurveSpace(CIImage) -> CIImage](./mediaprocessing/insrgbtonecurvespace%28_%29.md)
  VLM media processing is normally done without regard to the colorspace. Many, though not all, images are stored in sRGB and this will be the implicit colorspace used. This converts to a colorspace with an sRGB tone curve, though not necessarily sRGB primaries, etc.
- [static func normalize(CIImage, mean: (CGFloat, CGFloat, CGFloat), std: (CGFloat, CGFloat, CGFloat)) -> CIImage](./mediaprocessing/normalize%28_,mean,std%29.md)
  Normalize the image using the given mean and standard deviation parameters.
- [static func padToSquare(CIImage, backgroundColor: CIColor) -> CIImage](./mediaprocessing/padtosquare%28_,backgroundcolor%29.md)
  Enlarge an image by padding to square size. The original image is centered inside the square.
- [static func rectSmallerOrEqual(CGRect, size: CGSize) -> Bool](./mediaprocessing/rectsmallerorequal%28_,size%29.md)
  Return `true` if the size is smaller or equal to the size of the `extent`.
- [static func resampleBicubic(CIImage, to: CGSize) -> CIImage](./mediaprocessing/resamplebicubic%28_,to%29.md)
  Resample the image using bicubic interpolation.
- [static func resampleLanczos(CIImage, to: CGSize) -> CIImage](./mediaprocessing/resamplelanczos%28_,to%29.md)
  Resample the image using Lanczos interpolation.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/mediaprocessing)*