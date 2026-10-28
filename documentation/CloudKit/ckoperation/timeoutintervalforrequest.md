# timeoutIntervalForRequest

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The timeout interval when waiting for additional data.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.13
- tvOS 10.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`timeoutIntervalForRequest`](./configuration-swift.class/timeoutintervalforrequest.md) instead.

## Declaration

```swift
var timeoutIntervalForRequest: TimeInterval { get set }
```

```objc
@property (nonatomic, assign) NSTimeInterval timeoutIntervalForRequest;
```

## Discussion

This property determines the request timeout interval for the operation, which controls how long, in seconds, the operation waits for additional data to arrive before stopping. The timer for this value resets whenever new data arrives. When the timer reaches the interval without receiving any new data, it triggers a timeout.

The default value is `60`.

## See Also

### Deprecated Properties
- [var allowsCellularAccess: Bool](./allowscellularaccess.md)
  A Boolean value that indicates whether the operation can send data over the cellular network.
- [var container: CKContainer?](./container.md)
  The operation’s container.
- [var isLongLived: Bool](./islonglived.md)
  A Boolean value that indicates whether the operation is long-lived.
- [var timeoutIntervalForResource: TimeInterval](./timeoutintervalforresource.md)
  The maximum amount of time that a resource request can use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/timeoutintervalforrequest)*