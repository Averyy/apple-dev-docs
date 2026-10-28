# unitsPerSecond

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A conversion factor from seconds to your app’s preferred unit of time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var unitsPerSecond: Double { get set }
```

```objc
@property (nonatomic, assign) double unitsPerSecond;
```

## Discussion

Time-based properties throughout the framework apply the value you supply for this property to their value.

## See Also

### Measuring Units
- [var unitsPerMeter: Double](./unitspermeter.md)
  A conversion factor from meters to your app’s preferred unit of measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/unitspersecond)*