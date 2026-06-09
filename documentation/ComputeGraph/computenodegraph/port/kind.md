# ComputeNodeGraph.Port.Kind

**Framework**: ComputeGraph  
**Kind**: enum

The semantic role of a port, determining what it carries along an edge and whether the edge imposes execution ordering between its endpoints.

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
enum Kind
```

## Topics

### Enumeration Cases
- [ComputeNodeGraph.Port.Kind.context](computenodegraph/port/kind/context.md)
  Carries an ambient runtime context handle injected by the graph at execution time. Destination reads the handle; no ordering effect.
- [ComputeNodeGraph.Port.Kind.dependency](computenodegraph/port/kind/dependency.md)
  Pure “happens-after” edge. No runtime payload, no type lineage, no type compatibility check. The destination is ordered after the source but does not consume its output. Use this to splice a node (e.g. a compute stage) into execution order between two unrelated nodes.
- [ComputeNodeGraph.Port.Kind.event](computenodegraph/port/kind/event.md)
  Carries a typed event payload. Triggers downstream execution per event AND carries data (e.g. spawn/update/terminate events with element data).
- [ComputeNodeGraph.Port.Kind.flow](computenodegraph/port/kind/flow.md)
  Execution-ordering edge whose destination is conceptually a consumer of the source’s typed output. No runtime payload is transferred, but type compatibility is enforced. Used for stage → stage sequencing.
- [ComputeNodeGraph.Port.Kind.state](computenodegraph/port/kind/state.md)
  Carries a read/write binding to named external storage (element, emitter, group, output attribute, threadgroup memory). Type is always `.state(definition:)`. No ordering effect.
- [ComputeNodeGraph.Port.Kind.value](computenodegraph/port/kind/value.md)
  Carries a typed data value from source to destination. One-way read, no ordering effect.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/port/kind)*