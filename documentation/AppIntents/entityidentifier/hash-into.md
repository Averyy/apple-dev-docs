# hash(into:)

**Framework**: App Intents  
**Kind**: method

Hashes the entity identifier.

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
func hash(into hasher: inout Hasher)
```

#### Discussion

> ❗ **Important**: This implementation **intentionally ignores** the `stableIdentifier` field. Only `typeIdentifier` and `identifier` are used for hashing. This ensures that the same entity on different devices (same local ID, different stable ID) has the same hash, enabling correct behavior in `Set` and `Dictionary`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityidentifier/hash(into:))*