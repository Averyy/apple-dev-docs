# default

**Framework**: Core AI  
**Kind**: property

A policy that marks specialized assets as purgeable.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let `default`: AIModelCache.Policy
```

#### Discussion

The default policy marks a specialized asset as purgeable. The system can delete it when low on storage or when its source `.aimodel` changes or you delete it.

## See Also

- [static let persistent: AIModelCache.Policy](aimodelcache/policy/persistent.md)
  A policy that prevents automatic purging of specialized assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/policy/default)*