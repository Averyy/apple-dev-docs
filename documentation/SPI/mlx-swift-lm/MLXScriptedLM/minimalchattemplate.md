---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/minimalchattemplate"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# MinimalChatTemplate

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

A minimal one-marker-per-role template for mechanics tests. Not a real model family: prompts stay short and segment assertions stay readable.

## Declaration

```swift
struct MinimalChatTemplate
```

## Overview

```
<|tools|>[...]<|end|>          only when tools are present
<|system|>...<|end|>
<|user|>...<|end|>
<|assistant|>...<|tool_call|>{...}<|end|>
<|tool|>...<|end|>
<|assistant|>                  generation prompt
```

An assistant turn ends with `<|end|>`, which is also the default EOS. So the prompt for one turn plus the generated tokens (including EOS) is a prefix of the next turn’s rendering.

Tool calls render as canonical JSON (sorted keys).

## Topics

### Structures
- [MinimalChatTemplate.Markers](./minimalchattemplate/markers-swift.struct.md)
### Initializers
- [init(markers: Markers, nonAtomicMarkers: Set<String>)](./minimalchattemplate/init%28markers,nonatomicmarkers%29.md)
### Instance Properties
- [var endOfTurnToken: String?](./minimalchattemplate/endofturntoken.md)
- [var markers: Markers](./minimalchattemplate/markers-swift.property.md)
- [var nonAtomicMarkers: Set<String>](./minimalchattemplate/nonatomicmarkers.md)
  Markers registered as multi-token text instead of atomic specials.
- [var specialTokens: [String]](./minimalchattemplate/specialtokens.md)
- [var textMarkers: [String]](./minimalchattemplate/textmarkers.md)
### Instance Methods
- [func render(messages: [[String : any Sendable]], tools: [[String : any Sendable]]?, additionalContext: [String : any Sendable]?) throws -> [String]](./minimalchattemplate/render%28messages,tools,additionalcontext%29.md)
### Default Implementations
- [ScriptedChatTemplate Implementations](./minimalchattemplate/scriptedchattemplate-implementations.md)

## Relationships

### Conforms To
- [ScriptedChatTemplate](./scriptedchattemplate.md)
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Chat Templates
- [protocol ScriptedChatTemplate](./scriptedchattemplate.md)
  A chat template for scripted tests.
- [struct ChatMLTemplate](./chatmltemplate.md)
  Plain ChatML, as used by the Qwen family without its tool extensions.
- [enum ScriptedTemplateMessage](./scriptedtemplatemessage.md)
  Message helpers shared by template implementations.
- [enum ScriptedTemplateError](./scriptedtemplateerror.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/minimalchattemplate)*