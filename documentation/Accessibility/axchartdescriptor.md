# AXChartDescriptor

**Framework**: Accessibility  
**Kind**: class

An object that contains all the semantic information about an accessible chart.

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
class AXChartDescriptor
```

## Mentions

- [Representing chart data as an audio graph](representing-chart-data-as-an-audio-graph.md)

## Topics

### Creating a chart
- [convenience init(title: String?, summary: String?, xAxis: any AXDataAxisDescriptor, yAxis: AXNumericDataAxisDescriptor?, additionalAxes: [any AXDataAxisDescriptor], series: [AXDataSeriesDescriptor])](axchartdescriptor/init(title:summary:xaxis:yaxis:additionalaxes:series:).md)
  Creates a chart descriptor with the specified title, summary, x-axis descriptor, y-axis descriptor, descriptors for additional axes, and array of data series.
- [convenience init(attributedTitle: NSAttributedString?, summary: String?, xAxis: any AXDataAxisDescriptor, yAxis: AXNumericDataAxisDescriptor?, additionalAxes: [any AXDataAxisDescriptor], series: [AXDataSeriesDescriptor])](axchartdescriptor/init(attributedtitle:summary:xaxis:yaxis:additionalaxes:series:).md)
  Creates a chart descriptor with the specified attributed title, summary, x-axis descriptor, y-axis descriptor, descriptors for additional axes, and array of data series.
### Specifying the chart title
- [var title: String?](axchartdescriptor/title.md)
  The title of the chart.
- [var attributedTitle: NSAttributedString?](axchartdescriptor/attributedtitle.md)
  An attributed version of the chart title.
### Specifying the chart summary
- [var summary: String?](axchartdescriptor/summary.md)
  A description of the key takeaways or features of the chart.
### Specifying the axes
- [var xAxis: any AXDataAxisDescriptor](axchartdescriptor/xaxis-7sb9a.md)
  The axis descriptor for the chart’s x-axis.
- [var yAxis: AXNumericDataAxisDescriptor?](axchartdescriptor/yaxis.md)
  The axis descriptor for the chart’s y-axis.
- [var additionalAxes: [any AXDataAxisDescriptor]](axchartdescriptor/additionalaxes-2adwh.md)
  The descriptors for additional categorical or numerical axes beyond the x-axis and y-axis.
- [protocol AXDataAxisDescriptor](axdataaxisdescriptor.md)
  The basic interface for a data axis in a chart.
### Specifying a series of data points
- [var series: [AXDataSeriesDescriptor]](axchartdescriptor/series.md)
  The descriptors for each data series in the chart.
- [class AXDataSeriesDescriptor](axdataseriesdescriptor.md)
  An object that represents a series of data points.
### Specifying the content layout
- [var contentFrame: CGRect](axchartdescriptor/contentframe.md)
  The bounds of the view, in screen coordinates, for visually rendering data values.
- [var contentDirection: AXChartDescriptor.ContentDirection](axchartdescriptor/contentdirection-swift.property.md)
  The direction of the content in the chart.
- [AXChartDescriptor.ContentDirection](axchartdescriptor/contentdirection-swift.enum.md)
  A constant that describes the content direction of the chart.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol AXChart](axchart.md)
  A protocol that declares the minimum interface necessary for an accessibility element to act as a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axchartdescriptor)*