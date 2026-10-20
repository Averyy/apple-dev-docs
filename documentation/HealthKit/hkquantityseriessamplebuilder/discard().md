# discard()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) discard;
```

## See Also

### Ending the Collection
- [func finishSeries(metadata: [String : Any]?, completion: ([HKQuantitySample]?, (any Error)?) -> Void)](./finishseries%28metadata,completion%29.md)
  Finalizes the series and returns the resulting quantity samples.
- [func finishSeries(metadata: [String : Any]?, endDate: Date?, completion: ([HKQuantitySample]?, (any Error)?) -> Void)](./finishseries%28metadata,enddate,completion%29.md)
  Finalizes the series with the provided end date, and returns the resulting quantity samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplebuilder/discard())*