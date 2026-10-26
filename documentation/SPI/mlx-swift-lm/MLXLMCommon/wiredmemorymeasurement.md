---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredmemorymeasurement"
framework: "mlx-swift-lm/MLXLMCommon"
---

# WiredMemoryMeasurement

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Result of a wired memory measurement pass.

## Declaration

```swift
struct WiredMemoryMeasurement
```

## Topics

### Instance Properties
- [let kvBytes: Int](./wiredmemorymeasurement/kvbytes.md)
  Total bytes for KV caches after prefill.
- [let peakActiveBytes: Int](./wiredmemorymeasurement/peakactivebytes.md)
  Peak active memory observed during prefill.
- [let prefillStepSize: Int](./wiredmemorymeasurement/prefillstepsize.md)
  Prefill step size used for the measurement.
- [let tokenCount: Int](./wiredmemorymeasurement/tokencount.md)
  Number of tokens used during the prefill measurement.
- [var totalBytes: Int](./wiredmemorymeasurement/totalbytes.md)
  Combined budget suggestion (weights + KV + workspace).
- [let weightBytes: Int](./wiredmemorymeasurement/weightbytes.md)
  Total bytes for model weights (`nbytes` sum).
- [let workspaceBytes: Int](./wiredmemorymeasurement/workspacebytes.md)
  Estimated transient workspace bytes (prefill peak minus weights + KV).

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredmemorymeasurement)*