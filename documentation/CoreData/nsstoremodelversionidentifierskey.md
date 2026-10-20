# NSStoreModelVersionIdentifiersKey

**Framework**: Core Data  
**Kind**: var  
**Role**: Global Variable

Key to represent the version identifiers for the model used to create the store.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let NSStoreModelVersionIdentifiersKey: String
```

```c
extern NSString * const NSStoreModelVersionIdentifiersKey;
```

#### Discussion

If you add your own annotations to a model’s version identifier (see [`versionIdentifiers`](./nsmanagedobjectmodel/versionidentifiers.md)), they are stored in the persistent store’s metadata. You can use this key to retrieve the identifiers from the metadata dictionaries available from `NSPersistentStore` ([`metadata`](./nspersistentstore/metadata.md)) and `NSPersistentStoreCoordinator` ([`metadata(for:)`](./nspersistentstorecoordinator/metadata%28for%29.md) and related methods). The corresponding value is a Foundation collection (an `NSArray` or `NSSet` object).

## See Also

### Constants
- [let NSStoreModelVersionHashesKey: String](./nsstoremodelversionhasheskey.md)
  Key to represent the version hash information for the model used to create the store.
- [let NSPersistentStoreOSCompatibility: String](./nspersistentstoreoscompatibility.md)
  Key to represent the earliest version of the operation system that the persistent store supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsstoremodelversionidentifierskey)*