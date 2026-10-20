# timeSinceSampleStart

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The time of the measurement relative to the sample’s start time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var timeSinceSampleStart: TimeInterval { get }
```

```objc
@property (nonatomic, assign, readonly) NSTimeInterval timeSinceSampleStart;
```

## See Also

### Accessing Data
- [func quantity(for: HKElectrocardiogram.Lead) -> HKQuantity?](./quantity%28for%29.md)
  Returns the voltage for the specified lead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogram/voltagemeasurement/timesincesamplestart)*