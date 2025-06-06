# discard()

**Framework**: HealthKit  
**Kind**: method

Discards all previously collected data and invalidates the builder.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
func discard()
```

## See Also

- [func finishSeries(metadata: [String : Any]?, completion: ([HKQuantitySample]?, (any Error)?) -> Void)](hkquantityseriessamplebuilder/finishseries(metadata:completion:).md)
  Finalizes the series and returns the resulting quantity samples.
- [func finishSeries(metadata: [String : Any]?, endDate: Date?, completion: ([HKQuantitySample]?, (any Error)?) -> Void)](hkquantityseriessamplebuilder/finishseries(metadata:enddate:completion:).md)
  Finalizes the series with the provided end date, and returns the resulting quantity samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplebuilder/discard())*