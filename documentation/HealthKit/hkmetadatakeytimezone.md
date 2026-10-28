# HKMetadataKeyTimeZone

**Framework**: HealthKit  
**Kind**: var  
**Role**: Global Variable

The user’s time zone when the HealthKit object was created.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HKMetadataKeyTimeZone: String
```

```c
extern NSString * const HKMetadataKeyTimeZone;
```

## Discussion

This key takes a string value compatible with the [`NSTimeZone`](../Foundation/nstimezone.md) class’s [`timeZoneWithName:`](../Foundation/nstimezone/timezonewithname_.md) method. For best results when analyzing sleep samples, it’s recommended that you store time zone metadata with your sleep sample data.

## See Also

### General Keys
- [let HKMetadataKeyExternalUUID: String](./hkmetadatakeyexternaluuid.md)
  A unique identifier for an HKObject that is set by its source.
- [let HKMetadataKeyWasUserEntered: String](./hkmetadatakeywasuserentered.md)
  A key that indicates whether the sample was entered by the user.
- [let HKMetadataKeyQuantityClampedToLowerBound: String](./hkmetadatakeyquantityclampedtolowerbound.md)
- [let HKMetadataKeyQuantityClampedToUpperBound: String](./hkmetadatakeyquantityclampedtoupperbound.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeytimezone)*