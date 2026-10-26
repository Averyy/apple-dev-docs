---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/paroquantpreparedcheckpoint"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ParoQuantPreparedCheckpoint

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Prepared Checkpoint — the once-converted MLX-native form of a PARO checkpoint, stored beside the original so later loads skip the AutoAWQ conversion (unpack/reorder/repack, Mamba split, MoE expert stacking, rotation-key remap).

## Declaration

```swift
enum ParoQuantPreparedCheckpoint
```

#### Overview

Rotation parameters (`theta` / `pairs` / `channel_scales`) are stored verbatim and every rotation-derived value is recomputed at load by `prepareDerivedRotationState()` — nothing semantic is baked into the artifact, only layout conversion whose output is deterministic.

The artifact is self-describing: its safetensors metadata carries a manifest of the source files it was converted from plus a format version. Any mismatch (source re-download, conversion-semantics change) or read failure makes the loader silently fall back to full conversion and rewrite the artifact — a Prepared Checkpoint can never fail a load that would otherwise succeed.

## Topics

### Type Properties
- [static let excludedFileNames: Set<String>](./paroquantpreparedcheckpoint/excludedfilenames.md)
  File names that must never be treated as checkpoint sources — by the loader’s raw-safetensors scan, by the manifest, and by any caller computing weight identity over the directory (e.g. the app’s `ModelFingerprint`).
- [static let fileName: String](./paroquantpreparedcheckpoint/filename.md)
  Artifact file name, written into the checkpoint directory.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/paroquantpreparedcheckpoint)*