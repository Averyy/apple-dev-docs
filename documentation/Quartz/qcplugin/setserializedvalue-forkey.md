# setSerializedValue(_:forKey:)

**Framework**: Quartz  
**Kind**: method

Provides custom deserialization for patch internal settings that were previously serialized using the method [`serializedValue(forKey:)`](qcplugin/serializedvalue(forkey:).md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setSerializedValue(_ serializedValue: Any!, forKey key: String!)
```

#### Discussion

If your patch has internal settings that do not conform to the [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding) protocol, you must implement this method. After you deserialize the value, you need to call  `[self set:value forKey:key]` to set the corresponding internal setting of the custom patch instance to the deserialized value.

## Parameters

- `serializedValue`: The value to deserialize.
- `key`: The key for the value to deserialize.

## See Also

- [func serializedValue(forKey: String!) -> Any!](qcplugin/serializedvalue(forkey:).md)
  A method implemented to override serialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/setserializedvalue(_:forkey:))*