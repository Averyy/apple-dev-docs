# perShareAccessRequestResultBlock

**Framework**: CloudKit  
**Kind**: property

A block called once for each share URL processed by the server.

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
var perShareAccessRequestResultBlock: ((URL, Result<Void, any Error>) -> Void)? { get set }
```

#### Discussion

Use this block to handle results individually for each requested share.

Each [`CKOperation`](ckoperation.md) instance uses a private serial queue for callback block invocations. This queue ensures serialized execution and thread safety for mutable state shared within the operation’s blocks. Any mutable state should not be concurrently accessed outside these callback blocks.

## Parameters

- `shareURL`: The URL of the processed share.
- `result`: A result indicating success ( ) or an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation/pershareaccessrequestresultblock)*