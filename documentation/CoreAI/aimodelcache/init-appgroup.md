# init(appGroup:)

**Framework**: Core AI  
**Kind**: init

Creates a cache that shares specialized assets across an app group.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init?(appGroup groupIdentifier: String)
```

## Mentions

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)

#### Return Value

The shared app group cache, or `nil` when the group identifier is invalid (on iOS), the app group container cannot be accessed, or entitlement checks fail.

#### Discussion

Use this initializer when multiple apps within an app group need to share a cache for their specialized assets. This allows all apps within an app group to avoid each performing their own specialization for a shared model.

## Parameters

- `groupIdentifier`: A string that names the group whose shared cache you want to obtain. This input should exactly match one of the strings in the app’s App Groups Entitlement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/init(appgroup:))*