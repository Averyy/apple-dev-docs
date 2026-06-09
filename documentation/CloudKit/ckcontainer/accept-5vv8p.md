# accept(_:)

**Framework**: CloudKit  
**Kind**: method

Accepts the specified share metadata and returns the accepted share to an awaiting caller.

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
func accept(_ metadata: CKShare.Metadata) async throws -> CKShare
```

#### Return Value

The corresponding share for the share metadata.

## Parameters

- `metadata`: The metadata of the share to accept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/accept(_:)-5vv8p)*