# entities(matching:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Retrieves instances by string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func entities(matching string: String) async throws -> Self.Result
```

## Mentions

- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)

## Parameters

- `string`: “Name” used to refer to an entity instance (or a set thereof).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitystringquery/entities(matching:))*