# additionalValues

**Framework**: Accessibility  
**Kind**: property  
**Role**: Instance Property

An array of values for additional axes for the data point.

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
@property (nonatomic, copy) NSArray<AXDataPointValue *> * additionalValues;
```

## Discussion

Provide these values in the same order as their corresponding [`AXDataAxisDescriptor`](../axdataaxisdescriptor.md) objects in [`additionalAxes`](../axchartdescriptor/additionalaxes-2adwh.md).

## See Also

### Specifying the data value
- [var xValue: AXDataPointValue](./xvalue.md)
  The value of the x-axis for the data point.
- [var yValue: AXDataPointValue?](./yvalue.md)
  The value of the y-axis for the data point.
- [class AXDataPointValue](../axdatapointvalue.md)
  A single data value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdatapoint/additionalvalues)*