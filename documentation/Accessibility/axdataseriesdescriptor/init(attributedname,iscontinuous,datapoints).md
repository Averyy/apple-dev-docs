# init(attributedName:isContinuous:dataPoints:)

**Framework**: Accessibility  
**Kind**: init  
**Role**: Initializer

Creates a data series with the specified attributed name, a Boolean value that indicates whether the series is continuous, and data points.

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
init(attributedName: NSAttributedString, isContinuous: Bool, dataPoints: [AXDataPoint])
```

```objc
- (instancetype) initWithAttributedName:(NSAttributedString *) attributedName isContinuous:(BOOL) isContinuous dataPoints:(NSArray<AXDataPoint *> *) dataPoints;
```

## See Also

### Creating a data series
- [init(name: String, isContinuous: Bool, dataPoints: [AXDataPoint])](./init%28name,iscontinuous,datapoints%29.md)
  Creates a data series with the specified name, a Boolean value that indicates whether the series is continuous, and data points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axdataseriesdescriptor/init(attributedname:iscontinuous:datapoints:))*