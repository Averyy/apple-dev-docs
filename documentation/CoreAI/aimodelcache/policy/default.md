# default

**Framework**: Core AI  
**Kind**: property

A policy that marks specialized assets as purgeable.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let `default`: AIModelCache.Policy
```

#### Discussion

The default policy marks a specialized asset as purgeable. The system can delete it when low on storage or when its source `.aimodel` changes or you delete it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/policy/default)*