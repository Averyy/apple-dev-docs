---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallProcessor

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Processes generated text to detect and extract tool calls during streaming generation.

## Declaration

```swift
class ToolCallProcessor
```

#### Overview

`ToolCallProcessor` handles the streaming detection of tool calls in model output, buffering partial content and extracting complete tool calls when detected.

Example:

```swift
let processor = ToolCallProcessor(format: .lfm2)
for chunk in generatedChunks {
    if let text = processor.processChunk(chunk) {
        // Regular text to display
        print(text)
    }
}
// After generation completes:
for toolCall in processor.toolCalls {
    // Handle extracted tool calls
    print(toolCall.function.name)
}
```

## Topics

### Initializers
- [init(format: ToolCallFormat, tools: [[String : any Sendable]]?, toolCallPolicy: ToolCallPolicy)](./toolcallprocessor/init%28format,tools,toolcallpolicy%29.md)
  Initialize with a specific tool call format.
### Instance Properties
- [var recoveredToolCallCount: Int](./toolcallprocessor/recoveredtoolcallcount.md)
  Total calls promoted by cross-dialect recovery, including events that have already been drained by a diagnostic consumer.
- [var recoveryEvents: [ToolCallRecoveryEvent]](./toolcallprocessor/recoveryevents.md)
  Provenance for every call produced by cross-dialect recovery, in source order. Calls produced by the selected native parser are not included.
- [var rejectedToolCallCount: Int](./toolcallprocessor/rejectedtoolcallcount.md)
  Total rejected calls observed by this processor, including drained calls.
- [var rejectedToolCalls: [RejectedToolCall]](./toolcallprocessor/rejectedtoolcalls.md)
  Tool-call-shaped outputs that were parsed incompletely, were malformed, or failed authorization.
- [var toolCalls: [ToolCall]](./toolcallprocessor/toolcalls.md)
  The tool calls extracted during processing.
### Instance Methods
- [func drainRecoveryEvents() -> [ToolCallRecoveryEvent]](./toolcallprocessor/drainrecoveryevents%28%29.md)
  Removes and returns every cross-dialect recovery event in source order. A second call returns an empty array until more calls are recovered.
- [func drainRejectedToolCalls() -> [RejectedToolCall]](./toolcallprocessor/drainrejectedtoolcalls%28%29.md)
  Removes and returns every rejected call in source order. A second call returns an empty array until more rejections are observed.
- [func drainToolCalls() -> [ToolCall]](./toolcallprocessor/draintoolcalls%28%29.md)
  Removes and returns every parsed call in parse order. A second call returns an empty array until more chunks are processed.
- [func processChunk(String) -> String?](./toolcallprocessor/processchunk%28_%29.md)
  Process a generated text chunk and extract any tool call content.
- [func processChunkOutputs(String) -> [Output]](./toolcallprocessor/processchunkoutputs%28_%29.md)
  Processes a generated chunk and removes its output in source order.
- [func processEOS()](./toolcallprocessor/processeos%28%29.md)
  Process end-of-sequence, parsing any buffered content as tool call(s).
- [func processEOS(returnBufferedText: Bool) -> String?](./toolcallprocessor/processeos%28returnbufferedtext%29.md)
  Process end-of-sequence and optionally return residual buffered text.
- [func processEOSOutputs() -> [Output]](./toolcallprocessor/processeosoutputs%28%29.md)
  Finishes processing and removes residual output in source order.
### Enumerations
- [ToolCallProcessor.Output](./toolcallprocessor/output.md)
  An ordered item emitted while processing generated output.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallprocessor)*