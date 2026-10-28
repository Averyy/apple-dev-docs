# xValue

**Framework**: Accessibility  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy) AXDataPointValue * xValue;
```

## Discussion

Use a `double` value for a numeric x-axis, or an [`NSString`](../../Foundation/nsstring.md) value for a categorical x-axis.

## See Also

### Specifying the data value
- [var yValue: AXDataPointValue?](./yvalue.md)
  The value of the y-axis for the data point.
- [class AXDataPointValue](../axdatapointvalue.md)
  A single data value.
- [AXDataPoint.Value](./value.md)
  Constants that describe types of data values.
- [additionalValues](./additionalvalues.md)
  An array of values for additional axes for the data point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdatapoint/xvalue)*