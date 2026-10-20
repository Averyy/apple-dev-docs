# handleTakeValue(_:forUnboundKey:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Invoked by [`takeValue(_:forKey:)`](./takevalue%28_,forkey%29.md) when it finds no property binding for `key`.

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`setValue(_:forUndefinedKey:)`](./setvalue%28_,forundefinedkey%29.md) instead.

## Declaration

```swift
func handleTakeValue(_ value: Any?, forUnboundKey key: String)
```

```objc
- (void) handleTakeValue:(id) value forUnboundKey:(NSString *) key;
```

## See Also

### Deprecated Methods
- [class func useStoredAccessor() -> Bool](./usestoredaccessor%28%29.md)
  Returns `true` if the stored value methods [`storedValue(forKey:)`](./storedvalue%28forkey%29.md) and [`takeStoredValue(_:forKey:)`](./takestoredvalue%28_,forkey%29.md) should use private accessor methods in preference to public accessors.
- [func handleQuery(withUnboundKey: String) -> Any?](./handlequery%28withunboundkey%29.md)
  Invoked by [`value(forKey:)`](./value%28forkey%29.md) when it finds no property corresponding to `key`.
- [func storedValue(forKey: String) -> Any?](./storedvalue%28forkey%29.md)
  Returns the property identified by a given key.
- [func takeStoredValue(Any?, forKey: String)](./takestoredvalue%28_,forkey%29.md)
  Sets the value of the property identified by a given key.
- [func takeValues(from: [AnyHashable : Any])](./takevalues%28from%29.md)
  Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties
- [func takeValue(Any?, forKeyPath: String)](./takevalue%28_,forkeypath%29.md)
  Sets the value for the property identified by `keyPath` to `value`.
- [func takeValue(Any?, forKey: String)](./takevalue%28_,forkey%29.md)
  Sets the value for the property identified by `key` to `value`.
- [func unableToSetNil(forKey: String)](./unabletosetnil%28forkey%29.md)
  Invoked if `key` is represented by a scalar attribute.
- [func values(forKeys: [Any]) -> [AnyHashable : Any]](./values%28forkeys%29.md)
  Returns a dictionary containing as keys the property names in `keys`, with corresponding values being the corresponding property values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/handletakevalue(_:forunboundkey:))*