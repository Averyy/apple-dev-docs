# fetchAllChanges

**Framework**: CloudKit  
**Kind**: property

A Boolean value that indicates whether to send repeated requests to the server.

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
var fetchAllChanges: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the operation sends repeat requests to the server until it fetches all changes. CloudKit executes the handler you set on the [`changeTokenUpdatedBlock`](ckfetchdatabasechangesoperation/changetokenupdatedblock.md) property with a change token after each request.

The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var previousServerChangeToken: CKServerChangeToken?](ckfetchdatabasechangesoperation/previousserverchangetoken.md)
  The server change token.
- [var resultsLimit: Int](ckfetchdatabasechangesoperation/resultslimit.md)
  The maximum number of results that the operation fetches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/fetchallchanges)*