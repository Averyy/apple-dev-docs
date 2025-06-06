# MPSGraphOptions

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum

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

## Topics

### Enumeration Cases
- [MPSGraphOptions.none](mpsgraphoptions/none.md)
  No Options.
- [MPSGraphOptions.synchronizeResults](mpsgraphoptions/synchronizeresults.md)
  The graph synchronizes results to the CPU using a blit encoder if on a discrete GPU at the end of execution.
- [MPSGraphOptions.verbose](mpsgraphoptions/verbose.md)
  The framework prints more logging info.
### Initializers
- [init?(rawValue: UInt64)](mpsgraphoptions/init(rawvalue:).md)
### Type Properties
- [static var `default`: MPSGraphOptions](mpsgraphoptions/default.md)
  The framework uses these options as default if not overriden.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphoptions)*