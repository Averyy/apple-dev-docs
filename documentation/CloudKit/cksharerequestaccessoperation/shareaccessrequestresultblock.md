# shareAccessRequestResultBlock

**Framework**: CloudKit  
**Kind**: property

This block is called when the operation completes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var shareAccessRequestResultBlock: ((Result<Void, any Error>) -> Void)? { get set }
```

#### Discussion

The top-level error will never be `CKError.partialFailure`.  Instead, per-item errors are surfaced in prior invocations of `perShareResultBlock`.

The `Operation.completionBlock` will also be called if both are set.

Each [`CKOperation`](ckoperation.md) instance has a private serial queue. This queue is used for all callback block invocations. This block may share mutable state with other blocks assigned to this operation, but any such mutable state should not be concurrently used outside of blocks assigned to this operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation/shareaccessrequestresultblock)*