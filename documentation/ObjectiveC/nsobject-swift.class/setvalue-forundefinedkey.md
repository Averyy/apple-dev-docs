# setValue(_:forUndefinedKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Invoked by [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) when it finds no property for a given key.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func setValue(_ value: Any?, forUndefinedKey key: String)
```

#### Discussion

Subclasses can override this method to handle the request in some other way. The default implementation raises an `NSUndefinedKeyException`.

## Parameters

- `value`: The value for the key identified by  .
- `key`: A string that is not equal to the name of any of the receiver’s properties.

## See Also

- [func value(forUndefinedKey: String) -> Any?](nsobject-swift.class/value(forundefinedkey:).md)
  Invoked by [`value(forKey:)`](nsobject-swift.class/value(forkey:).md) when it finds no property corresponding to a given key.
- [func setValue(Any?, forKeyPath: String)](nsobject-swift.class/setvalue(_:forkeypath:).md)
  Sets the value for the property identified by a given key path to a given value.
- [func setValuesForKeys([String : Any])](nsobject-swift.class/setvaluesforkeys(_:).md)
  Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
- [func setNilValueForKey(String)](nsobject-swift.class/setnilvalueforkey(_:).md)
  Invoked by [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).
- [func setValue(Any?, forKey: String)](nsobject-swift.class/setvalue(_:forkey:).md)
  Sets the property of the receiver specified by a given key to a given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvalue(_:forundefinedkey:))*