# serializedValue(forKey:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

A method implemented to override serialization.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func serializedValue(forKey key: String!) -> Any!
```

```objc
- (id) serializedValueForKey:(NSString *) key;
```

#### Return Value

Either `nil` or a value that’s compliant with property lists:  `NSString`, `NSNumber`, `NSDate`, `NSData`, `NSArray`, or `NSDictionary`.

#### Discussion

Provides custom serialization for patch internal settings that do not comply to the [`NSCoding`](../../Foundation/nscoding.md) protocol.

#### Discussion

If your patch has internal settings that do not conform to the [`NSCoding`](../../Foundation/nscoding.md) protocol, you must implement this method.

## Parameters

- `key`: The key for the value to retrieve.

## See Also

### Supporting Saving and Retrieving Internal Settings
- [func setSerializedValue(Any!, forKey: String!)](./setserializedvalue%28_,forkey%29.md)
  Provides custom deserialization for patch internal settings that were previously serialized using the method [`serializedValue(forKey:)`](./serializedvalue%28forkey%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/serializedvalue(forkey:))*