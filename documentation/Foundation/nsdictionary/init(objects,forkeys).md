# init(objects:forKeys:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.

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
convenience init(objects: [Any], forKeys keys: [any NSCopying])
```

```objc
- (instancetype) initWithObjects:(NSArray<id> *) objects forKeys:(NSArray<id<NSCopying>> *) keys;
```

## Discussion

This method steps through the `objects` and `keys` arrays, creating entries in the new dictionary as it goes. An `NSInvalidArgumentException` is raised if the objects and keys arrays do not have the same number of elements.

## Parameters

- `objects`: An array containing the values for the new dictionary.
- `keys`: An array containing the keys for the new dictionary. Each key is copied (using [`copy(with:)`](../nscopying/copy%28with%29.md); keys must conform to the `NSCopying` protocol), and the copy is added to the new dictionary.

## See Also

### Creating a Dictionary from Objects and Keys
- [init(objects: UnsafePointer<AnyObject>?, forKeys: UnsafePointer<any NSCopying>?, count: Int)](./init%28objects,forkeys,count%29.md)
  Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.
- [convenience init(object: Any, forKey: any NSCopying)](./init%28object,forkey%29.md)
  Creates a dictionary containing a given key and value.
- [+ dictionaryWithObjects:forKeys:count:](./dictionarywithobjects_forkeys_count_.md)
  Creates a dictionary containing a specified number of objects from a C array.
- [+ dictionaryWithObjectsAndKeys:](./dictionarywithobjectsandkeys_.md)
  Creates a dictionary containing entries constructed from the specified set of values and keys.
### Related Documentation
- [- initWithObjectsAndKeys:](./initwithobjectsandkeys_.md)
  Initializes a newly allocated dictionary with entries constructed from the specified set of values and keys.
- [+ dictionaryWithObjects:forKeys:](./dictionarywithobjects_forkeys_.md)
  Creates a dictionary containing entries constructed from the contents of an array of keys and an array of values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/init(objects:forkeys:))*