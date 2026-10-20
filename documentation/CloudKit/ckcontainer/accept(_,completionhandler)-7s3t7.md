# accept(_:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Accepts the specified share metadatas.

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
func accept(_ metadatas: [CKShare.Metadata], completionHandler: @escaping @Sendable (Result<[CKShare.Metadata : Result<CKShare, any Error>], any Error>) -> Void)
```

#### Discussion

The closure doesn’t return a value and takes the following parameters:

- A dictionary of fetched shares. The dictionary uses the metadatas you specify in `metadatas` as its keys. The value of each key is a [`Result`](https://developer.apple.com/documentation/swift/result) that contains either the corresponding fetched share, or an error that describes why CloudKit can’t fetch that share.

This method accepts shares asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKAcceptSharesOperation`](ckacceptsharesoperation.md) and configure it to use the necessary priority.

## Parameters

- `metadatas`: The metadatas of the shares to accept.
- `completionHandler`: The handler to execute when the process finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/accept(_:completionhandler:)-7s3t7)*