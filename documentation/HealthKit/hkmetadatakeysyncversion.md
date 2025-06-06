# HKMetadataKeySyncVersion

**Framework**: HealthKit  
**Kind**: var

The version number for a piece of data, used when updating or syncing.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let HKMetadataKeySyncVersion: String
```

#### Discussion

This key takes an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) as its value. When you save an object to the HealthKit store, the new object replaces any matching objects (existing objects with a matching [`HKMetadataKeySyncIdentifier`](hkmetadatakeysyncidentifier.md) value) with a lower sync version.

For more information, see [`HKMetadataKeySyncIdentifier`](hkmetadatakeysyncidentifier.md).

## See Also

- [let HKMetadataKeySyncIdentifier: String](hkmetadatakeysyncidentifier.md)
  A unique string that identifies a piece of data so it can be updated and synced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeysyncversion)*