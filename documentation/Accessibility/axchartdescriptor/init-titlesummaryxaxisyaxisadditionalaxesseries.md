# init(title:summary:xAxis:yAxis:additionalAxes:series:)

**Framework**: Accessibility  
**Kind**: init

Creates a chart descriptor with the specified title, summary, x-axis descriptor, y-axis descriptor, descriptors for additional axes, and array of data series.

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
convenience init(title: String? = nil, summary: String? = nil, xAxis: any AXDataAxisDescriptor, yAxis: AXNumericDataAxisDescriptor? = nil, additionalAxes: [any AXDataAxisDescriptor] = [], series: [AXDataSeriesDescriptor])
```

## See Also

- [convenience init(attributedTitle: NSAttributedString?, summary: String?, xAxis: any AXDataAxisDescriptor, yAxis: AXNumericDataAxisDescriptor?, additionalAxes: [any AXDataAxisDescriptor], series: [AXDataSeriesDescriptor])](axchartdescriptor/init(attributedtitle:summary:xaxis:yaxis:additionalaxes:series:).md)
  Creates a chart descriptor with the specified attributed title, summary, x-axis descriptor, y-axis descriptor, descriptors for additional axes, and array of data series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axchartdescriptor/init(title:summary:xaxis:yaxis:additionalaxes:series:))*