# yAxis

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The input object that represents the y-axis on the directional pad.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var yAxis: any GCAxisInput { get }
```

```objc
@property (readonly) id<GCAxisInput> yAxis;
```

## See Also

### Axes
- [var xAxis: any GCAxisInput](./xaxis.md)
  The input object that represents the x-axis on the directional pad.
- [var xyAxes: any GCAxis2DInput](./xyaxes.md)
  The location of the directional pad represented as a point.
- [protocol GCAxis2DInput](../gcaxis2dinput.md)
  The common properties of inputs that provide a normalized point in a two-dimensional coordinate system with a fixed origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdirectionpadelement/yaxis)*