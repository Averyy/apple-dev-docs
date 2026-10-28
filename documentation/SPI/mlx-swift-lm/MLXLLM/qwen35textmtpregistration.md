---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35textmtpregistration"
framework: "mlx-swift-lm/MLXLLM"
---

# Qwen35TextMTPRegistration

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: enum  
**Role**: Enumeration

Registers Qwen3.5-family text MTP drafter model types.

## Declaration

```swift
enum Qwen35TextMTPRegistration
```

## Overview

Standalone Qwen MTP checkpoints do not identify the verifier architecture: their `vision_config` is empty for both text and multimodal use. Text and multimodal drafters therefore use separate registries instead of relying on config-shape predicates or registration order.

## Topics

### Type Methods
- [static func register() async](./qwen35textmtpregistration/register%28%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/qwen35textmtpregistration)*