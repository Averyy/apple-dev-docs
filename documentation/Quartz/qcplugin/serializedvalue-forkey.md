# serializedValue(forKey:)

**Framework**: Quartz  
**Kind**: method

A method implemented to override serialization.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func serializedValue(forKey key: String!) -> Any!
```

#### Return Value

Either `nil` or a value that’s compliant with property lists:  `NSString`, `NSNumber`, `NSDate`, `NSData`, `NSArray`, or `NSDictionary`.

#### Discussion

Provides custom serialization for patch internal settings that do not comply to the [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding) protocol.

#### Discussion

If your patch has internal settings that do not conform to the [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding) protocol, you must implement this method.

## Parameters

- `key`: The key for the value to retrieve.

## See Also

- [func setSerializedValue(Any!, forKey: String!)](qcplugin/setserializedvalue(_:forkey:).md)
  Provides custom deserialization for patch internal settings that were previously serialized using the method [`serializedValue(forKey:)`](qcplugin/serializedvalue(forkey:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/serializedvalue(forkey:))*