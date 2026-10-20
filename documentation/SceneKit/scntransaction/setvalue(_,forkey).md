# setValue(_:forKey:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Associates an arbitrary object with the current transaction using the specified key.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class func setValue(_ value: Any?, forKey key: String)
```

```objc
+ (void) setValue:(id) value forKey:(NSString *) key;
```

#### Discussion

Nested transactions have nested data scope. Setting a value for a key associates it with the current transaction (or innermost nested transaction) only, and reading the value for a key searches through nested transactions (starting from the innermost).

## Parameters

- `value`: An object to associate with the current transaction.
- `key`: A unique string identifying the object for later retrieval.

## See Also

### Getting and Setting Transaction Properties
- [class func value(forKey: String) -> Any?](./value%28forkey%29.md)
  Returns the object previously associated with the current transaction using the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/setvalue(_:forkey:))*