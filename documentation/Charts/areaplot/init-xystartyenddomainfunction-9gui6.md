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


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/areaplot/init(x:ystart:yend:domain:function:)-9gui6)*