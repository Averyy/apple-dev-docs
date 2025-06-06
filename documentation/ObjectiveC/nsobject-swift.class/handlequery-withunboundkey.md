# handleQuery(withUnboundKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Invoked by [`value(forKey:)`](nsobject-swift.class/value(forkey:).md) when it finds no property corresponding to `key`.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func handleQuery(withUnboundKey key: String) -> Any?
```

## See Also

- [class func useStoredAccessor() -> Bool](nsobject-swift.class/usestoredaccessor.md)
  Returns `true` if the stored value methods [`storedValue(forKey:)`](nsobject-swift.class/storedvalue(forkey:).md) and [`takeStoredValue(_:forKey:)`](nsobject-swift.class/takestoredvalue(_:forkey:).md) should use private accessor methods in preference to public accessors.
- [func handleTakeValue(Any?, forUnboundKey: String)](nsobject-swift.class/handletakevalue(_:forunboundkey:).md)
  Invoked by [`takeValue(_:forKey:)`](nsobject-swift.class/takevalue(_:forkey:).md) when it finds no property binding for `key`.
- [func storedValue(forKey: String) -> Any?](nsobject-swift.class/storedvalue(forkey:).md)
  Returns the property identified by a given key.
- [func takeStoredValue(Any?, forKey: String)](nsobject-swift.class/takestoredvalue(_:forkey:).md)
  Sets the value of the property identified by a given key.
- [func takeValues(from: [AnyHashable : Any])](nsobject-swift.class/takevalues(from:).md)
  Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties
- [func takeValue(Any?, forKeyPath: String)](nsobject-swift.class/takevalue(_:forkeypath:).md)
  Sets the value for the property identified by `keyPath` to `value`.
- [func takeValue(Any?, forKey: String)](nsobject-swift.class/takevalue(_:forkey:).md)
  Sets the value for the property identified by `key` to `value`.
- [func unableToSetNil(forKey: String)](nsobject-swift.class/unabletosetnil(forkey:).md)
  Invoked if `key` is represented by a scalar attribute.
- [func values(forKeys: [Any]) -> [AnyHashable : Any]](nsobject-swift.class/values(forkeys:).md)
  Returns a dictionary containing as keys the property names in `keys`, with corresponding values being the corresponding property values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/handlequery(withunboundkey:))*