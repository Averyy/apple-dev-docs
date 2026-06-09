# ==(_:_:)

**Framework**: App Intents  
**Kind**: op

Two identifiers are equal when they have the same shape **and** the same values: both-local compares local IDs (ignoring stable), both-stable-only compares stable IDs.  Mixed shapes (one has local, the other doesn’t) are never equal — this keeps the Hashable contract intact since each shape hashes a different component.

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
static func == (lhs: SyncableEntityIdentifier<LocalID, StableID>, rhs: SyncableEntityIdentifier<LocalID, StableID>) -> Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/==(_:_:))*