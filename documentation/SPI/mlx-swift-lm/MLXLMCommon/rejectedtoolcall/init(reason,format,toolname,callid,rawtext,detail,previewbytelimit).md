---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rejectedtoolcall/init(reason:format:toolname:callid:rawtext:detail:previewbytelimit:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(reason:format:toolName:callID:rawText:detail:previewByteLimit:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

Creates a rejection while retaining a bounded diagnostic preview.

## Declaration

```swift
init(reason: Reason, format: ToolCallFormat, toolName: String? = nil, callID: String? = nil, rawText: String, detail: String? = nil, previewByteLimit: Int = RejectedToolCall.defaultPreviewByteLimit)
```

## Parameters

- `reason`: The semantic reason the output was rejected.
- `format`: The tool-call protocol used to interpret the output.
- `toolName`: The recovered function name, if available.
- `callID`: The recovered call identifier, if available.
- `rawText`: The complete rejected model output. Only a bounded preview is retained by this value.
- `detail`: A diagnostic summary that must not contain raw model output or sensitive argument values.
- `previewByteLimit`: Maximum approximate UTF-8 size of the retained preview. The preview preserves both ends and never splits a Swift `Character`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rejectedtoolcall/init(reason:format:toolname:callid:rawtext:detail:previewbytelimit:))*