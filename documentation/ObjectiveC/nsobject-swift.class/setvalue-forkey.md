# setValue(_:forKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Sets the property of the receiver specified by a given key to a given value.

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
func setValue(_ value: Any?, forKey key: String)
```

#### Discussion

If `key` identifies a to-one relationship, relate the object specified by `value` to the receiver, unrelating the previously related object if there was one. Given a collection object and a `key` that identifies a to-many relationship, relate the objects contained in the collection to the receiver, unrelating previously related objects if there were any.

The search pattern that `setValue:forKey:` uses is described in [`Accessor Search Patterns`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html#//apple_ref/doc/uid/20000955) in [`Key-Value Coding Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).

In a reference-counted environment, if the instance variable is accessed directly, `value` is retained.

## Parameters

- `value`: The value for the property identified by  .
- `key`: The name of one of the receiver’s properties.

## See Also

- [func setValue(Any?, forKeyPath: String)](nsobject-swift.class/setvalue(_:forkeypath:).md)
  Sets the value for the property identified by a given key path to a given value.
- [func setValuesForKeys([String : Any])](nsobject-swift.class/setvaluesforkeys(_:).md)
  Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
- [func setNilValueForKey(String)](nsobject-swift.class/setnilvalueforkey(_:).md)
  Invoked by [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) when it’s given a `nil` value for a scalar value (such as an `int` or `float`).
- [func setValue(Any?, forUndefinedKey: String)](nsobject-swift.class/setvalue(_:forundefinedkey:).md)
  Invoked by [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) when it finds no property for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setvalue(_:forkey:))*