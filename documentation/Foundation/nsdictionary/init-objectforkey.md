# init(object:forKey:)

**Framework**: Foundation  
**Kind**: init

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

#### Return Value

A new dictionary containing a single object, `object`, for a single key, `aKey`.

## Parameters

- `object`: If this value is  , an   is raised.
- `key`: If this value is  , an   is raised.

## See Also

- [convenience init(objects: [Any], forKeys: [any NSCopying])](nsdictionary/init(objects:forkeys:).md)
  Initializes a newly allocated dictionary with key-value pairs constructed from the provided arrays of keys and objects.
- [init(objects: UnsafePointer<AnyObject>?, forKeys: UnsafePointer<any NSCopying>?, count: Int)](nsdictionary/init(objects:forkeys:count:).md)
  Initializes a newly allocated dictionary with the specified number of key-value pairs constructed from the provided C arrays of keys and objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/init(object:forkey:))*