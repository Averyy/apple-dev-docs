# setNilValueForKey(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Invoked by [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).

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
func setNilValueForKey(_ key: String)
```

```objc
- (void) setNilValueForKey:(NSString *) key;
```

#### Discussion

Subclasses can override this method to handle the request in some other way, such as by substituting `0` or a sentinel value for `nil` and invoking [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) again or setting the variable directly. The default implementation raises an `NSInvalidArgumentException`.

## Parameters

- `key`: The name of one of the receiver’s properties.

## See Also

### Setting Values
- [func setValue(Any?, forKeyPath: String)](./setvalue%28_,forkeypath%29.md)
  Sets the value for the property identified by a given key path to a given value.
- [func setValuesForKeys([String : Any])](./setvaluesforkeys%28_%29.md)
  Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
- [func setValue(Any?, forKey: String)](./setvalue%28_,forkey%29.md)
  Sets the property of the receiver specified by a given key to a given value.
- [func setValue(Any?, forUndefinedKey: String)](./setvalue%28_,forundefinedkey%29.md)
  Invoked by [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) when it finds no property for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setnilvalueforkey(_:))*