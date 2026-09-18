# persistent

**Framework**: Core AI  
**Kind**: property

A policy that prevents automatic purging of specialized assets.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static let persistent: AIModelCache.Policy
```

#### Discussion

This policy ensures the system does not purge specialized assets until the next OS update. You can manually delete them, but the system does *not* automatically purge them under low storage or when the source `.aimodel` changes.

> **Note**: On tvOS this setting is unavailable. Any policy must be purgeable for storagePressure.

## See Also

- [static let `default`: AIModelCache.Policy](aimodelcache/policy/default.md)
  A policy that marks specialized assets as purgeable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/policy/persistent)*