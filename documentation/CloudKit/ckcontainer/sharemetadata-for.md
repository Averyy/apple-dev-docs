# shareMetadata(for:)

**Framework**: CloudKit  
**Kind**: method

Fetches the share metadata for the specified share URL.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func shareMetadata(for url: URL) async throws -> CKShare.Metadata
```

#### Discussion

- Returns The share metadata for the share URL.

## Parameters

- `url`: The share URL that CloudKit uses to locate the metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/sharemetadata(for:))*