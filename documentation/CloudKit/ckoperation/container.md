# container

**Framework**: CloudKit  
**Kind**: property

The operation’s container.

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
var container: CKContainer? { get set }
```

#### Discussion

The container defines where the operation executes. The [`add(_:)`](ckcontainer/add(_:).md) method of the [`CKContainer`](ckcontainer.md) and [`CKDatabase`](ckdatabase.md) classes implicitly set this property to their container.

If you execute the operation yourself, either directly or using a custom operation queue, set the value of this property explicitly. If the value is `nil` when you execute an operation, the operation implicitly executes in your app’s default container.

## See Also

- [var allowsCellularAccess: Bool](ckoperation/allowscellularaccess.md)
  A Boolean value that indicates whether the operation can send data over the cellular network.
- [var isLongLived: Bool](ckoperation/islonglived.md)
  A Boolean value that indicates whether the operation is long-lived.
- [var timeoutIntervalForRequest: TimeInterval](ckoperation/timeoutintervalforrequest.md)
  The timeout interval when waiting for additional data.
- [var timeoutIntervalForResource: TimeInterval](ckoperation/timeoutintervalforresource.md)
  The maximum amount of time that a resource request can use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/container)*