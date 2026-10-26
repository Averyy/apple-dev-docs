---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/atemtoolcallparser"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ATEMToolCallParser

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parser for Muse Glimmer’s Onyx ATEM tool-call format.

## Declaration

```swift
struct ATEMToolCallParser
```

#### Overview

ATEM deliberately is not XML: parameter bodies may contain unescaped, multi-line text. Parse only the protocol’s structural tags and never run a global namespace replacement over the payload—the latter silently mutates legitimate string arguments containing `<atem:`.

## Topics

### Initializers
- [init()](./atemtoolcallparser/init%28%29.md)
### Instance Properties
- [let endTag: String?](./atemtoolcallparser/endtag.md)
- [let startTag: String?](./atemtoolcallparser/starttag.md)
### Instance Methods
- [func parse(content: String, tools: [[String : any Sendable]]?) -> ToolCall?](./atemtoolcallparser/parse%28content,tools%29.md)
- [func parseEOS(String, tools: [[String : any Sendable]]?) -> [ToolCall]](./atemtoolcallparser/parseeos%28_,tools%29.md)
### Default Implementations
- [ToolCallParser Implementations](./atemtoolcallparser/toolcallparser-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [ToolCallParser](./toolcallparser.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/atemtoolcallparser)*