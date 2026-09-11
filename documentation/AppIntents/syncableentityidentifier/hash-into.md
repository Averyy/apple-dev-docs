# hash(into:)

**Framework**: App Intents  
**Kind**: method

Hashes based on the local ID if present, otherwise the stable ID.

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
func hash(into hasher: inout Hasher)
```

#### Discussion

This ensures consistent hashing with equality - identifiers that are equal will produce the same hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/hash(into:))*