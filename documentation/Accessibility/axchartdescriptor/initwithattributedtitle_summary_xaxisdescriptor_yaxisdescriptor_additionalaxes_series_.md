# initWithAttributedTitle:summary:xAxisDescriptor:yAxisDescriptor:additionalAxes:series:

**Framework**: Accessibility  
**Kind**: method  
**Role**: Instance Method

Creates a chart descriptor with the specified attributed title, summary, x-axis descriptor, y-axis descriptor, descriptors for additional axes, and array of data series.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
- (instancetype) initWithAttributedTitle:(NSAttributedString *) attributedTitle summary:(NSString *) summary xAxisDescriptor:(id<AXDataAxisDescriptor>) xAxis yAxisDescriptor:(AXNumericDataAxisDescriptor *) yAxis additionalAxes:(NSArray<id<AXDataAxisDescriptor>> *) additionalAxes series:(NSArray<AXDataSeriesDescriptor *> *) series;
```

## See Also

### Creating a chart
- [- initWithTitle:summary:xAxisDescriptor:yAxisDescriptor:series:](./initwithtitle_summary_xaxisdescriptor_yaxisdescriptor_series_.md)
  Creates a chart descriptor with the specified title, summary, x-axis descriptor, y-axis descriptor, descriptors for additional axes, and array of data series.
- [- initWithAttributedTitle:summary:xAxisDescriptor:yAxisDescriptor:series:](./initwithattributedtitle_summary_xaxisdescriptor_yaxisdescriptor_series_.md)
  Creates a chart descriptor with the specified attributed title, summary, x-axis descriptor, y-axis descriptor, and array of data series.
- [- initWithTitle:summary:xAxisDescriptor:yAxisDescriptor:additionalAxes:series:](./initwithtitle_summary_xaxisdescriptor_yaxisdescriptor_additionalaxes_series_.md)
  Creates a chart descriptor with the specified title, summary, x-axis descriptor, y-axis descriptor, descriptors for additional axes, and array of data series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axchartdescriptor/initwithattributedtitle:summary:xaxisdescriptor:yaxisdescriptor:additionalaxes:series:)*