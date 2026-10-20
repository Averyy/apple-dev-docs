# bool(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the Boolean value associated with the specified key.

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
func bool(forKey aKey: String) -> Bool
```

```objc
- (BOOL) boolForKey:(NSString *) aKey;
```

#### Return Value

The Boolean value associated with `aKey`, or `false` if the key isn’t present.

#### Discussion

This method automatically coerces certain values to their equivalent Boolean meanings. For example, it coerces the numbers 1 and 1.0, and the strings “true”, “YES”, and “1” to the value `true`.

## Parameters

- `aKey`: The key to retrieve from the iCloud key-value store.

## See Also

### Getting values
- [func double(forKey: String) -> Double](./double%28forkey%29.md)
  Returns the double value associated with the specified key.
- [func longLong(forKey: String) -> Int64](./longlong%28forkey%29.md)
  Returns the 64-bit integer value associated with the specified key.
- [func string(forKey: String) -> String?](./string%28forkey%29.md)
  Returns the string associated with the specified key.
- [func data(forKey: String) -> Data?](./data%28forkey%29.md)
  Returns the data object associated with the specified key.
- [func object(forKey: String) -> Any?](./object%28forkey%29.md)
  Returns the object associated with the specified key.
- [func array(forKey: String) -> [Any]?](./array%28forkey%29.md)
  Returns the array associated with the specified key.
- [func dictionary(forKey: String) -> [String : Any]?](./dictionary%28forkey%29.md)
  Returns the dictionary object associated with the specified key.
- [var dictionaryRepresentation: [String : Any]](./dictionaryrepresentation.md)
  A dictionary with all of the key-value pairs in the iCloud key-value store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/bool(forkey:))*