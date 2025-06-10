# init(x:y:domain:function:)

**Framework**: Swift Charts  
**Kind**: init

Creates a mark that fills the area between zero and the given function.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
init(x: LocalizedStringKey, y: LocalizedStringKey, domain: ClosedRange<Double>? = nil, function: @escaping (Double) -> Double)
```

#### Discussion

Parameters:

- x: The localized string key for the x label.
- y: The localized string key for the y label.
- domain: The domain of x. If set to `nil`, the domain of the chart’s x scale will be used.
- function: The function to graph..

> **Note**: For x values where the function is undefined or is infinity, the function is expected to return `Double.nan` or `Double.infinity` respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/areaplot/init(x:y:domain:function:)-etud)*