# fetchShareMetadatas(for:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches share metadatas for the specified share URLs.

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
func fetchShareMetadatas(for urls: [URL], completionHandler: @escaping @Sendable (Result<[URL : Result<CKShare.Metadata, any Error>], any Error>) -> Void)
```

#### Discussion

The closure doesn’t return a value and takes the following parameters:

- A dictionary of fetched share metadatas. The dictionary uses the URLs you specify in `urls` as its keys. The value of each key is a [`Result`](https://developer.apple.com/documentation/swift/result) that contains either the corresponding fetched share metadata, or an error that describes why CloudKit can’t fetch that share metadata.

This method searches for share metadatas asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKFetchShareMetadataOperation`](ckfetchsharemetadataoperation.md) and configure it to use the necessary priority.

## Parameters

- `urls`: The share URLs that CloudKit uses to locate the metadatas.
- `completionHandler`: The handler to execute with the fetch results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/fetchsharemetadatas(for:completionhandler:))*