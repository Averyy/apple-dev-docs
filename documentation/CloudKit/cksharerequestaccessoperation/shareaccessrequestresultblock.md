# shareAccessRequestResultBlock

**Framework**: CloudKit  
**Kind**: property

A block called when the entire share access request operation completes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var shareAccessRequestResultBlock: ((Result<Void, any Error>) -> Void)? { get set }
```

#### Discussion

Use this block to handle the overall success or failure of the operation.

The top-level error returned here will never be `CKError.partialFailure`. Individual share errors are reported through the [`perShareAccessRequestResultBlock`](cksharerequestaccessoperation/pershareaccessrequestresultblock.md).

If the completionBlock is set on the [`CKOperation`](ckoperation.md), it will also be called after this block.

Each [`CKOperation`](ckoperation.md) instance uses a private serial queue for callback block invocations. This queue ensures serialized execution and thread safety for mutable state shared within the operation’s blocks. Any mutable state should not be concurrently accessed outside these callback blocks.

## Parameters

- `result`: A result indicating success ( ) or an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation/shareaccessrequestresultblock)*