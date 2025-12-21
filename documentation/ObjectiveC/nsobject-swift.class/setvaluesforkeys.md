# setValuesForKeys(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.

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
func setValuesForKeys(_ keyedValues: [String : Any])
```

#### Discussion

The default implementation invokes [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) for each key-value pair, substituting `nil` for `NSNull` values in `keyedValues`.

## Parameters

- `keyedValues`: A dictionary whose keys identify properties in the receiver. The values of the properties in the receiver are set to the corresponding values in the dictionary.

## See Also

- [func dictionaryWithValues(forKeys: [String]) -> [String : Any]](nsobject-swift.class/dictionarywithvalues(forkeys:).md)
  Returns a dictionary containing the property values identified by each of the keys in a given array.
- [func setValue(Any?, forKeyPath: String)](nsobject-swift.class/setvalue(_:forkeypath:).md)
  Sets the value for the property identified by a given key path to a given value.
- [func setNilValueForKey(String)](nsobject-swift.class/setnilvalueforkey(_:).md)
  Invoked by [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).
- [func setValue(Any?, forKey: String)](nsobject-swift.class/setvalue(_:forkey:).md)
  Sets the property of the receiver specified by a given key to a given value.
- [func setValue(Any?, forUndefinedKey: String)](nsobject-swift.class/setvalue(_:forundefinedkey:).md)
  Invoked by [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) when it finds no property for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvaluesforkeys(_:))*