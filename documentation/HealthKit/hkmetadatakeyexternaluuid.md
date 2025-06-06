# HKMetadataKeyExternalUUID

**Framework**: HealthKit  
**Kind**: var

A unique identifier for an HKObject that is set by its source.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HKMetadataKeyExternalUUID: String
```

#### Discussion

This key takes a string value. This value is independent of the UUID assigned to the object by the HealthKit store. You can assign your own UUID to any HealthKit objects you create. Use these IDs to uniquely identify objects in your application. You typically use the UUID from the corresponding data entry on your server. This lets you create multiple copies of that data across multiple devices. Each copy shares the same external UUID.

## See Also

- [let HKMetadataKeyTimeZone: String](hkmetadatakeytimezone.md)
  The user’s time zone when the HealthKit object was created.
- [let HKMetadataKeyWasUserEntered: String](hkmetadatakeywasuserentered.md)
  A key that indicates whether the sample was entered by the user.
- [let HKMetadataKeyQuantityClampedToLowerBound: String](hkmetadatakeyquantityclampedtolowerbound.md)
- [let HKMetadataKeyQuantityClampedToUpperBound: String](hkmetadatakeyquantityclampedtoupperbound.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyexternaluuid)*