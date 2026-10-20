# dictionaryRepresentation

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A dictionary with all of the key-value pairs in the iCloud key-value store.

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
var dictionaryRepresentation: [String : Any] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,id> * dictionaryRepresentation;
```

#### Discussion

Getting this property retrieves the in-memory copy of the keys and values. If changes to the keys and values are pending, the system fetches those changes from iCloud and updates the dictionary before returning it. To ensure the dictionary contains all recent changes, call [`synchronize()`](./synchronize%28%29.md) shortly before accessing this property. All of the values in the dictionary are property list object types.

## See Also

### Getting values
- [func bool(forKey: String) -> Bool](./bool%28forkey%29.md)
  Returns the Boolean value associated with the specified key.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/dictionaryrepresentation)*