# duration

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 17.0+ - Deprecated in 27.2
- iPadOS 17.0+ - Deprecated in 27.2
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`interval`](../signpostrecord/interval.md) instead.

## Declaration

```swift
var duration: Measurement<UnitDuration>? { get }
```

```objc
@property (copy, readonly, nullable) NSMeasurement<NSUnitDuration *> * duration;
```

## See Also

### Reading the data
- [var beginTimeStamp: Date](./begintimestamp.md)
- [var category: String](./category.md)
- [var endTimeStamp: Date?](./endtimestamp.md)
- [var isInterval: Bool](./isinterval.md)
- [var name: String](./name.md)
- [var subsystem: String](./subsystem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxsignpostrecord/duration)*