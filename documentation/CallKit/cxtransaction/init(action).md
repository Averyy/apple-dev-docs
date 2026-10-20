# init(action:)

**Framework**: CallKit  
**Kind**: init  
**Role**: Initializer

Initializes a new transaction with the specified action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
convenience init(action: CXAction)
```

```objc
- (instancetype) initWithAction:(CXAction *) action;
```

#### Return Value

A new transaction with the specified action.

#### Discussion

This initializer is a convenience for using the designated initializer and calling the [`addAction(_:)`](./addaction%28_%29.md) method passing `action`.

## Parameters

- `action`: The action to add to the transaction.

## See Also

### Creating New Transactions
- [init(actions: [CXAction])](./init%28actions%29.md)
  Initializes a new transaction with the specified actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxtransaction/init(action:))*