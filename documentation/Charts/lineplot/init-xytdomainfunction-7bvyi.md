# init(x:y:t:domain:function:)

**Framework**: Swift Charts  
**Kind**: init

Creates a mark that graphs a parametric function (x, y) = f(t).

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
init(x: LocalizedStringKey, y: LocalizedStringKey, t: LocalizedStringKey, domain: ClosedRange<Double>, function: @escaping (Double) -> (x: Double, y: Double))
```

#### Discussion

Parameters:

- x: The localized string key for the x label.
- y: The localized string key for the y label.
- t: The localized string key for the t label.
- domain: The domain of t. Must be a finite domain.
- function: The function to graph. Returns a tuple of (x, y) for a value of t.

> **Note**: For t values where the function is undefined or is infinity, the function is expected to return `Double.nan` or `Double.infinity` respectively.

## See Also

- [init(x: Text, y: Text, t: Text, domain: ClosedRange<Double>, function: (Double) -> (x: Double, y: Double))](lineplot/init(x:y:t:domain:function:)-5c4bo.md)
  Creates a mark that graphs a parametric function (x, y) = f(t).
- [init(x: LocalizedStringResource, y: LocalizedStringResource, t: LocalizedStringResource, domain: ClosedRange<Double>, function: (Double) -> (x: Double, y: Double))](lineplot/init(x:y:t:domain:function:)-610ta.md)
  Creates a mark that graphs a parametric function (x, y) = f(t).
- [init<S1, S2, S3>(x: S1, y: S2, t: S3, domain: ClosedRange<Double>, function: (Double) -> (x: Double, y: Double))](lineplot/init(x:y:t:domain:function:)-3mqls.md)
  Creates a mark that graphs a parametric function (x, y) = f(t).


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/lineplot/init(x:y:t:domain:function:)-7bvyi)*