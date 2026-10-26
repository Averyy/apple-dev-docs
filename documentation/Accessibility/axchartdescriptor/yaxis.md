# yAxis

**Framework**: Accessibility  
**Kind**: property  
**Role**: Instance Property

The axis descriptor for the chart’s y-axis.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var yAxis: AXNumericDataAxisDescriptor? { get set }
```

```objc
@property (nonatomic, strong, nullable) AXNumericDataAxisDescriptor * yAxis;
```

## See Also

### Specifying the axes
- [var xAxis: any AXDataAxisDescriptor](./xaxis-7sb9a.md)
  The axis descriptor for the chart’s x-axis.
- [var additionalAxes: [any AXDataAxisDescriptor]](./additionalaxes-2adwh.md)
  The descriptors for additional categorical or numerical axes beyond the x-axis and y-axis.
- [protocol AXDataAxisDescriptor](../axdataaxisdescriptor.md)
  The basic interface for a data axis in a chart.
- [xAxis](./xaxis-6dnxd.md)
  The axis descriptor for the chart’s x-axis.
- [additionalAxes](./additionalaxes-9ldc0.md)
  The descriptors for additional categorical or numerical axes beyond the x-axis and y-axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axchartdescriptor/yaxis)*