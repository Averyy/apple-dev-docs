# dictionary(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the dictionary object associated with the specified key.

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
func dictionary(forKey defaultName: String) -> [String : Any]?
```

```objc
- (NSDictionary<NSString *,id> *) dictionaryForKey:(NSString *) defaultName;
```

#### Return Value

The dictionary object associated with `defaultName`, or `nil` if the key isn’t present in the defaults database. This method also returns `nil` if the retrieved value isn’t a dictionary object.

#### Discussion

The returned dictionary and its contents are immutable, even if you originally set the key to mutable values.

## Parameters

- `defaultName`: The key to retrieve from the defaults database.

## See Also

### Getting the value of a key
- [func bool(forKey: String) -> Bool](./bool%28forkey%29.md)
  Returns the Boolean value associated with the specified key.
- [func integer(forKey: String) -> Int](./integer%28forkey%29.md)
  Returns the integer value associated with the specified key.
- [func float(forKey: String) -> Float](./float%28forkey%29.md)
  Returns the floating-point value associated with the specified key.
- [func double(forKey: String) -> Double](./double%28forkey%29.md)
  Returns the double value associated with the specified key.
- [func url(forKey: String) -> URL?](./url%28forkey%29.md)
  Returns the URL associated with the specified key.
- [func string(forKey: String) -> String?](./string%28forkey%29.md)
  Returns the string associated with the specified key.
- [func stringArray(forKey: String) -> [String]?](./stringarray%28forkey%29.md)
  Returns the array of strings associated with the specified key.
- [func data(forKey: String) -> Data?](./data%28forkey%29.md)
  Returns the data object associated with the specified key.
- [func object(forKey: String) -> Any?](./object%28forkey%29.md)
  Returns the object associated with the specified key.
- [func array(forKey: String) -> [Any]?](./array%28forkey%29.md)
  Returns the array associated with the specified key.
- [func dictionaryRepresentation() -> [String : Any]](./dictionaryrepresentation%28%29.md)
  Returns a dictionary with the union of all key-value pairs found from all domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/dictionary(forkey:))*