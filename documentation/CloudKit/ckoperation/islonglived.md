# isLongLived

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the operation is long-lived.

**Availability**:
- iOS 9.3+ - Deprecated in 11.0
- iPadOS 9.3+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.13
- tvOS 9.2+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`isLongLived`](./configuration-swift.class/islonglived.md) instead.

## Declaration

```swift
var isLongLived: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isLongLived) BOOL longLived;
```

#### Discussion

Set this property to [`true`](../../Swift/true.md) to make the operation long-lived. The default value is [`false`](../../Swift/false.md). If you change this property’s value after you execute the operation, the change has no effect.

For more information, see [Long-Lived Operations](../ckoperation.md#Long-Lived-Operations).

## See Also

### Deprecated Properties
- [var allowsCellularAccess: Bool](./allowscellularaccess.md)
  A Boolean value that indicates whether the operation can send data over the cellular network.
- [var container: CKContainer?](./container.md)
  The operation’s container.
- [var timeoutIntervalForRequest: TimeInterval](./timeoutintervalforrequest.md)
  The timeout interval when waiting for additional data.
- [var timeoutIntervalForResource: TimeInterval](./timeoutintervalforresource.md)
  The maximum amount of time that a resource request can use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/islonglived)*