# actions

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The actions added to a transaction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var actions: [CXAction] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<__kindof CXAction *> * actions;
```

## See Also

### Accessing Transaction Attributes
- [var uuid: UUID](./uuid.md)
  The unique identifier of the transaction.
- [var isComplete: Bool](./iscomplete.md)
  A Boolean value that indicates whether the transaction has been completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxtransaction/actions)*