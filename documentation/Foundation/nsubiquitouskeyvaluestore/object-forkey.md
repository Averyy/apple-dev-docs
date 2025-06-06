# object(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns the object associated with the specified key.

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
func object(forKey aKey: String) -> Any?
```

#### Return Value

The object associated with the specified key or `nil` if the key was not found.

#### Discussion

You can use this method to retrieve objects whose type you do not necessarily know from the key-value store. The object returned by this method is always one of the property list types: [`NSNumber`](nsnumber.md), [`NSString`](nsstring.md), [`NSDate`](nsdate.md), [`NSData`](nsdata.md), [`NSArray`](nsarray.md), or [`NSDictionary`](nsdictionary.md).

## Parameters

- `aKey`: A key in the key-value store.

## See Also

- [func set(Any?, forKey: String)](nsubiquitouskeyvaluestore/set(_:forkey:)-9e3de.md)
  Sets an object for the specified key in the key-value store.
- [func array(forKey: String) -> [Any]?](nsubiquitouskeyvaluestore/array(forkey:).md)
  Returns the array associated with the specified key.
- [func bool(forKey: String) -> Bool](nsubiquitouskeyvaluestore/bool(forkey:).md)
  Returns the Boolean value associated with the specified key.
- [func data(forKey: String) -> Data?](nsubiquitouskeyvaluestore/data(forkey:).md)
  Returns the data object associated with the specified key.
- [func dictionary(forKey: String) -> [String : Any]?](nsubiquitouskeyvaluestore/dictionary(forkey:).md)
  Returns the dictionary object associated with the specified key.
- [func double(forKey: String) -> Double](nsubiquitouskeyvaluestore/double(forkey:).md)
  Returns the double value associated with the specified key.
- [func longLong(forKey: String) -> Int64](nsubiquitouskeyvaluestore/longlong(forkey:).md)
  Returns the `long long` value associated with the specified key.
- [func string(forKey: String) -> String?](nsubiquitouskeyvaluestore/string(forkey:).md)
  Returns the string associated with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/object(forkey:))*