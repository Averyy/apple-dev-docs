# shareMetadatas

**Framework**: CloudKit  
**Kind**: property

The share metadatas to process.

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
var shareMetadatas: [CKShare.Metadata]? { get set }
```

#### Discussion

Use this property to view or change the metadata of the shares you want to process. If you intend to specify or change the value of this property, do so before you execute the operation or submit it to a queue.

## See Also

- [var perShareCompletionBlock: ((CKShare.Metadata, CKShare?, (any Error)?) -> Void)?](ckacceptsharesoperation/persharecompletionblock.md)
  The block to execute as CloudKit processes individual shares.
- [var acceptSharesCompletionBlock: (((any Error)?) -> Void)?](ckacceptsharesoperation/acceptsharescompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckacceptsharesoperation/sharemetadatas)*