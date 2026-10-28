# perShareMetadataBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute as the operation fetches individual shares.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.12+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 8.0

> **Deprecated**: Use perShareMetadataResultBlock instead

## Declaration

```swift
var perShareMetadataBlock: ((URL, CKShare.Metadata?, (any Error)?) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^perShareMetadataBlock)(NSURL *shareURL, CKShareMetadata *shareMetadata, NSError *error);
```

## Discussion

The closure returns no value and takes the following parameters:

- The share’s URL.
- The share metadata, or `nil` if CloudKit can’t fetch the metadata.
- If CloudKit can’t fetch the share metadata, this parameter provides information about the failure; otherwise, it’s `nil`.

The operation executes this closure once for each URL in the [`shareURLs`](./shareurls.md) property. Each time the closure executes, it executes serially with respect to the other closures of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.

## See Also

### Processing the Operation’s Results
- [var fetchShareMetadataCompletionBlock: (((any Error)?) -> Void)?](./fetchsharemetadatacompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/persharemetadatablock)*