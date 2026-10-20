# allowsCellularAccess

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the operation can send data over the cellular network.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.10+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`allowsCellularAccess`](./configuration-swift.class/allowscellularaccess.md) instead.

## Declaration

```swift
var allowsCellularAccess: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL allowsCellularAccess;
```

#### Discussion

When you send or receive many records, or when you send records with large assets, you might set this property to [`false`](../../Swift/false.md) to avoid consuming too much of the user’s cellular data bandwidth. The default value is [`true`](../../Swift/true.md).

When this property is [`false`](../../Swift/false.md), the operation fails if Wi-Fi isn’t available.

## See Also

### Deprecated Properties
- [var container: CKContainer?](./container.md)
  The operation’s container.
- [var isLongLived: Bool](./islonglived.md)
  A Boolean value that indicates whether the operation is long-lived.
- [var timeoutIntervalForRequest: TimeInterval](./timeoutintervalforrequest.md)
  The timeout interval when waiting for additional data.
- [var timeoutIntervalForResource: TimeInterval](./timeoutintervalforresource.md)
  The maximum amount of time that a resource request can use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/allowscellularaccess)*