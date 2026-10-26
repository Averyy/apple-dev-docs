# init(object:forKey:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a dictionary containing a given key and value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(object: Any, forKey key: any NSCopying)
```

```objc
+ (instancetype) dictionaryWithObject:(ObjectType) object forKey:(id<NSCopying>) key;
```

#### Return Value

A new dictionary containing a single object, `object`, for a single key, `aKey`.

## Parameters

- `object`: The value corresponding to `aKey`.

  If this value is `nil`, an [`invalidArgumentException`](../nsexceptionname/invalidargumentexception.md) is raised.
- `key`: The key for `anObject`.

  If this value is `nil`, an [`invalidArgumentException`](../nsexceptionname/invalidargumentexception.md) is raised.

## See Also

### Creating a Dictionary from Objects and Keys
- [convenience init(objects: [Any], forKeys: [any NSCopying])](./init%28objects,forkeys%29.md)
  Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.
- [init(objects: UnsafePointer<AnyObject>?, forKeys: UnsafePointer<any NSCopying>?, count: Int)](./init%28objects,forkeys,count%29.md)
  Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.
- [- initWithObjectsAndKeys:](./initwithobjectsandkeys_.md)
  Initializes a newly allocated dictionary with entries constructed from the specified set of values and keys.
### Related Documentation
- [+ dictionaryWithObjects:forKeys:](./dictionarywithobjects_forkeys_.md)
  Creates a dictionary containing entries constructed from the contents of an array of keys and an array of values.
- [+ dictionaryWithObjectsAndKeys:](./dictionarywithobjectsandkeys_.md)
  Creates a dictionary containing entries constructed from the specified set of values and keys.
- [+ dictionaryWithObjects:forKeys:count:](./dictionarywithobjects_forkeys_count_.md)
  Creates a dictionary containing a specified number of objects from a C array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/init(object:forkey:))*