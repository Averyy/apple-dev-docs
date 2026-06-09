# ComputeNodeGraph.Scope

**Framework**: ComputeGraph  
**Kind**: struct

A scope is a named region of memory, indicating where a value lives

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
struct Scope
```

#### Overview

A value that exists on each element of a simulation would have a scope of [`element`](element.md), whereas a value that exists on the emitter stage would have a scope of [`emitter`](emitter.md).

Each stage of execution provides a subset of available scopes. Stages such as [`group`](group.md) are available only when grouping is enabled for particles.

## Topics

### Initializers
- [init(String)](computenodegraph/scope/init(_:).md)
### Instance Properties
- [let name: String](computenodegraph/scope/name.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/scope)*