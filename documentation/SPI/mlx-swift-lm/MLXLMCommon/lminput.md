---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/lminput"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LMInput

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Representation of [`LanguageModel`](./languagemodel.md) input.

## Declaration

```swift
struct LMInput
```

#### Overview

This can contain text (tokens), prepared images (`MLXArray`), or other media as needed. [`LMInput`](./lminput.md) is produced by [`UserInputProcessor`](./userinputprocessor.md) in response to [`UserInput`](./userinput.md).

The [`ModelContext`](./modelcontext.md) holds the [`UserInputProcessor`](./userinputprocessor.md) associated with a [`LanguageModel`](./languagemodel.md).

## Topics

### Structures
- [LMInput.ProcessedAudio](./lminput/processedaudio.md)
  Representation of prepared audio features.
- [LMInput.ProcessedImage](./lminput/processedimage.md)
  Representation of prepared input image(s).
- [LMInput.ProcessedVideo](./lminput/processedvideo.md)
  Representation of prepared input video(s). For now, this is virtually identical to ProcessedImage.
- [LMInput.Text](./lminput/text-swift.struct.md)
  Representation of tokenized input text.
### Initializers
- [init(text: LMInput.Text, image: LMInput.ProcessedImage?, video: LMInput.ProcessedVideo?, audio: LMInput.ProcessedAudio?)](./lminput/init%28text,image,video,audio%29.md)
- [init(tokens: MLXArray, mask: MLXArray?)](./lminput/init%28tokens,mask%29.md)
### Instance Properties
- [let audio: ProcessedAudio?](./lminput/audio.md)
- [let image: ProcessedImage?](./lminput/image.md)
- [let text: Text](./lminput/text-swift.property.md)
- [let video: ProcessedVideo?](./lminput/video.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/lminput)*