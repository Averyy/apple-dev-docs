# Observable

**Framework**: Observation  
**Kind**: protocol

A type that emits notifications to observers when underlying data changes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
protocol Observable
```

## Mentions

- [Applying Macros](../swift/applying-macros.md)

#### Overview

Conforming to this protocol signals to other APIs that the type supports observation. However, applying the `Observable` protocol by itself to a type doesn’t add observation functionality to the type. Instead, always use the [`Observable()`](observable().md) macro when adding observation support to a type.

## See Also

- [macro Observable()](observable().md)
  Defines and implements conformance of the Observable protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/observable)*