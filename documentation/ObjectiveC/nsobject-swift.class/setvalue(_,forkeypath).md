# setValue(_:forKeyPath:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sets the value for the property identified by a given key path to a given value.

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
func setValue(_ value: Any?, forKeyPath keyPath: String)
```

```objc
- (void) setValue:(id) value forKeyPath:(NSString *) keyPath;
```

## Discussion

The default implementation of this method gets the destination object for each relationship using [`value(forKey:)`](./value%28forkey%29.md), and sends the final object a [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) message.

### Special Considerations

When using this method, and the destination object does not implement an accessor for the value, the default behavior is for that object to retain `value` rather than copy or assign `value`.

## Parameters

- `value`: The value for the property identified by `keyPath`.
- `keyPath`: A key path of the form relationship.property (with one or more relationships): for example “department.name” or “department.manager.lastName.”

## See Also

### Related Documentation
- [func value(forKeyPath: String) -> Any?](./value%28forkeypath%29.md)
  Returns the value for the derived property identified by a given key path.
### Setting Values
- [func setValuesForKeys([String : Any])](./setvaluesforkeys%28_%29.md)
  Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
- [func setNilValueForKey(String)](./setnilvalueforkey%28_%29.md)
  Invoked by [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).
- [func setValue(Any?, forKey: String)](./setvalue%28_,forkey%29.md)
  Sets the property of the receiver specified by a given key to a given value.
- [func setValue(Any?, forUndefinedKey: String)](./setvalue%28_,forundefinedkey%29.md)
  Invoked by [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) when it finds no property for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvalue(_:forkeypath:))*