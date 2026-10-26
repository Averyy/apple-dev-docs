---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtemplateerror"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ScriptedTemplateError

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: enum  
**Role**: Enumeration

## Declaration

```swift
enum ScriptedTemplateError
```

## Topics

### Enumeration Cases
- [ScriptedTemplateError.invalidJSON(_:)](./scriptedtemplateerror/invalidjson%28_%29.md)
- [ScriptedTemplateError.unknownRole(_:)](./scriptedtemplateerror/unknownrole%28_%29.md)
- [ScriptedTemplateError.unsupported(_:)](./scriptedtemplateerror/unsupported%28_%29.md)
  The template has no rendering for this input, such as tools in plain ChatML.
### Default Implementations
- [Equatable Implementations](./scriptedtemplateerror/equatable-implementations.md)
- [Error Implementations](./scriptedtemplateerror/error-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Error
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Chat Templates
- [protocol ScriptedChatTemplate](./scriptedchattemplate.md)
  A chat template for scripted tests.
- [struct MinimalChatTemplate](./minimalchattemplate.md)
  A minimal one-marker-per-role template for mechanics tests. Not a real model family: prompts stay short and segment assertions stay readable.
- [struct ChatMLTemplate](./chatmltemplate.md)
  Plain ChatML, as used by the Qwen family without its tool extensions.
- [enum ScriptedTemplateMessage](./scriptedtemplatemessage.md)
  Message helpers shared by template implementations.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtemplateerror)*