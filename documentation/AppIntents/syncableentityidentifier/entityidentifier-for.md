# entityIdentifier(for:)

**Framework**: App Intents  
**Kind**: method

Creates an identifier from a string representation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static func entityIdentifier(for string: String) -> SyncableEntityIdentifier<LocalID, StableID>?
```

#### Return Value

An identifier with local ID set, or `nil` if parsing fails

#### Discussion

Attempts to parse the string as a local ID. The stable ID is not populated during deserialization - it should be populated by queries when fetching entities.

## Parameters

- `string`: The string representation


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/entityidentifier(for:))*