# scaleType

**Framework**: Accessibility  
**Kind**: property  
**Role**: Instance Property

The scale for the axis.

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
var scaleType: AXNumericDataAxisDescriptor.ScaleType { get set }
```

```objc
@property (nonatomic, assign) AXNumericDataAxisDescriptorScale scaleType;
```

## Discussion

Match the value of this property to the visual representation in the chart.

The default value is [`AXNumericDataAxisDescriptor.ScaleType.linear`](./scaletype-swift.enum/linear.md).

## See Also

### Configuring the axis scale
- [AXNumericDataAxisDescriptor.ScaleType](./scaletype-swift.enum.md)
  Constants that describe the scale of a numeric axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axnumericdataaxisdescriptor/scaletype-swift.property)*