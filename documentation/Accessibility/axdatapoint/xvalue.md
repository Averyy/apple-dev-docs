# xValue

**Framework**: Accessibility  
**Kind**: property

The value of the x-axis for the data point.

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
@NSCopying
var xValue: AXDataPointValue { get set }
```

#### Discussion

Use a `double` value for a numeric x-axis, or an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) value for a categorical x-axis.

## See Also

- [var yValue: AXDataPointValue?](axdatapoint/yvalue.md)
  The value of the y-axis for the data point.
- [class AXDataPointValue](axdatapointvalue.md)
  A single data value.
- [AXDataPoint.Value](axdatapoint/value.md)
  Constants that describe types of data values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdatapoint/xvalue)*