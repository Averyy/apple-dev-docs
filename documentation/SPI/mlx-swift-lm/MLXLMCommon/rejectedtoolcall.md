---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rejectedtoolcall"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RejectedToolCall

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A tool-call-shaped model output that was deliberately not made executable.

## Declaration

```swift
struct RejectedToolCall
```

#### Overview

Rejections are emitted separately from [`ToolCall`](./toolcall.md) so code handling a `ToolCall` can rely on it having passed parsing and authorization. The raw model output is retained only as a bounded diagnostic preview and is never included in the error description.

## Topics

### Initializers
- [init(from: any Decoder) throws](./rejectedtoolcall/init%28from%29.md)
- [init(reason: Reason, format: ToolCallFormat, toolName: String?, callID: String?, rawText: String, detail: String?, previewByteLimit: Int)](./rejectedtoolcall/init%28reason,format,toolname,callid,rawtext,detail,previewbytelimit%29.md)
  Creates a rejection while retaining a bounded diagnostic preview.
### Instance Properties
- [let callID: String?](./rejectedtoolcall/callid.md)
  The parsed call identifier, when one could be recovered safely.
- [let detail: String?](./rejectedtoolcall/detail.md)
  A safe diagnostic summary that does not contain raw model output.
- [let format: ToolCallFormat](./rejectedtoolcall/format.md)
  The protocol used to interpret the model output.
- [let isPreviewTruncated: Bool](./rejectedtoolcall/ispreviewtruncated.md)
  Whether [`rawTextPreview`](./rejectedtoolcall/rawtextpreview.md) omits bytes from the middle of the output.
- [let rawTextByteCount: Int](./rejectedtoolcall/rawtextbytecount.md)
  The number of UTF-8 bytes in the complete rejected model output.
- [let rawTextPreview: String](./rejectedtoolcall/rawtextpreview.md)
  A bounded prefix-and-suffix preview of the rejected model output.
- [let reason: Reason](./rejectedtoolcall/reason-swift.property.md)
  The semantic reason the output was rejected.
- [let toolName: String?](./rejectedtoolcall/toolname.md)
  The parsed function name, when one could be recovered safely.
### Type Properties
- [static let defaultPreviewByteLimit: Int](./rejectedtoolcall/defaultpreviewbytelimit.md)
  The default maximum number of UTF-8 bytes retained in [`rawTextPreview`](./rejectedtoolcall/rawtextpreview.md).
### Enumerations
- [RejectedToolCall.Reason](./rejectedtoolcall/reason-swift.enum.md)
  Why the model output could not become an executable [`ToolCall`](./toolcall.md).
### Default Implementations
- [Encodable Implementations](./rejectedtoolcall/encodable-implementations.md)
- [Equatable Implementations](./rejectedtoolcall/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rejectedtoolcall)*