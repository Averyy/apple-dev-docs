# uuid

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The unique identifier of the transaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var uuid: UUID { get }
```

```objc
@property (nonatomic, copy, readonly) NSUUID * UUID;
```

## See Also

### Accessing Transaction Attributes
- [var isComplete: Bool](./iscomplete.md)
  A Boolean value that indicates whether the transaction has been completed.
- [var actions: [CXAction]](./actions.md)
  The actions added to a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxtransaction/uuid)*