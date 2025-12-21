# isLongLived

**Framework**: CloudKit  
**Kind**: property

A Boolean value that indicates whether the operation is long-lived.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var isLongLived: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/Swift/true) to make the operation long-lived. The default value is [`false`](https://developer.apple.com/documentation/Swift/false). If you change this property’s value after you execute the operation, the change has no effect.

For more information, see [`Long-Lived Operations`](ckoperation#Long-Lived-Operations.md).

## See Also

- [var allowsCellularAccess: Bool](ckoperation/allowscellularaccess.md)
  A Boolean value that indicates whether the operation can send data over the cellular network.
- [var container: CKContainer?](ckoperation/container.md)
  The operation’s container.
- [var timeoutIntervalForRequest: TimeInterval](ckoperation/timeoutintervalforrequest.md)
  The timeout interval when waiting for additional data.
- [var timeoutIntervalForResource: TimeInterval](ckoperation/timeoutintervalforresource.md)
  The maximum amount of time that a resource request can use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/islonglived)*