# perShareMetadataBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute as the operation fetches individual shares.

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
var perShareMetadataBlock: ((URL, CKShare.Metadata?, (any Error)?) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameters:

- The share’s URL.
- The share metadata, or `nil` if CloudKit can’t fetch the metadata.
- If CloudKit can’t fetch the share metadata, this parameter provides information about the failure; otherwise, it’s `nil`.

The operation executes this closure once for each URL in the [`shareURLs`](ckfetchsharemetadataoperation/shareurls.md) property. Each time the closure executes, it executes serially with respect to the other closures of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.

## See Also

- [var fetchShareMetadataCompletionBlock: (((any Error)?) -> Void)?](ckfetchsharemetadataoperation/fetchsharemetadatacompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/persharemetadatablock)*