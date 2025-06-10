# perShareAccessRequestResultBlock

**Framework**: CloudKit  
**Kind**: property

Called once for each share URL that the server processed

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
var perShareAccessRequestResultBlock: ((URL, Result<Void, any Error>) -> Void)? { get set }
```

#### Discussion

Each [`CKOperation`](ckoperation.md) instance has a private serial queue. This queue is used for all callback block invocations. This block may share mutable state with other blocks assigned to this operation, but any such mutable state should not be concurrently used outside of blocks assigned to this operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation/pershareaccessrequestresultblock)*