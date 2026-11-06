# MTLForwardProgressUsage

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

Options for how a pipeline depends on blocking synchronization across SIMD groups.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum MTLForwardProgressUsage
```

```c
enum MTLForwardProgressUsage : NSInteger;
```

## Overview

These options tune the GPU scheduler for different synchronization patterns.

## Topics

### Enumeration Cases
- [MTLForwardProgressUsage.automatic](./mtlforwardprogressusage/automatic.md)
  Instructs the Metal compiler to decide which forward progress mode to apply to the pipeline by analyzing its program.
- [MTLForwardProgressUsage.simdGroupParallel](./mtlforwardprogressusage/simdgroupparallel.md)
  Tunes the pipeline for programs that frequently impede forward progress, such as spin loops or locks.
- [MTLForwardProgressUsage.weak](./mtlforwardprogressusage/weak.md)
  Tunes the pipeline for programs that infrequently impede forward progress, such as spin loops or locks.
### Initializers
- [init?(rawValue: Int)](./mtlforwardprogressusage/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlforwardprogressusage)*