# set(_:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the value of the specified key to a data object.

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
func set(_ aData: Data?, forKey aKey: String)
```

```objc
- (void) setData:(NSData *) aData forKey:(NSString *) aKey;
```

## Discussion

To store types that aren’t property list objects, archive them to an [`NSData`](../nsdata.md) object first and add that object to the store using this method. Exercise caution when saving custom objects to iCloud. Instances of your app on a person’s other devices must also be able to extract the objects and use them. Design your objects to be portable, and design new versions of your app to support previous versions of your custom types.

## Parameters

- `aData`: The data object to save to the iCloud key-value store.
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
- [func set(Any?, forKey: String)](./set%28_,forkey%29-9e3de.md)
  Sets the value of the specified key to a property list object.
- [func set([Any]?, forKey: String)](./set%28_,forkey%29-40a8f.md)
  Sets the value of the specified key to an array of property list objects.
- [func set([String : Any]?, forKey: String)](./set%28_,forkey%29-9vmlm.md)
  Sets the value of the specified key to a dictionary of property list objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/set(_:forkey:)-3ga7z)*