# allowsCellularAccess

**Framework**: CloudKit  
**Kind**: property

A Boolean value that indicates whether the operation can send data over the cellular network.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var allowsCellularAccess: Bool { get set }
```

#### Discussion

When you send or receive many records, or when you send records with large assets, you might set this property to [`false`](https://developer.apple.com/documentation/Swift/false) to avoid consuming too much of the user’s cellular data bandwidth. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

When this property is [`false`](https://developer.apple.com/documentation/Swift/false), the operation fails if Wi-Fi isn’t available.

## See Also

- [var container: CKContainer?](ckoperation/container.md)
  The operation’s container.
- [var isLongLived: Bool](ckoperation/islonglived.md)
  A Boolean value that indicates whether the operation is long-lived.
- [var timeoutIntervalForRequest: TimeInterval](ckoperation/timeoutintervalforrequest.md)
  The timeout interval when waiting for additional data.
- [var timeoutIntervalForResource: TimeInterval](ckoperation/timeoutintervalforresource.md)
  The maximum amount of time that a resource request can use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/allowscellularaccess)*