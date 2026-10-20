# setValue(_:forUndefinedKey:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Invoked by [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) when it finds no property for a given key.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func setValue(_ value: Any?, forUndefinedKey key: String)
```

```objc
- (void) setValue:(id) value forUndefinedKey:(NSString *) key;
```

#### Discussion

Subclasses can override this method to handle the request in some other way. The default implementation raises an `NSUndefinedKeyException`.

## Parameters

- `value`: The value for the key identified by `key`.
- `key`: A string that is not equal to the name of any of the receiver’s properties.

## See Also

### Related Documentation
- [func value(forUndefinedKey: String) -> Any?](./value%28forundefinedkey%29.md)
  Invoked by [`value(forKey:)`](./value%28forkey%29.md) when it finds no property corresponding to a given key.
### Setting Values
- [func setValue(Any?, forKeyPath: String)](./setvalue%28_,forkeypath%29.md)
  Sets the value for the property identified by a given key path to a given value.
- [func setValuesForKeys([String : Any])](./setvaluesforkeys%28_%29.md)
  Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
- [func setNilValueForKey(String)](./setnilvalueforkey%28_%29.md)
  Invoked by [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).
- [func setValue(Any?, forKey: String)](./setvalue%28_,forkey%29.md)
  Sets the property of the receiver specified by a given key to a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvalue(_:forundefinedkey:))*