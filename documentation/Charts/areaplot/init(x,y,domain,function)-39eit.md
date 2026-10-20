# init(x:y:domain:function:)

**Framework**: Swift Charts  
**Kind**: init  
**Role**: Initializer

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
init<S1, S2>(x: S1, y: S2, domain: ClosedRange<Double>? = nil, function: @escaping @Sendable (Double) -> Double) where S1 : StringProtocol, S2 : StringProtocol
```

Available when `Content` is `FunctionAreaPlotContent`.

#### Discussion

Parameters:

- x: The localized string key for the x label.
- y: The localized string key for the y label.
- domain: The domain of x. If set to `nil`, the domain of the chart’s x scale will be used.
- function: The function to graph..

> **Note**: For x values where the function is undefined or is infinity, the function is expected to return `Double.nan` or `Double.infinity` respectively.

## See Also

### Plotting functions
- [init(x: Text, y: Text, domain: ClosedRange<Double>?, function: (Double) -> Double)](./init%28x,y,domain,function%29-2fab1.md)
  Creates a mark that fills the area between zero and the given function.
- [init(x: LocalizedStringResource, y: LocalizedStringResource, domain: ClosedRange<Double>?, function: (Double) -> Double)](./init%28x,y,domain,function%29-1jmpp.md)
  Creates a mark that fills the area between zero and the given function.
- [init(x: LocalizedStringKey, y: LocalizedStringKey, domain: ClosedRange<Double>?, function: (Double) -> Double)](./init%28x,y,domain,function%29-etud.md)
  Creates a mark that fills the area between zero and the given function.
- [init(x: Text, yStart: Text, yEnd: Text, domain: ClosedRange<Double>?, function: (Double) -> (yStart: Double, yEnd: Double))](./init%28x,ystart,yend,domain,function%29-etcn.md)
  Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init(x: LocalizedStringResource, yStart: LocalizedStringResource, yEnd: LocalizedStringResource, domain: ClosedRange<Double>?, function: (Double) -> (yStart: Double, yEnd: Double))](./init%28x,ystart,yend,domain,function%29-9gui6.md)
  Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init(x: LocalizedStringKey, yStart: LocalizedStringKey, yEnd: LocalizedStringKey, domain: ClosedRange<Double>?, function: (Double) -> (yStart: Double, yEnd: Double))](./init%28x,ystart,yend,domain,function%29-5akqm.md)
  Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init<S1, S2, S3>(x: S1, yStart: S2, yEnd: S3, domain: ClosedRange<Double>?, function: (Double) -> (yStart: Double, yEnd: Double))](./init%28x,ystart,yend,domain,function%29-23gxe.md)
  Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/areaplot/init(x:y:domain:function:)-39eit)*