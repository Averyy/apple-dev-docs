# accept(_:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

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
@preconcurrency
func accept(_ metadatas: [CKShare.Metadata], completionHandler: @escaping (Result<[CKShare.Metadata : Result<CKShare, any Error>], any Error>) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/accept(_:completionhandler:)-7s3t7)*