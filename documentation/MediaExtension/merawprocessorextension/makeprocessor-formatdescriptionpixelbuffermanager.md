# makeProcessor(formatDescription:pixelBufferManager:)

**Framework**: MediaExtension  
**Kind**: method  
**Required**: Yes

A factory method to create a video RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func makeProcessor(formatDescription: CMVideoFormatDescription, pixelBufferManager extensionPixelBufferManager: MERAWProcessorPixelBufferManager) throws -> any MERAWProcessor
```

#### Discussion

Creates a new `MERAWProcessor` matching the given `CMVideoFormatDescriptionRef`.  If these parameters are not compatible with the `MERAWProcessor`, the call should fail, returning `MEErrorUnsupportedFeature`.

## Parameters

- `formatDescription`: A   describing the video data that was decoded to produce the RAW input for the video RAW processor.
- `extensionPixelBufferManager`: An   instance that should be retained by the new   instance and used for output pixelBuffer configuration and allocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessorextension/makeprocessor(formatdescription:pixelbuffermanager:))*