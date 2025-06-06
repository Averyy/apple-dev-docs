# init(action:)

**Framework**: CallKit  
**Kind**: init

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

#### Return Value

A new transaction with the specified action.

#### Discussion

This initializer is a convenience for using the designated initializer and calling the [`addAction(_:)`](cxtransaction/addaction(_:).md) method passing `action`.

## Parameters

- `action`: The action to add to the transaction.

## See Also

- [init(actions: [CXAction])](cxtransaction/init(actions:).md)
  Initializes a new transaction with the specified actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxtransaction/init(action:))*