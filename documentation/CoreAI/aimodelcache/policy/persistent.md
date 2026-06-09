# persistent

**Framework**: Core AI  
**Kind**: property

A policy that prevents automatic purging of specialized assets.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let persistent: AIModelCache.Policy
```

#### Discussion

This policy ensures the system does not purge specialized assets until the next OS update. You can manually delete them, but the system does *not* automatically purge them under low storage or when the source `.aimodel` changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/policy/persistent)*