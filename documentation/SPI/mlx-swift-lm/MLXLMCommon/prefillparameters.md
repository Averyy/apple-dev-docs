---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters"
framework: "mlx-swift-lm/MLXLMCommon"
---

# PrefillParameters

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Parameters controlling how a prompt is prefilled into the [`KVCache`](./kvcache.md).

## Declaration

```swift
struct PrefillParameters
```

## Overview

Set via [`prefill`](./generateparameters/prefill.md) and passed to [`prepare(_:cache:state:prefill:)`](./languagemodel/prepare%28_,cache,state,prefill%29.md):

```swift
var parameters = GenerateParameters()
parameters.prefill.stepSize = 1024
parameters.prefill.progress = { processed, total in ... }
```

## Topics

### Initializers
- [init(stepSize: Int?, chunking: Chunking, progress: (@Sendable (_ processed: Int, _ total: Int) -> Void)?, prefix: (@Sendable (_ positions: Int) -> Void)?)](./prefillparameters/init%28stepsize,chunking,progress,prefix%29.md)
### Instance Properties
- [var chunking: Chunking](./prefillparameters/chunking-swift.property.md)
  How the prompt is divided into forwards. See [`PrefillParameters.Chunking`](./prefillparameters/chunking-swift.enum.md).
- [var prefix: (@Sendable (_ positions: Int) -> Void)?](./prefillparameters/prefix.md)
  Called once, before the first prefill forward, with the positions the cache already holds.
- [var progress: (@Sendable (_ processed: Int, _ total: Int) -> Void)?](./prefillparameters/progress.md)
  Called after each prefill chunk with `(processedPositions, totalPositions)`.
- [var stepSize: Int?](./prefillparameters/stepsize.md)
  Ceiling on tokens evaluated per prefill forward. `nil` lets each model pick its own default (512 for the generic path; the Gemma 3 text path uses a smaller, tuned chunk).
### Instance Methods
- [func chunkLength(forChunking: Int, defaultStepSize: Int, maximumStepSize: Int?) -> Int?](./prefillparameters/chunklength%28forchunking,defaultstepsize,maximumstepsize%29.md)
  The per-forward chunk length for prefilling `count` positions, or `nil` when the prompt should go through in a single forward ([`PrefillParameters.Chunking.unchunked`](./prefillparameters/chunking-swift.enum/unchunked.md)).
- [func forEachChunk(total: Int, reserving: Int, defaultStepSize: Int, maximumStepSize: Int?, (Range<Int>) -> Void) throws -> Int](./prefillparameters/foreachchunk%28total,reserving,defaultstepsize,maximumstepsize,_%29.md)
  Drives a chunked prefill over `total` positions and returns the number of positions processed.
- [func resolvedStepSize(defaultStepSize: Int, maximumStepSize: Int?) -> Int](./prefillparameters/resolvedstepsize%28defaultstepsize,maximumstepsize%29.md)
  The effective step-size ceiling: [`stepSize`](./prefillparameters/stepsize.md) if set, else the model’s `defaultStepSize`, clamped to `maximumStepSize` and floored at 1.
### Type Properties
- [static let defaultStepSize: Int](./prefillparameters/defaultstepsize.md)
  The step size used when neither [`stepSize`](./prefillparameters/stepsize.md) nor a model default applies.
### Enumerations
- [PrefillParameters.Chunking](./prefillparameters/chunking-swift.enum.md)
  Strategy dividing the prompt into prefill forwards.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters)*