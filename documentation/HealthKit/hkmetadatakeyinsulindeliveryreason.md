# HKMetadataKeyInsulinDeliveryReason

**Framework**: HealthKit  
**Kind**: var

The medical reason for administering insulin.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let HKMetadataKeyInsulinDeliveryReason: String
```

#### Discussion

This key is required for [`insulinDelivery`](hkquantitytypeidentifier/insulindelivery.md) samples. It takes an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a [`HKInsulinDeliveryReason`](hkinsulindeliveryreason.md) value.

## Topics

### Valid Delivery Reasons
- [enum HKInsulinDeliveryReason](hkinsulindeliveryreason.md)
  Possible reasons for administering insulin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyinsulindeliveryreason)*