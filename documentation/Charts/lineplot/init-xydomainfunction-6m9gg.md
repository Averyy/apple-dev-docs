# init(x:y:domain:function:)

**Framework**: Swift Charts  
**Kind**: init

Creates a mark that graphs a function y = f(x).

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
init(x: Text, y: Text, domain: ClosedRange<Double>? = nil, function: @escaping (Double) -> Double)
```

#### Discussion

Parameters:

- x: The x label.
- y: The y label.
- domain: The domain of x. If set to `nil`, the domain of the chart’s x scale will be used.
- function: The function to graph.

> **Note**: For x values where the function is undefined or is infinity, the function is expected to return `Double.nan` or `Double.infinity` respectively.

## See Also

- [init(x: LocalizedStringKey, y: LocalizedStringKey, domain: ClosedRange<Double>?, function: (Double) -> Double)](lineplot/init(x:y:domain:function:)-1135f.md)
  Creates a mark that graphs a function y = f(x).
- [init(x: LocalizedStringResource, y: LocalizedStringResource, domain: ClosedRange<Double>?, function: (Double) -> Double)](lineplot/init(x:y:domain:function:)-17i43.md)
  Creates a mark that graphs a function y = f(x).
- [init<S1, S2>(x: S1, y: S2, domain: ClosedRange<Double>?, function: (Double) -> Double)](lineplot/init(x:y:domain:function:)-6gv5v.md)
  Creates a mark that graphs a function y = f(x).


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/lineplot/init(x:y:domain:function:)-6m9gg)*