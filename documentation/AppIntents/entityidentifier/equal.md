# ==(_:_:)

**Framework**: App Intents  
**Kind**: op

Compares two entity identifiers for equality.

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
static func == (lhs: EntityIdentifier, rhs: EntityIdentifier) -> Bool
```

#### Discussion

> ❗ **Important**: This implementation **intentionally ignores** the `stableIdentifier` field. Only `entityType` and `identifier` are compared. This ensures that the same entity on different devices (same local ID, different stable ID) is considered equal, enabling correct Dictionary/Set behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityidentifier/==(_:_:))*