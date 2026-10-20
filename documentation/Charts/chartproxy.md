# ChartProxy

**Framework**: Swift Charts  
**Kind**: struct  
**Role**: Structure

A proxy that you use to access the scales and plot area of a chart.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct ChartProxy
```

#### Overview

You get a chart proxy from the [`chartOverlay(alignment:content:)`](../SwiftUI/view/chartoverlay%28alignment,content%29.md) and [`chartBackground(alignment:content:)`](../SwiftUI/view/chartbackground%28alignment,content%29.md) modifiers. You can use the chart proxy to convert data values to screen coordinates or vice-versa.

Below is an example where we convert the screen coordinates from a drag gesture to data values.

```swift
Chart(data) {
    LineMark(
        x: .value("date", $0.date),
        y: .value("price", $0.price)
    )
}
.chartOverlay { proxy in
    GeometryReader { geometry in
        Rectangle().fill(.clear).contentShape(Rectangle())
            .gesture(
                DragGesture()
                    .onChanged { value in
                        // Convert the gesture location to the coordinate space of the plot area.
                        let origin = geometry[proxy.plotAreaFrame].origin
                        let location = CGPoint(
                            x: value.location.x - origin.x,
                            y: value.location.y - origin.y
                        )
                        // Get the x (date) and y (price) value from the location.
                        let (date, price) = proxy.value(at: location, as: (Date, Double).self)
                        print("Location: \(date), \(price)")
                    }
            )
    }
}
```

## Topics

### Instance Properties
- [var plotAreaFrame: Anchor<CGRect>](./chartproxy/plotareaframe.md)
  An anchor to the frame of the chart’s plot.
- [var plotAreaSize: CGSize](./chartproxy/plotareasize.md)
  The size of the plot in the chart.
- [var plotContainerFrame: Anchor<CGRect>?](./chartproxy/plotcontainerframe.md)
  An anchor to the frame of the chart’s plot container, or `nil` if there is no chart in the context of the chart proxy.
- [var plotFrame: Anchor<CGRect>?](./chartproxy/plotframe.md)
  An anchor to the frame of the chart’s plot, or `nil` if there is no chart in the context of the chart proxy.
- [var plotSize: CGSize](./chartproxy/plotsize.md)
  The size of the plot in the chart.
### Instance Methods
- [func angle(at: CGPoint) -> Angle](./chartproxy/angle%28at%29.md)
  Returns the angle relative to the plot area center, where the 12 o’clock position is interpreted as zero degrees, increasing clockwise.
- [func foregroundStyle<P>(for: P) -> AnyShapeStyle?](./chartproxy/foregroundstyle%28for%29.md)
  Returns the foreground style for the given data value. Returns `nil` if the foreground style scale is unavailable, or the value is invalid.
- [func foregroundStyleDomain<P>(dataType: P.Type) -> [P]](./chartproxy/foregroundstyledomain%28datatype%29.md)
- [func lineStyle<P>(for: P) -> StrokeStyle?](./chartproxy/linestyle%28for%29.md)
  Returns the line style for the given data value. Returns `nil` if the line style scale is unavailable, or the value is invalid.
- [func lineStyleDomain<P>(dataType: P.Type) -> [P]](./chartproxy/linestyledomain%28datatype%29.md)
- [func position<X, Y>(for: (x: X, y: Y)) -> CGPoint?](./chartproxy/position%28for%29.md)
  Returns the x and y positions as a `CGPoint` for the given data values, or `nil` if either the X or the y scale is unavailable or if any data value is invalid. The returned position is relative to the plot.
- [func position<P>(forX: P) -> CGFloat?](./chartproxy/position%28forx%29.md)
  Returns the x position for the given data value, or `nil` if the x scale is unavailable or if the data value is invalid. The returned position is relative to the plot.
- [func position<P>(forY: P) -> CGFloat?](./chartproxy/position%28fory%29.md)
  Returns the y position for the given data value, or `nil` if the y scale is unavailable or if the data value is invalid. The returned position is relative to the plot.
- [func positionRange<X, Y>(for: (x: X, y: Y)) -> CGRect?](./chartproxy/positionrange%28for%29.md)
  Returns the range of x and y positions for the given pair of data values, or `nil` if the y scale is unavailable or if the value is invalid.
- [func positionRange<P>(forX: P) -> ClosedRange<CGFloat>?](./chartproxy/positionrange%28forx%29.md)
  Returns the range of x position for the given data value, or `nil` if the x scale is unavailable or if the value is invalid. The returned position range is relative to the plot.
- [func positionRange<P>(forY: P) -> ClosedRange<CGFloat>?](./chartproxy/positionrange%28fory%29.md)
  Returns the range of y position for the given data value, or `nil` if the x scale is unavailable or if the value is invalid. The returned position range is relative to the plot.
- [func selectAngleValue(at: Angle)](./chartproxy/selectanglevalue%28at%29.md)
- [func selectXRange(from: CGFloat, to: CGFloat)](./chartproxy/selectxrange%28from,to%29.md)
- [func selectXValue(at: CGFloat)](./chartproxy/selectxvalue%28at%29.md)
- [func selectYRange(from: CGFloat, to: CGFloat)](./chartproxy/selectyrange%28from,to%29.md)
- [func selectYValue(at: CGFloat)](./chartproxy/selectyvalue%28at%29.md)
- [func symbol<P>(for: P) -> AnyChartSymbolShape?](./chartproxy/symbol%28for%29.md)
  Returns the symbol for the given data value. Returns `nil` if the symbol scale is unavailable, or the value is invalid.
- [func symbolDomain<P>(dataType: P.Type) -> [P]](./chartproxy/symboldomain%28datatype%29.md)
- [func symbolSize<P>(for: P) -> CGFloat?](./chartproxy/symbolsize%28for%29.md)
  Returns the symbol size for the given data value. Returns `nil` if the symbol size scale is unavailable, or the value is invalid.
- [func symbolSizeDomain<P>(dataType: P.Type) -> [P]](./chartproxy/symbolsizedomain%28datatype%29.md)
- [func value<X, Y>(at: CGPoint, as: (X, Y).Type) -> (X, Y)?](./chartproxy/value%28at,as%29.md)
  Returns the data values at the given position, or `nil` if the position does not correspond to a valid Y value.
- [func value<P>(atAngle: Angle, as: P.Type) -> P?](./chartproxy/value%28atangle,as%29.md)
  Returns the data value at the given angle, or `nil` if the angle does not correspond to a valid data value.
- [func value<P>(atX: CGFloat, as: P.Type) -> P?](./chartproxy/value%28atx,as%29.md)
  Returns the data value at the given x position, or `nil` if the position does not correspond to a valid X value.
- [func value<P>(atY: CGFloat, as: P.Type) -> P?](./chartproxy/value%28aty,as%29.md)
  Returns the data value at the given y position, or `nil` if the position does not correspond to a valid Y value.
- [func xDomain<P>(dataType: P.Type) -> [P]](./chartproxy/xdomain%28datatype%29.md)
- [func yDomain<P>(dataType: P.Type) -> [P]](./chartproxy/ydomain%28datatype%29.md)

## See Also

### Chart management
- [struct ChartPlotContent](./chartplotcontent.md)
  A view that represents a chart’s plot area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartproxy)*