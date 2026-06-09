# sourceAssetChangedOrDeleted

**Framework**: Core AI  
**Kind**: property

A condition that allows purging when the source model changes or no longer exists.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let sourceAssetChangedOrDeleted: AIModelCache.Policy.PurgeConditions
```

#### Discussion

This option allows the system to delete a specialized asset when the `.aimodel` the asset derives from changes or no longer exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/policy/purgeconditions-swift.struct/sourceassetchangedordeleted)*