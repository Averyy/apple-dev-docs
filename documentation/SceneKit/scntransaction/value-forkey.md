# value(forKey:)

**Framework**: SceneKit  
**Kind**: method

Returns the object previously associated with the current transaction using the specified key.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func value(forKey key: String) -> Any?
```

#### Return Value

The object previously associated with the transaction (or an enclosing transaction) using the specified key, or `nil` if no value for that key could be found.

#### Discussion

Nested transactions have nested data scope. Setting a value for a key associates it with the current transaction (or innermost nested transaction) only, but reading the value for a key searches through nested transactions (starting from the innermost).

## Parameters

- `key`: The unique string identifying an object previously associated with the transaction.

## See Also

- [class func setValue(Any?, forKey: String)](scntransaction/setvalue(_:forkey:).md)
  Associates an arbitrary object with the current transaction using the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/value(forkey:))*