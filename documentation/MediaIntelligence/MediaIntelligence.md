# Media Intelligence

**Framework**: Media Intelligence  
**Kind**: module

Analyze video content and group faces in images using on-device machine learning.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

#### Overview

Media Intelligence provides on-device algorithms to analyze image and video content. Use it in video editors, photo organizers, and other media apps to add intelligence features without building the underlying analysis pipeline yourself.

For images, [`FaceGroupAnalyzer`](facegroupanalyzer.md) detects faces in a collection of image assets and groups matching faces into *entities*, each representing a unique person. You can then query the analyzer to retrieve faces by asset, entity, or face ID, and use the results to build features like person-based photo organization or face search.

For video, [`VideoAnalyzer`](videoanalyzer.md) accepts one or more analysis requests for a specified asset and returns results for each. Use [`HighlightAnalysisRequest`](highlightanalysisrequest.md) to identify the most engaging segments of a video clip, or use [`KeyFrameAnalysisRequest`](keyframeanalysisrequest.md) to select a keyframe that represents the overall theme of the video. Both requests run in-process on the device, with no data leaving the system.

## Topics

### Image analysis
- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)
  Organize photos by person using on-device face detection.
- [class FaceGroupAnalyzer](facegroupanalyzer.md)
  An object that detects faces in images and groups them by person.
- [struct MediaIntelligenceImageAsset](mediaintelligenceimageasset.md)
  An image asset to analyze.
### Video analysis
- [Finding the best moments in a video](finding-the-best-moments-in-a-video.md)
  Identify keyframes and highlight segments using on-device analysis.
- [class VideoAnalyzer](videoanalyzer.md)
  An object that analyzes video assets for highlights and key frames.
- [struct MediaIntelligenceVideoAsset](mediaintelligencevideoasset.md)
  A video asset to analyze.
- [class HighlightAnalysisRequest](highlightanalysisrequest.md)
  A request that identifies the most engaging segments of a video.
- [class KeyFrameAnalysisRequest](keyframeanalysisrequest.md)
  A request that identifies the best representative frame of a video.
### Errors
- [enum MediaIntelligenceError](mediaintelligenceerror.md)
  An error that indicates a media analysis operation failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MediaIntelligence)*