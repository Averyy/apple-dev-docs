# init(actions:)

**Framework**: CallKit  
**Kind**: init

Initializes a new transaction with the specified actions.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(actions: [CXAction])
```

#### Return Value

A new transaction with the specified actions.

#### Discussion

This initializer is a convenience for using the designated initializer and calling the [`addAction(_:)`](cxtransaction/addaction(_:).md) method passing each object in `actions`.

## Parameters

- `actions`: The actions to added to the transaction.

## See Also

- [convenience init(action: CXAction)](cxtransaction/init(action:).md)
  Initializes a new transaction with the specified action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxtransaction/init(actions:))*