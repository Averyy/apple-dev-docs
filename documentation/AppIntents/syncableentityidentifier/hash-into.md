# hash(into:)

**Framework**: App Intents  
**Kind**: method

Hashes based on the local ID if present, otherwise the stable ID.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

#### Discussion

This ensures consistent hashing with equality - identifiers that are equal will produce the same hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/hash(into:))*