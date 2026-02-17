# shareMetadatas(for:)

**Framework**: CloudKit  
**Kind**: method

Fetches share metadatas for the specified share URLs and returns them to an awaiting caller.

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
func shareMetadatas(for urls: [URL]) async throws -> [URL : Result<CKShare.Metadata, any Error>]
```

#### Return Value

A dictionary of fetched share metadatas. The dictionary uses the URLs you specify in `urls` as its keys. The value of each key is a [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either the corresponding fetched share metadata, or an error that describes why CloudKit can’t fetch that share metadata.

#### Discussion

This method searches for share metadatas asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKFetchShareMetadataOperation`](ckfetchsharemetadataoperation.md) and configure it to use the necessary priority.

## Parameters

- `urls`: The share URLs that CloudKit uses to locate the metadatas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/sharemetadatas(for:))*