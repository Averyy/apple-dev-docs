# decodeObject(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes and returns an object associated with a given key.

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
func decodeObject(forKey key: String) -> Any?
```

```objc
- (id) decodeObjectForKey:(NSString *) key;
```

#### Return Value

The object associated with the key `key`. Returns `nil` if `key` does not exist, or if the value for `key` is `nil`.

## Parameters

- `key`: A key in the archive within the current decoding scope. `key` must not be `nil`.

## See Also

### Related Documentation
- [func encode(Any?, forKey: String)](../nskeyedarchiver/encode%28_,forkey%29-9f4n9.md)
  Encodes a given object and associates it with a given key.
### Decoding Data
- [func containsValue(forKey: String) -> Bool](./containsvalue%28forkey%29.md)
  Returns a Boolean value that indicates whether the archive contains a value for a given key within the current decoding scope.
- [func decodeDecodable<T>(T.Type, forKey: String) -> T?](./decodedecodable%28_,forkey%29.md)
  Decodes a decodable value associated with a given key.
- [func decodeTopLevelDecodable<T>(T.Type, forKey: String) throws -> T?](./decodetopleveldecodable%28_,forkey%29.md)
  Decodes a top-level decodable value associated with a given key.
- [func decodeBool(forKey: String) -> Bool](./decodebool%28forkey%29.md)
  Decodes a Boolean value associated with a given key.
- [func decodeBytes(forKey: String, returnedLength: UnsafeMutablePointer<Int>?) -> UnsafePointer<UInt8>?](./decodebytes%28forkey,returnedlength%29.md)
  Decodes a stream of bytes associated with a given key.
- [func decodeDouble(forKey: String) -> Double](./decodedouble%28forkey%29.md)
  Decodes a double-precision floating-point value associated with a given key.
- [func decodeFloat(forKey: String) -> Float](./decodefloat%28forkey%29.md)
  Decodes a single-precision floating-point value associated with a given key.
- [func decodeInt32(forKey: String) -> Int32](./decodeint32%28forkey%29.md)
  Decodes a 32-bit integer value associated with a given key.
- [func decodeInt64(forKey: String) -> Int64](./decodeint64%28forkey%29.md)
  Decodes a 64-bit integer value associated with a given key.
- [func finishDecoding()](./finishdecoding%28%29.md)
  Tells the receiver that you are finished decoding objects.
- [var decodingFailurePolicy: NSCoder.DecodingFailurePolicy](./decodingfailurepolicy.md)
  The action to take when this unarchiver fails to decode an entry.
- [- decodeIntForKey:](./decodeintforkey_.md)
  Decodes an integer value associated with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/decodeobject(forkey:))*