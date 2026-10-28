# set(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the value of the specified key to a property list object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func set(_ anObject: Any?, forKey aKey: String)
```

```objc
- (void) setObject:(id) anObject forKey:(NSString *) aKey;
```

## Discussion

Use this method to write property list object types to the iCloud key-value store.

## Parameters

- `anObject`: The property list type to save to the iCloud key-value store.
- `aKey`: The key to associate with the value.

## See Also

### Setting values
- [func set(Bool, forKey: String)](./set%28_,forkey%29-8o8mq.md)
  Sets the value of the specified key to a Boolean value.
- [func set(Double, forKey: String)](./set%28_,forkey%29-1xml0.md)
  Sets the value of the specified key to a double value.
- [func set(Int64, forKey: String)](./set%28_,forkey%29-7tt20.md)
  Sets the value of the specified key to a 64-bit integer value.
- [func set(String?, forKey: String)](./set%28_,forkey%29-2rlp.md)
  Sets the value of the specified key to a string value.
- [func set(Data?, forKey: String)](./set%28_,forkey%29-3ga7z.md)
  Sets the value of the specified key to a data object.
- [func set([Any]?, forKey: String)](./set%28_,forkey%29-40a8f.md)
  Sets the value of the specified key to an array of property list objects.
- [func set([String : Any]?, forKey: String)](./set%28_,forkey%29-9vmlm.md)
  Sets the value of the specified key to a dictionary of property list objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/set(_:forkey:)-9e3de)*