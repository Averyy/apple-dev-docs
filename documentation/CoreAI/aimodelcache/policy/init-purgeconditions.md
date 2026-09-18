# init(purgeConditions:)

**Framework**: Core AI  
**Kind**: init

Creates a policy with the specified purge conditions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(purgeConditions: AIModelCache.Policy.PurgeConditions)
```

#### Discussion

> **Note**: On tvOS any policy will be implicitly purgeable for storagePressure.

## Parameters

- `purgeConditions`: The set of conditions under which the system can purge specialized assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/policy/init(purgeconditions:))*