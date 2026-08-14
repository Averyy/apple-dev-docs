# AIModelCache.Policy

**Framework**: Core AI  
**Kind**: struct

A policy that controls when the system purges specialized assets from a cache.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Policy
```

## Mentions

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)

#### Overview

Defines the conditions under which the system may purge specialized assets in an [`AIModelCache`](aimodelcache.md).

> **Note**: Regardless of policy, the system always purges assets when the OS updates, as specialized assets are OS-version specific.

## Topics

### Using preset policies
- [static let `default`: AIModelCache.Policy](aimodelcache/policy/default.md)
  A policy that marks specialized assets as purgeable.
- [static let persistent: AIModelCache.Policy](aimodelcache/policy/persistent.md)
  A policy that prevents automatic purging of specialized assets.
### Creating a custom policy
- [init(purgeConditions: AIModelCache.Policy.PurgeConditions)](aimodelcache/policy/init(purgeconditions:).md)
  Creates a policy with the specified purge conditions.
### Inspecting a policy
- [var purgeConditions: AIModelCache.Policy.PurgeConditions](aimodelcache/policy/purgeconditions-swift.property.md)
  The conditions under which the system may purge specialized assets.
### Describing purge conditions
- [AIModelCache.Policy.PurgeConditions](aimodelcache/policy/purgeconditions-swift.struct.md)
  A set of conditions that determine when the system purges specialized assets.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/policy)*