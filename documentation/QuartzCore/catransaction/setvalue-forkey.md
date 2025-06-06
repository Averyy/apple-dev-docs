# setValue(_:forKey:)

**Framework**: Core Animation  
**Kind**: method

Sets the arbitrary keyed-data for the specified key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func setValue(_ anObject: Any?, forKey key: String)
```

#### Discussion

Nested transactions have nested data scope; setting a key always sets it in the innermost scope.

## Parameters

- `anObject`: The value for the key identified by  .
- `key`: The name of one of the receiver’s properties.

## See Also

- [class func value(forKey: String) -> Any?](catransaction/value(forkey:).md)
  Returns the arbitrary keyed-data specified by the given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/setvalue(_:forkey:))*