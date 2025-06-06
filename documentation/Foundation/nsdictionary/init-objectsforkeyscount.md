# init(objects:forKeys:count:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.

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
init(objects: UnsafePointer<AnyObject>?, forKeys keys: UnsafePointer<any NSCopying>?, count cnt: Int)
```

#### Discussion

This method steps through the `objects` and `keys` arrays, creating entries in the new dictionary as it goes. An `NSInvalidArgumentException` is raised if a key or value object is `nil`.

This method is a designated initializer of `NSDictionary`.

## Parameters

- `objects`: A C array of values for the new dictionary.
- `keys`: A C array of keys for the new dictionary. Each key is copied (using  ; keys must conform to the   protocol), and the copy is added to the new dictionary.
- `cnt`: The number of elements to use from the   and   arrays.   must not exceed the number of elements in   or  .

## See Also

- [init()](nsdictionary/init.md)
  Initializes a newly allocated dictionary.
- [convenience init(objects: [Any], forKeys: [any NSCopying])](nsdictionary/init(objects:forkeys:).md)
  Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.
- [convenience init(object: Any, forKey: any NSCopying)](nsdictionary/init(object:forkey:).md)
  Creates a dictionary containing a given key and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/init(objects:forkeys:count:))*