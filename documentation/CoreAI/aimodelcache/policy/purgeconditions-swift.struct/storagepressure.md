# storagePressure

**Framework**: Core AI  
**Kind**: property  
**Role**: Type Property

A condition that allows purging under device storage pressure.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static let storagePressure: AIModelCache.Policy.PurgeConditions
```

#### Discussion

This option allows the system to delete a specialized asset when the device runs low on storage and needs to reclaim space.

## See Also

### Identifying purge conditions
- [static let sourceAssetChangedOrDeleted: AIModelCache.Policy.PurgeConditions](./sourceassetchangedordeleted.md)
  A condition that allows purging when the source model changes or no longer exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/policy/purgeconditions-swift.struct/storagepressure)*