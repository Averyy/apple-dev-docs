# storagePressure

**Framework**: Core AI  
**Kind**: property

A condition that allows purging under device storage pressure.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static let storagePressure: AIModelCache.Policy.PurgeConditions
```

#### Discussion

This option allows the system to delete a specialized asset when the device runs low on storage and needs to reclaim space.

## See Also

- [static let sourceAssetChangedOrDeleted: AIModelCache.Policy.PurgeConditions](aimodelcache/policy/purgeconditions-swift.struct/sourceassetchangedordeleted.md)
  A condition that allows purging when the source model changes or no longer exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/policy/purgeconditions-swift.struct/storagepressure)*