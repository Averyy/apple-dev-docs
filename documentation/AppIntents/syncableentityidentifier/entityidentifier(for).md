# entityIdentifier(for:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Type Method

Creates an identifier from a string representation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func entityIdentifier(for string: String) -> SyncableEntityIdentifier<LocalID, StableID>?
```

Available when `LocalID` conforms to `EntityIdentifierConvertible`, `LocalID` conforms to `Sendable`, `StableID` conforms to `EntityIdentifierConvertible`, and `StableID` conforms to `Sendable`.

## Return Value

An identifier with local ID set, or `nil` if parsing fails

## Discussion

Attempts to parse the string as a local ID. The stable ID is not populated during deserialization - it should be populated by queries when fetching entities.

## Parameters

- `string`: The string representation


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/entityidentifier(for:))*