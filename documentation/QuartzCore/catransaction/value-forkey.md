# value(forKey:)

**Framework**: Core Animation  
**Kind**: method

Returns the arbitrary keyed-data specified by the given key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func value(forKey key: String) -> Any?
```

#### Return Value

The value for the data specified by the key.

#### Discussion

Nested transactions have nested data scope. Requesting a value for a key first searches the innermost scope, then the enclosing transactions.

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

- [class func setValue(Any?, forKey: String)](catransaction/setvalue(_:forkey:).md)
  Sets the arbitrary keyed-data for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/value(forkey:))*