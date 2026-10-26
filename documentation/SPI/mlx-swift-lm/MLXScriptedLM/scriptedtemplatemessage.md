---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtemplatemessage"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ScriptedTemplateMessage

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: enum  
**Role**: Enumeration

Message helpers shared by template implementations.

## Declaration

```swift
enum ScriptedTemplateMessage
```

## Topics

### Type Methods
- [static func canonicalJSON(any Sendable) throws -> String](./scriptedtemplatemessage/canonicaljson%28_%29.md)
- [static func content(of: [String : any Sendable]) -> String](./scriptedtemplatemessage/content%28of%29.md)
  String content, or the concatenated `text` fields of a content-parts array.

## See Also

### Chat Templates
- [protocol ScriptedChatTemplate](./scriptedchattemplate.md)
  A chat template for scripted tests.
- [struct MinimalChatTemplate](./minimalchattemplate.md)
  A minimal one-marker-per-role template for mechanics tests. Not a real model family: prompts stay short and segment assertions stay readable.
- [struct ChatMLTemplate](./chatmltemplate.md)
  Plain ChatML, as used by the Qwen family without its tool extensions.
- [enum ScriptedTemplateError](./scriptedtemplateerror.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtemplatemessage)*