# entities

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

The entities to delete.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
var entities: [Self.Entity] { get }
```

Available when `Entity` is `Self.Target.ValueType`.

## Discussion

When [`target`](./target-1cesv.md) is an [`EntityCollection`](../entitycollection.md), this default implementation returns an empty array. Read the identifiers from `target`, or call [`resolvedEntities()`](../entitycollection/resolvedentities%28%29.md) to fetch the entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/deleteintent/entities-9b809)*