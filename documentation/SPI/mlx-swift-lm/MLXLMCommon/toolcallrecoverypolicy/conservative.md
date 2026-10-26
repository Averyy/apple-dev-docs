---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallrecoverypolicy/conservative"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallRecoveryPolicy.conservative

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Recover only structurally complete alternate-dialect calls that carry an explicit protocol marker (`<tool_call>`, `<|tool_call>`, `<function=`, `[TOOL_CALLS]`) and appear in committed response text — never inside reasoning spans (`<think>`/`<thinking>`/`[THINK]`), Markdown code spans or fences, or ordinary JSON data — and only when the call names an exactly declared tool. Argument normalization and schema enforcement are governed independently by [`ToolCallValidationPolicy`](../toolcallvalidationpolicy.md).

## Declaration

```swift
case conservative
```

#### Discussion

Explicit protocol attempts that are malformed, incomplete at end of stream, or undeclared are surfaced as [`RejectedToolCall`](../rejectedtoolcall.md) rather than leaked as response text. Markerless `name[ARGS]{...}` rehearsals are never promoted by this policy: without a protocol marker, prose that merely mentions a declared call is indistinguishable from an intended one.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallrecoverypolicy/conservative)*