# container

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The operation’s container.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.10+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`container`](./configuration-swift.class/container.md) instead.

## Declaration

```swift
var container: CKContainer? { get set }
```

```objc
@property (nonatomic, strong, nullable) CKContainer * container;
```

## Discussion

The container defines where the operation executes. The [`add(_:)`](../ckcontainer/add%28_%29.md) method of the [`CKContainer`](../ckcontainer.md) and [`CKDatabase`](../ckdatabase.md) classes implicitly set this property to their container.

If you execute the operation yourself, either directly or using a custom operation queue, set the value of this property explicitly. If the value is `nil` when you execute an operation, the operation implicitly executes in your app’s default container.

## See Also

### Deprecated Properties
- [var allowsCellularAccess: Bool](./allowscellularaccess.md)
  A Boolean value that indicates whether the operation can send data over the cellular network.
- [var isLongLived: Bool](./islonglived.md)
  A Boolean value that indicates whether the operation is long-lived.
- [var timeoutIntervalForRequest: TimeInterval](./timeoutintervalforrequest.md)
  The timeout interval when waiting for additional data.
- [var timeoutIntervalForResource: TimeInterval](./timeoutintervalforresource.md)
  The maximum amount of time that a resource request can use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/container)*