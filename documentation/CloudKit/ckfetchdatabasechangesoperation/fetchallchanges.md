# fetchAllChanges

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) BOOL fetchAllChanges;
```

## Discussion

If [`true`](../../Swift/true.md), the operation sends repeat requests to the server until it fetches all changes. CloudKit executes the handler you set on the [`changeTokenUpdatedBlock`](./changetokenupdatedblock.md) property with a change token after each request.

The default value is [`true`](../../Swift/true.md).

## See Also

### Configuring the Operation
- [var previousServerChangeToken: CKServerChangeToken?](./previousserverchangetoken.md)
  The server change token.
- [var resultsLimit: Int](./resultslimit.md)
  The maximum number of results that the operation fetches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/fetchallchanges)*