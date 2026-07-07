# maximum

**Framework**: HealthKit  
**Kind**: property

The maximum threshold for the zone.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var maximum: HKQuantity? { get }
```

#### Discussion

If `nil`, the zone has no upper bound.

## See Also

- [let index: Int](hkworkoutzone/index.md)
  The zero-based index of the zone within the containing zone configuration, ordered from lowest to highest threshold.
- [var minimum: HKQuantity?](hkworkoutzone/minimum.md)
  The minimum threshold for the zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzone/maximum)*