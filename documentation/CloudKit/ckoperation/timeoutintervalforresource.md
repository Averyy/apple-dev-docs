# timeoutIntervalForResource

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The maximum amount of time that a resource request can use.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.13
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`timeoutIntervalForResource`](./configuration-swift.class/timeoutintervalforresource.md) instead.

## Declaration

```swift
var timeoutIntervalForResource: TimeInterval { get set }
```

```objc
@property (nonatomic, assign) NSTimeInterval timeoutIntervalForResource;
```

## Discussion

This property determines the resource timeout interval for this operation, which controls how long, in seconds, to wait for the entire operation to complete before stopping. The resource timer starts when the operation executes and counts until either the operation completes or this timeout interval occurs, whichever comes first.

The default value is `604800`, the number of seconds in 7 days.

## See Also

### Deprecated Properties
- [var allowsCellularAccess: Bool](./allowscellularaccess.md)
  A Boolean value that indicates whether the operation can send data over the cellular network.
- [var container: CKContainer?](./container.md)
  The operation’s container.
- [var isLongLived: Bool](./islonglived.md)
  A Boolean value that indicates whether the operation is long-lived.
- [var timeoutIntervalForRequest: TimeInterval](./timeoutintervalforrequest.md)
  The timeout interval when waiting for additional data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/timeoutintervalforresource)*