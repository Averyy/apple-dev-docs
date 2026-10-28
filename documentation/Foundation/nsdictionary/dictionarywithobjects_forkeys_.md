# dictionaryWithObjects:forKeys:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a dictionary containing entries constructed from the contents of an array of keys and an array of values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) dictionaryWithObjects:(NSArray<id> *) objects forKeys:(NSArray<id<NSCopying>> *) keys;
```

## Return Value

A new dictionary containing entries constructed from the contents of `objects` and `keys`.

## Discussion

This method steps through the `objects` and `keys` arrays, creating entries in the new dictionary as it goes. An `NSInvalidArgumentException` is raised if objects and keys don’t have the same number of elements.

## Parameters

- `objects`: An array containing the values for the new dictionary.
- `keys`: An array containing the keys for the new dictionary. Each key is copied (using [`copy(with:)`](../nscopying/copy%28with%29.md); keys must conform to the `NSCopying` protocol), and the copy is added to the dictionary.

## See Also

### Creating a Dictionary from Objects and Keys
- [+ dictionaryWithObjects:forKeys:count:](./dictionarywithobjects_forkeys_count_.md)
  Creates a dictionary containing a specified number of objects from a C array.
- [convenience init(objects: [Any], forKeys: [any NSCopying])](./init%28objects,forkeys%29.md)
  Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.
- [init(objects: UnsafePointer<AnyObject>?, forKeys: UnsafePointer<any NSCopying>?, count: Int)](./init%28objects,forkeys,count%29.md)
  Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.
- [+ dictionaryWithObjectsAndKeys:](./dictionarywithobjectsandkeys_.md)
  Creates a dictionary containing entries constructed from the specified set of values and keys.
- [- initWithObjectsAndKeys:](./initwithobjectsandkeys_.md)
  Initializes a newly allocated dictionary with entries constructed from the specified set of values and keys.
- [convenience init(object: Any, forKey: any NSCopying)](./init%28object,forkey%29.md)
  Creates a dictionary containing a given key and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/dictionarywithobjects:forkeys:)*