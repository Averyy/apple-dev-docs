# AIModelCache.Policy.PurgeConditions

**Framework**: Core AI  
**Kind**: struct

A set of conditions that determine when the system purges specialized assets.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct PurgeConditions
```

#### Overview

> **Note**: The system always purges assets on OS update regardless of these conditions.

## Topics

### Identifying purge conditions
- [static let sourceAssetChangedOrDeleted: AIModelCache.Policy.PurgeConditions](aimodelcache/policy/purgeconditions-swift.struct/sourceassetchangedordeleted.md)
  A condition that allows purging when the source model changes or no longer exists.
- [static let storagePressure: AIModelCache.Policy.PurgeConditions](aimodelcache/policy/purgeconditions-swift.struct/storagepressure.md)
  A condition that allows purging under device storage pressure.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/policy/purgeconditions-swift.struct)*