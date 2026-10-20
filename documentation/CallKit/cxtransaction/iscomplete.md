# isComplete

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the transaction has been completed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var isComplete: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isComplete) BOOL complete;
```

#### Discussion

A transaction is complete only when all of its actions are complete.

## See Also

### Accessing Transaction Attributes
- [var uuid: UUID](./uuid.md)
  The unique identifier of the transaction.
- [var actions: [CXAction]](./actions.md)
  The actions added to a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxtransaction/iscomplete)*