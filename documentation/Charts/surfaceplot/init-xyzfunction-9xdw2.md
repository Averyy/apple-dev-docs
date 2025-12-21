# init(x:y:z:function:)

**Framework**: Swift Charts  
**Kind**: init

Creates a SurfacePlot that represents a function y = f(x, z).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
init(x: some StringProtocol, y: some StringProtocol, z: some StringProtocol, function: @escaping (Double, Double) -> Double)
```

#### Discussion

> **Note**: For x values where the function is undefined or is infinity, the function is expected to return `Double.nan`

## Parameters

- `x`: The x label.
- `y`: The y label.
- `z`: The z label.
- `function`: The function to graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/surfaceplot/init(x:y:z:function:)-9xdw2)*