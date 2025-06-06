# minimum

**Framework**: HealthKit  
**Kind**: property

The maximum walking steadiness percentage for the classification.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
var minimum: HKQuantity { get }
```

#### Discussion

This property contains the maximum walking steadiness value for the classification. It contains an [`HKQuantity`](hkquantity.md) instance with a percentage value between `0.0` and `1.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkapplewalkingsteadinessclassification/minimum)*