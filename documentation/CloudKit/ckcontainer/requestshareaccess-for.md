# requestShareAccess(for:)

**Framework**: CloudKit  
**Kind**: method

Requests access to the specified share URLs, and returns the results to an awaiting caller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 15.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func requestShareAccess(for urls: [URL]) async throws -> [URL : Result<Void, any Error>]
```

#### Return Value

A dictionary of acceptance results. The dictionary uses the urls you specify in `urls` as its keys. The value of each key is a [`Result`](https://developer.apple.com/documentation/swift/result): `.success(())` when CloudKit grants access to that share, or an error that describes why CloudKit can’t request access to that share.

#### Discussion

This method requests access to shares asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKShareRequestAccessOperation`](cksharerequestaccessoperation.md) and configure it to use the necessary priority.

## Parameters

- `urls`: The share URLs that CloudKit uses to locate the shares.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/requestshareaccess(for:))*