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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/init(object:forkey:))*