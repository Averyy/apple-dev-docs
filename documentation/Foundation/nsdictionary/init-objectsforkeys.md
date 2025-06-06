# init(objects:forKeys:)

**Framework**: Foundation  
**Kind**: init

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

#### Discussion

This method steps through the `objects` and `keys` arrays, creating entries in the new dictionary as it goes. An `NSInvalidArgumentException` is raised if the objects and keys arrays do not have the same number of elements.

## Parameters

- `objects`: An array containing the values for the new dictionary.
- `keys`: An array containing the keys for the new dictionary. Each key is copied (using  ; keys must conform to the   protocol), and the copy is added to the new dictionary.

## See Also

- [init(objects: UnsafePointer<AnyObject>?, forKeys: UnsafePointer<any NSCopying>?, count: Int)](nsdictionary/init(objects:forkeys:count:).md)
  Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.
- [convenience init(object: Any, forKey: any NSCopying)](nsdictionary/init(object:forkey:).md)
  Creates a dictionary containing a given key and value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/init(objects:forkeys:))*