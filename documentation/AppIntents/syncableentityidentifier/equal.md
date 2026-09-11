# ==(_:_:)

**Framework**: App Intents  
**Kind**: op

Two identifiers are equal when they have the same shape **and** the same values: both-local compares local IDs (ignoring stable), both-stable-only compares stable IDs.  Mixed shapes (one has local, the other doesn’t) are never equal — this keeps the Hashable contract intact since each shape hashes a different component.

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
static func == (lhs: SyncableEntityIdentifier<LocalID, StableID>, rhs: SyncableEntityIdentifier<LocalID, StableID>) -> Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/==(_:_:))*