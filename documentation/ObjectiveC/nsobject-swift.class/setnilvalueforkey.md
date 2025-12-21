# setNilValueForKey(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Invoked by [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).

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
func setNilValueForKey(_ key: String)
```

#### Discussion

Subclasses can override this method to handle the request in some other way, such as by substituting `0` or a sentinel value for `nil` and invoking [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) again or setting the variable directly. The default implementation raises an `NSInvalidArgumentException`.

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

- [func setValue(Any?, forKeyPath: String)](nsobject-swift.class/setvalue(_:forkeypath:).md)
  Sets the value for the property identified by a given key path to a given value.
- [func setValuesForKeys([String : Any])](nsobject-swift.class/setvaluesforkeys(_:).md)
  Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
- [func setValue(Any?, forKey: String)](nsobject-swift.class/setvalue(_:forkey:).md)
  Sets the property of the receiver specified by a given key to a given value.
- [func setValue(Any?, forUndefinedKey: String)](nsobject-swift.class/setvalue(_:forundefinedkey:).md)
  Invoked by [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) when it finds no property for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setnilvalueforkey(_:))*