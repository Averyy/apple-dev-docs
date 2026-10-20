# AIModelCache.Policy.PurgeConditions

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

A set of conditions that determine when the system purges specialized assets.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct PurgeConditions
```

#### Overview

> **Note**: The system always purges assets on OS update regardless of these conditions.

## Topics

### Identifying purge conditions
- [static let sourceAssetChangedOrDeleted: AIModelCache.Policy.PurgeConditions](./purgeconditions-swift.struct/sourceassetchangedordeleted.md)
  A condition that allows purging when the source model changes or no longer exists.
- [static let storagePressure: AIModelCache.Policy.PurgeConditions](./purgeconditions-swift.struct/storagepressure.md)
  A condition that allows purging under device storage pressure.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../../Swift/hashable.md)
- [OptionSet](../../../Swift/optionset.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)
- [SetAlgebra](../../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/policy/purgeconditions-swift.struct)*