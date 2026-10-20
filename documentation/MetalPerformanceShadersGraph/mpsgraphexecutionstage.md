# MPSGraphExecutionStage

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum  
**Role**: Enumeration

Execution events that can be used with shared events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphExecutionStage
```

```c
enum MPSGraphExecutionStage : uint64_t;
```

## Topics

### Enumeration Cases
- [MPSGraphExecutionStage.completed](./mpsgraphexecutionstage/completed.md)
  stage when execution of the graph completes.
### Initializers
- [init?(rawValue: UInt64)](./mpsgraphexecutionstage/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutionstage)*