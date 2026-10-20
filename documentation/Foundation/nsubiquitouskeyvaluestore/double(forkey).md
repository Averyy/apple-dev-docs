# double(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the double value associated with the specified key.

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
func double(forKey aKey: String) -> Double
```

```objc
- (double) doubleForKey:(NSString *) aKey;
```

#### Return Value

The double value associated with `aKey`, or `0.0` if the key isn’t present.

#### Discussion

This method automatically coerces certain types to their equivalent double values. The Boolean value `true` becomes `1.0` and `false` becomes `0.0`. An integer becomes the equivalent double –– for example, `2` becomes `2.0`. A string that contains a numerical value contains the equivalent double — for example, “123.4” becomes `123.4`.

## Parameters

- `aKey`: The key to retrieve from the iCloud key-value store.

## See Also

### Getting values
- [func bool(forKey: String) -> Bool](./bool%28forkey%29.md)
  Returns the Boolean value associated with the specified key.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/double(forkey:))*