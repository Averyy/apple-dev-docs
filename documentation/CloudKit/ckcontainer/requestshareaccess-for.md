# requestShareAccess(for:)

**Framework**: CloudKit  
**Kind**: method

Requests share access for the specified URLs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func requestShareAccess(for urls: [URL]) async throws -> [URL : Result<Void, any Error>]
```

#### Discussion

[`CKShareRequestAccessOperation`](cksharerequestaccessoperation.md) is the more configurable, [`CKOperation`](ckoperation.md)-based alternative to this function


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/requestshareaccess(for:))*