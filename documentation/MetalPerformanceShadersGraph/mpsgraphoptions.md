# MPSGraphOptions

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum  
**Role**: Enumeration

The options available to a graph.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphOptions
```

```c
enum MPSGraphOptions : uint64_t;
```

## Topics

### Enumeration Cases
- [MPSGraphOptions.none](./mpsgraphoptions/none.md)
  No Options.
- [MPSGraphOptions.synchronizeResults](./mpsgraphoptions/synchronizeresults.md)
  The graph synchronizes results to the CPU using a blit encoder if on a discrete GPU at the end of execution.
- [MPSGraphOptions.verbose](./mpsgraphoptions/verbose.md)
  The framework prints more logging info.
### Initializers
- [init?(rawValue: UInt64)](./mpsgraphoptions/init%28rawvalue%29.md)
### Type Properties
- [static var `default`: MPSGraphOptions](./mpsgraphoptions/default.md)
  The framework uses these options as default if not overriden.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphoptions)*