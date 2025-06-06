# EntityStringQuery

**Framework**: App Intents  
**Kind**: protocol

An interface that locates entities using arbitrary string input.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol EntityStringQuery : EntityQuery
```

## Mentions

- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)

#### Overview

EntityStringQuery adds to a [`EntityQuery`](entityquery.md) the ability to query instances by `String`. The `String` value against which entities are matched typically represents the name a user would use to refer to a particular instance.

## Topics

### Searching for entities
- [func entities(matching: String) async throws -> Self.Result](entitystringquery/entities(matching:).md)
  Retrieves instances by string.

## Relationships

### Inherits From
- [DynamicOptionsProvider](dynamicoptionsprovider.md)
- [EntityQuery](entityquery.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitystringquery)*