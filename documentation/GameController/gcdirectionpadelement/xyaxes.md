# xyAxes

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The location of the directional pad represented as a point.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.3+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var xyAxes: any GCAxis2DInput { get }
```

```objc
@property (readonly) id<GCAxis2DInput> xyAxes;
```

## See Also

### Axes
- [var xAxis: any GCAxisInput](./xaxis.md)
  The input object that represents the x-axis on the directional pad.
- [var yAxis: any GCAxisInput](./yaxis.md)
  The input object that represents the y-axis on the directional pad.
- [protocol GCAxis2DInput](../gcaxis2dinput.md)
  The common properties of inputs that provide a normalized point in a two-dimensional coordinate system with a fixed origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdirectionpadelement/xyaxes)*