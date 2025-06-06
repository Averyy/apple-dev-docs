# acceptSharesCompletionBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when the operation finishes.

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
var acceptSharesCompletionBlock: (((any Error)?) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameter:

- An error that contains information about a problem, or `nil` if CloudKit successfully processes the shares.

The operation executes this closure only once. The closure executes on a background queue, so any tasks that require access to the main queue must dispatch accordingly.

The closure reports an error of type [`CKError.Code.partialFailure`](ckerror/code/partialfailure.md) when it can’t process some of the shares. The `userInfo` dictionary of the error contains a [`CKPartialErrorsByItemIDKey`](ckpartialerrorsbyitemidkey.md) key that has a dictionary as its value. The keys of the dictionary are share URLs that CloudKit can’t process, and the corresponding values are errors that contain information about the failures.

Set this property’s value before you execute the operation or submit it to a queue.

## See Also

- [var shareMetadatas: [CKShare.Metadata]?](ckacceptsharesoperation/sharemetadatas.md)
  The share metadatas to process.
- [var perShareCompletionBlock: ((CKShare.Metadata, CKShare?, (any Error)?) -> Void)?](ckacceptsharesoperation/persharecompletionblock.md)
  The block to execute as CloudKit processes individual shares.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/acceptsharescompletionblock)*