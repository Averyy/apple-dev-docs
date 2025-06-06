# fetchShareMetadata(with:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches the share metadata for the specified share URL.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func shareMetadata(for url: URL) async throws -> CKShare.Metadata
```

#### Discussion

The closure doesn’t return a value and takes the following parameters:

- The share metadata, or `nil` if CloudKit can’t find the metadata.
- An error if a problem occurs, or `nil` if CloudKit successfully retrieves the metadata.

## Parameters

- `url`: The share URL that CloudKit uses to locate the metadata.
- `completionHandler`: The handler to execute with the fetch results.

## See Also

- [func accept(CKShare.Metadata, completionHandler: (CKShare?, (any Error)?) -> Void)](ckcontainer/accept(_:completionhandler:)-949ea.md)
  Accepts the specified share metadata.
- [static let CKAccountChanged: NSNotification.Name](../foundation/nsnotification/name/1399172-ckaccountchanged.md)
  A notification that a container posts when the status of an iCloud account changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/fetchsharemetadata(with:completionhandler:))*