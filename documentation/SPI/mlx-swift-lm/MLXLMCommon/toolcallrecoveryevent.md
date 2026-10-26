---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallrecoveryevent"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ToolCallRecoveryEvent

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Provenance for a tool call produced by cross-dialect recovery.

## Declaration

```swift
struct ToolCallRecoveryEvent
```

#### Overview

Recovery events feed diagnostics and telemetry without changing the ordinary [`ToolCall`](./toolcall.md) execution interface.

## Topics

### Initializers
- [init(toolName: String, callID: String?, selectedFormat: ToolCallFormat, dialect: Dialect, repair: Repair, wasIncompleteAtEOS: Bool)](./toolcallrecoveryevent/init%28toolname,callid,selectedformat,dialect,repair,wasincompleteateos%29.md)
### Instance Properties
- [let callID: String?](./toolcallrecoveryevent/callid.md)
  The recovered call identifier, when the dialect carried one.
- [let dialect: Dialect](./toolcallrecoveryevent/dialect-swift.property.md)
  The dialect the call was actually emitted in.
- [let repair: Repair](./toolcallrecoveryevent/repair-swift.property.md)
  The repair that was applied.
- [let selectedFormat: ToolCallFormat](./toolcallrecoveryevent/selectedformat.md)
  The format selected for this generation (the authoritative parser).
- [let toolName: String](./toolcallrecoveryevent/toolname.md)
  The recovered function name.
- [let wasIncompleteAtEOS: Bool](./toolcallrecoveryevent/wasincompleteateos.md)
  Whether the call was committed at end of stream rather than from a complete in-stream frame.
### Enumerations
- [ToolCallRecoveryEvent.Dialect](./toolcallrecoveryevent/dialect-swift.enum.md)
  The textual dialect the model actually emitted.
- [ToolCallRecoveryEvent.Repair](./toolcallrecoveryevent/repair-swift.enum.md)
  The repair applied to make the call executable.
### Default Implementations
- [Equatable Implementations](./toolcallrecoveryevent/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/toolcallrecoveryevent)*