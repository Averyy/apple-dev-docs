# NSPersistentStoreOSCompatibility

**Framework**: Core Data  
**Kind**: var

Key to represent the earliest version of the operation system that the persistent store supports.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSPersistentStoreOSCompatibility: String
```

#### Discussion

The corresponding value is an `NSNumber` object that takes the form of the constants defined by the availability macros defined in `/usr/include/AvailabilityMacros.h`; for example `1040` represents OS X version 10.4.0.

Backward compatibility may preclude some features.

## See Also

- [let NSStoreModelVersionHashesKey: String](nsstoremodelversionhasheskey.md)
  Key to represent the version hash information for the model used to create the store.
- [let NSStoreModelVersionIdentifiersKey: String](nsstoremodelversionidentifierskey.md)
  Key to represent the version identifiers for the model used to create the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoreoscompatibility)*