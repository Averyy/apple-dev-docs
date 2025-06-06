# setValue(_:forKey:)

**Framework**: SceneKit  
**Kind**: method

Associates an arbitrary object with the current transaction using the specified key.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func setValue(_ value: Any?, forKey key: String)
```

#### Discussion

Nested transactions have nested data scope. Setting a value for a key associates it with the current transaction (or innermost nested transaction) only, and reading the value for a key searches through nested transactions (starting from the innermost).

## Parameters

- `value`: An object to associate with the current transaction.
- `key`: A unique string identifying the object for later retrieval.

## See Also

- [class func value(forKey: String) -> Any?](scntransaction/value(forkey:).md)
  Returns the object previously associated with the current transaction using the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/setvalue(_:forkey:))*