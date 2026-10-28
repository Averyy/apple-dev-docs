# setSerializedValue(_:forKey:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Provides custom deserialization for patch internal settings that were previously serialized using the method [`serializedValue(forKey:)`](./serializedvalue%28forkey%29.md).

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func setSerializedValue(_ serializedValue: Any!, forKey key: String!)
```

```objc
- (void) setSerializedValue:(id) serializedValue forKey:(NSString *) key;
```

## Discussion

If your patch has internal settings that do not conform to the [`NSCoding`](../../Foundation/nscoding.md) protocol, you must implement this method. After you deserialize the value, you need to call  `[self set:value forKey:key]` to set the corresponding internal setting of the custom patch instance to the deserialized value.

## Parameters

- `serializedValue`: The value to deserialize.
- `key`: The key for the value to deserialize.

## See Also

### Supporting Saving and Retrieving Internal Settings
- [func serializedValue(forKey: String!) -> Any!](./serializedvalue%28forkey%29.md)
  A method implemented to override serialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/setserializedvalue(_:forkey:))*