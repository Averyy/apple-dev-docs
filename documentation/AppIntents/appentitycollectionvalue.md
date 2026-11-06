# AppEntityCollectionValue

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

An intent value that holds multiple app entities of the same type.

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
protocol AppEntityCollectionValue : _IntentValue
```

## Overview

Arrays and sets of entities, and [`EntityCollection`](./entitycollection.md), conform to this protocol. Use it to accept any of them, such as for the [`target`](./deleteintent/target-1cesv.md) of a delete intent.

## Relationships

### Conforming Types
- [EntityCollection](./entitycollection.md)

## See Also

### Entity collections
- [struct EntityCollection](./entitycollection.md)
  An array of entity identifiers that you use to improve the efficiency of operations involving large numbers of entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentitycollectionvalue)*