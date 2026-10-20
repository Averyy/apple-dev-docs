# diameter

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

Part of the contact’s fit, it measures the diameter of the lens, measured in mm.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@NSCopying
var diameter: HKQuantity? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) HKQuantity * diameter;
```

#### Discussion

The property’s range is 9 to 15 mm.

## See Also

### Accessing the specification’s data
- [var baseCurve: HKQuantity?](./basecurve.md)
  Part of the contact’s fit, it measures the curve of the back side of the contact, measured in mm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcontactslensspecification/diameter)*