---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput"
framework: "mlx-swift-lm/MLXLMCommon"
---

# UserInput

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Container for raw user input.

## Declaration

```swift
struct UserInput
```

#### Overview

A [`UserInputProcessor`](./userinputprocessor.md) can convert this to [`LMInput`](./lminput.md). See also [`ModelContext`](./modelcontext.md).

## Topics

### Structures
- [UserInput.Audio](./userinput/audio.md)
  Representation of an audio resource.
- [UserInput.AudioProcessing](./userinput/audioprocessing.md)
  Representation of audio processing
- [UserInput.Image](./userinput/image.md)
  Representation of an image resource.
- [UserInput.Processing](./userinput/processing-swift.struct.md)
  Representation of processing to apply to media.
- [UserInput.Video](./userinput/video.md)
  Representation of a video resource.
- [UserInput.VideoFrame](./userinput/videoframe.md)
- [UserInput.VideoProcessing](./userinput/videoprocessing.md)
  Representation of video processing options.
### Initializers
- [init(chat: [Chat.Message], processing: Processing, tools: [ToolSpec]?, additionalContext: [String : any Sendable]?)](./userinput/init%28chat,processing,tools,additionalcontext%29.md)
  Initialize the `UserInput` with a model agnostic structured context.
- [init(messages: [Message], images: [Image], videos: [Video], audios: [Audio], tools: [ToolSpec]?, additionalContext: [String : any Sendable]?)](./userinput/init%28messages,images,videos,audios,tools,additionalcontext%29.md)
  Initialize the `UserInput` with model specific mesage structures.
- [init(prompt: Prompt, images: [Image], videos: [Video], audios: [Audio], processing: Processing, tools: [ToolSpec]?, additionalContext: [String : any Sendable]?)](./userinput/init%28prompt,images,videos,audios,processing,tools,additionalcontext%29.md)
  Initialize the `UserInput` with a preconfigured [`UserInput.Prompt`](./userinput/prompt-swift.enum.md).
- [init(prompt: String, images: [Image], videos: [Video], audios: [Audio], tools: [ToolSpec]?, additionalContext: [String : any Sendable]?)](./userinput/init%28prompt,images,videos,audios,tools,additionalcontext%29.md)
  Initialize the `UserInput` with a single text prompt.
### Instance Properties
- [var additionalContext: [String : any Sendable]?](./userinput/additionalcontext.md)
  Additional values provided for the chat template rendering context
- [var audios: [UserInput.Audio]](./userinput/audios.md)
  The audios associated with the `UserInput`.
- [var images: [UserInput.Image]](./userinput/images.md)
  The images associated with the `UserInput`.
- [var processing: Processing](./userinput/processing-swift.property.md)
- [var prompt: Prompt](./userinput/prompt-swift.property.md)
  The prompt to evaluate.
- [var tools: [ToolSpec]?](./userinput/tools.md)
- [var videos: [UserInput.Video]](./userinput/videos.md)
  The images associated with the `UserInput`.
### Enumerations
- [UserInput.AudioFormat](./userinput/audioformat.md)
  Representation of the audio format.
- [UserInput.Prompt](./userinput/prompt-swift.enum.md)
  Representation of a prompt or series of messages (conversation).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput)*