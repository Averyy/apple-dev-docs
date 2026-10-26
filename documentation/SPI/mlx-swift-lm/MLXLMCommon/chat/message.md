---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chat/message"
framework: "mlx-swift-lm/MLXLMCommon"
---

# Chat.Message

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

## Declaration

```swift
struct Message
```

## Topics

### Structures
- [Chat.Message.Tool](./message/tool-swift.struct.md)
### Initializers
- [init(role: Role, content: String, images: [UserInput.Image], videos: [UserInput.Video], audios: [UserInput.Audio], tool: Tool?)](./message/init%28role,content,images,videos,audios,tool%29.md)
### Instance Properties
- [var audios: [UserInput.Audio]](./message/audios.md)
  Array of audio data associated with the message.
- [var content: String](./message/content.md)
  The content of the message.
- [var images: [UserInput.Image]](./message/images.md)
  Array of image data associated with the message.
- [var role: Role](./message/role-swift.property.md)
  The role of the message sender.
- [var tool: Tool?](./message/tool-swift.property.md)
  Tool-call metadata associated with this message.
- [var videos: [UserInput.Video]](./message/videos.md)
  Array of video data associated with the message.
### Type Methods
- [static func assistant(String, images: [UserInput.Image], videos: [UserInput.Video], toolCalls: [ToolCall]?) -> Chat.Message](./message/assistant%28_,images,videos,toolcalls%29.md)
- [static func system(String, images: [UserInput.Image], videos: [UserInput.Video]) -> Chat.Message](./message/system%28_,images,videos%29.md)
- [static func tool(String, id: String?, name: String?) -> Chat.Message](./message/tool%28_,id,name%29.md)
- [static func user(String, images: [UserInput.Image], videos: [UserInput.Video], audios: [UserInput.Audio]) -> Chat.Message](./message/user%28_,images,videos,audios%29.md)
### Enumerations
- [Chat.Message.Role](./message/role-swift.enum.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chat/message)*