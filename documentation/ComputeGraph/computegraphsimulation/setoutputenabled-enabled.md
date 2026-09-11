# setOutputEnabled(_:enabled:)

**Framework**: Compute Graph  
**Kind**: method

Enables or disables execution of the provided output stage, without disabling the system it represents.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
final func setOutputEnabled(_ outputID: Int, enabled: Bool)
```

#### Discussion

Disabling an output is useful when you want to switch between multiple outputs for the simulation, for example two outputs with different topologies for the same elements.

## Parameters

- `outputID`: The node identifier of the output to enable or disable.
- `enabled`: `true` to simulate the output; `false` to omit it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/setoutputenabled(_:enabled:))*