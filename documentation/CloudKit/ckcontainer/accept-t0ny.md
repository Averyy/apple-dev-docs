# accept(_:)

**Framework**: CloudKit  
**Kind**: method

Accepts the specified share metadatas and returns the accepted shares to an awaiting caller.

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
func accept(_ metadatas: [CKShare.Metadata]) async throws -> [CKShare.Metadata : Result<CKShare, any Error>]
```

#### Return Value

A dictionary of accepted shares. The dictionary uses the share metadatas you specify in `metadatas` as its keys. The value of each key is a [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either the corresponding accepted share, or an error that describes why CloudKit can’t accept that share.

#### Discussion

This method accepts shares asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKAcceptSharesOperation`](ckacceptsharesoperation.md) and configure it to use the necessary priority.

## Parameters

- `metadatas`: The share metadatas of the shares to accept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/accept(_:)-t0ny)*