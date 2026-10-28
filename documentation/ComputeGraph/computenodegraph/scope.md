# ComputeNodeGraph.Scope

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

A scope is a named region of memory, indicating where a value lives

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
struct Scope
```

## Overview

A value that exists on each element of a simulation would have a scope of [`element`](../element.md), whereas a value that exists on the emitter stage would have a scope of [`emitter`](../emitter.md).

Each stage of execution provides a subset of available scopes. Stages such as [`group`](../group.md) are available only when grouping is enabled for particles.

## Topics

### Initializers
- [init(String)](./scope/init%28_%29.md)
### Instance Properties
- [let name: String](./scope/name.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/scope)*