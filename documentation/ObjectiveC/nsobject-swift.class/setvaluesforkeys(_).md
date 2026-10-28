# setValuesForKeys(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.

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
func setValuesForKeys(_ keyedValues: [String : Any])
```

```objc
- (void) setValuesForKeysWithDictionary:(NSDictionary<NSString *,id> *) keyedValues;
```

## Discussion

The default implementation invokes [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) for each key-value pair, substituting `nil` for `NSNull` values in `keyedValues`.

## Parameters

- `keyedValues`: A dictionary whose keys identify properties in the receiver. The values of the properties in the receiver are set to the corresponding values in the dictionary.

## See Also

### Related Documentation
- [func dictionaryWithValues(forKeys: [String]) -> [String : Any]](./dictionarywithvalues%28forkeys%29.md)
  Returns a dictionary containing the property values identified by each of the keys in a given array.
### Setting Values
- [func setValue(Any?, forKeyPath: String)](./setvalue%28_,forkeypath%29.md)
  Sets the value for the property identified by a given key path to a given value.
- [func setNilValueForKey(String)](./setnilvalueforkey%28_%29.md)
  Invoked by [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).
- [func setValue(Any?, forKey: String)](./setvalue%28_,forkey%29.md)
  Sets the property of the receiver specified by a given key to a given value.
- [func setValue(Any?, forUndefinedKey: String)](./setvalue%28_,forundefinedkey%29.md)
  Invoked by [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) when it finds no property for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvaluesforkeys(_:))*