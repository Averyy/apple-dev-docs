# init(x:yStart:yEnd:domain:function:)

**Framework**: Swift Charts  
**Kind**: init

Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).

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
init(x: LocalizedStringResource, yStart: LocalizedStringResource, yEnd: LocalizedStringResource, domain: ClosedRange<Double>? = nil, function: @escaping (Double) -> (yStart: Double, yEnd: Double))
```

#### Discussion

Parameters:

- x: The localized string resource for the x label.
- yStart: The localized string resource for the start label.
- yEnd: The localized string resource for the end label.
- domain: The domain of x. If set to `nil`, the domain of the chart’s x scale will be used.
- function: The function to graph. Returns a tuple of (yStart: yStart, yEnd: yEnd).

> **Note**: For x values where the function is undefined or is infinity, the function is expected to return `Double.nan` or `Double.infinity` respectively.

## See Also

- [init(x: Text, y: Text, domain: ClosedRange<Double>?, function: (Double) -> Double)](areaplot/init(x:y:domain:function:)-2fab1.md)
  Creates a mark that fills the area between zero and the given function.
- [init(x: LocalizedStringResource, y: LocalizedStringResource, domain: ClosedRange<Double>?, function: (Double) -> Double)](areaplot/init(x:y:domain:function:)-1jmpp.md)
  Creates a mark that fills the area between zero and the given function.
- [init(x: LocalizedStringKey, y: LocalizedStringKey, domain: ClosedRange<Double>?, function: (Double) -> Double)](areaplot/init(x:y:domain:function:)-etud.md)
  Creates a mark that fills the area between zero and the given function.
- [init<S1, S2>(x: S1, y: S2, domain: ClosedRange<Double>?, function: (Double) -> Double)](areaplot/init(x:y:domain:function:)-39eit.md)
  Creates a mark that fills the area between zero and the given function.
- [init(x: Text, yStart: Text, yEnd: Text, domain: ClosedRange<Double>?, function: (Double) -> (yStart: Double, yEnd: Double))](areaplot/init(x:ystart:yend:domain:function:)-etcn.md)
  Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init(x: LocalizedStringKey, yStart: LocalizedStringKey, yEnd: LocalizedStringKey, domain: ClosedRange<Double>?, function: (Double) -> (yStart: Double, yEnd: Double))](areaplot/init(x:ystart:yend:domain:function:)-5akqm.md)
  Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init<S1, S2, S3>(x: S1, yStart: S2, yEnd: S3, domain: ClosedRange<Double>?, function: (Double) -> (yStart: Double, yEnd: Double))](areaplot/init(x:ystart:yend:domain:function:)-23gxe.md)
  Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/areaplot/init(x:ystart:yend:domain:function:)-9gui6)*