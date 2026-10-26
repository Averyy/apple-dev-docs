---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/chatmltemplate"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ChatMLTemplate

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

Plain ChatML, as used by the Qwen family without its tool extensions.

## Declaration

```swift
struct ChatMLTemplate
```

#### Overview

```
<|im_start|>system\n...<|im_end|>\n
<|im_start|>user\n...<|im_end|>\n
<|im_start|>assistant\n...<|im_end|>\n
<|im_start|>assistant\n            generation prompt
```

Role names are ordinary text, so any role renders. `<|im_end|>` is the default EOS: a turn’s prompt plus its generated tokens (including EOS) is a prefix of the next turn’s rendering, since the `\n` after `<|im_end|>` comes after that prefix.

Plain ChatML has no tool convention, so tools and tool calls throw [`ScriptedTemplateError.unsupported(_:)`](./scriptedtemplateerror/unsupported%28_%29.md).

## Topics

### Initializers
- [init()](./chatmltemplate/init%28%29.md)
### Instance Properties
- [var corpus: [String]](./chatmltemplate/corpus.md)
- [var endOfTurnToken: String?](./chatmltemplate/endofturntoken.md)
- [var specialTokens: [String]](./chatmltemplate/specialtokens.md)
### Instance Methods
- [func render(messages: [[String : any Sendable]], tools: [[String : any Sendable]]?, additionalContext: [String : any Sendable]?) throws -> [String]](./chatmltemplate/render%28messages,tools,additionalcontext%29.md)
### Type Properties
- [static let imEnd: String](./chatmltemplate/imend.md)
- [static let imStart: String](./chatmltemplate/imstart.md)
### Default Implementations
- [ScriptedChatTemplate Implementations](./chatmltemplate/scriptedchattemplate-implementations.md)

## Relationships

### Conforms To
- [ScriptedChatTemplate](./scriptedchattemplate.md)
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Chat Templates
- [protocol ScriptedChatTemplate](./scriptedchattemplate.md)
  A chat template for scripted tests.
- [struct MinimalChatTemplate](./minimalchattemplate.md)
  A minimal one-marker-per-role template for mechanics tests. Not a real model family: prompts stay short and segment assertions stay readable.
- [enum ScriptedTemplateMessage](./scriptedtemplatemessage.md)
  Message helpers shared by template implementations.
- [enum ScriptedTemplateError](./scriptedtemplateerror.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/chatmltemplate)*