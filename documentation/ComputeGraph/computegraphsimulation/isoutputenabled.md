# isOutputEnabled(_:)

**Framework**: ComputeGraph  
**Kind**: method

Returns whether the specified output is currently enabled for simulation.

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
final func isOutputEnabled(_ outputID: Int) -> Bool
```

#### Return Value

`true` if the output is simulated; `false` if it is disabled.

## Parameters

- `outputID`: The node identifier of the output to query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/isoutputenabled(_:))*