# decodeBytes(forKey:returnedLength:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes a stream of bytes associated with a given key.

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
func decodeBytes(forKey key: String, returnedLength lengthp: UnsafeMutablePointer<Int>?) -> UnsafePointer<UInt8>?
```

```objc
- (const uint8_t *) decodeBytesForKey:(NSString *) key returnedLength:(NSUInteger *) lengthp;
```

#### Return Value

The stream of bytes associated with the key `key`. Returns `NULL` if `key` does not exist.

#### Discussion

The returned value is a pointer to a temporary buffer owned by the receiver. The buffer goes away with the unarchiver, not the containing autorelease pool block. You must copy the bytes into your own buffer if you need the data to persist beyond the life of the receiver.

## Parameters

- `key`: A key in the archive within the current decoding scope. `key` must not be `nil`.
- `lengthp`: Upon return, contains the number of bytes returned.

## See Also

### Related Documentation
- [func encodeBytes(UnsafePointer<UInt8>?, length: Int, forKey: String)](../nskeyedarchiver/encodebytes%28_,length,forkey%29.md)
  Encodes a given number of bytes from a given C array of bytes and associates them with a key.
### Decoding Data
- [func containsValue(forKey: String) -> Bool](./containsvalue%28forkey%29.md)
  Returns a Boolean value that indicates whether the archive contains a value for a given key within the current decoding scope.
- [func decodeDecodable<T>(T.Type, forKey: String) -> T?](./decodedecodable%28_,forkey%29.md)
  Decodes a decodable value associated with a given key.
- [func decodeTopLevelDecodable<T>(T.Type, forKey: String) throws -> T?](./decodetopleveldecodable%28_,forkey%29.md)
  Decodes a top-level decodable value associated with a given key.
- [func decodeBool(forKey: String) -> Bool](./decodebool%28forkey%29.md)
  Decodes a Boolean value associated with a given key.
- [func decodeDouble(forKey: String) -> Double](./decodedouble%28forkey%29.md)
  Decodes a double-precision floating-point value associated with a given key.
- [func decodeFloat(forKey: String) -> Float](./decodefloat%28forkey%29.md)
  Decodes a single-precision floating-point value associated with a given key.
- [func decodeInt32(forKey: String) -> Int32](./decodeint32%28forkey%29.md)
  Decodes a 32-bit integer value associated with a given key.
- [func decodeInt64(forKey: String) -> Int64](./decodeint64%28forkey%29.md)
  Decodes a 64-bit integer value associated with a given key.
- [func decodeObject(forKey: String) -> Any?](./decodeobject%28forkey%29.md)
  Decodes and returns an object associated with a given key.
- [func finishDecoding()](./finishdecoding%28%29.md)
  Tells the receiver that you are finished decoding objects.
- [var decodingFailurePolicy: NSCoder.DecodingFailurePolicy](./decodingfailurepolicy.md)
  The action to take when this unarchiver fails to decode an entry.
- [- decodeIntForKey:](./decodeintforkey_.md)
  Decodes an integer value associated with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/decodebytes(forkey:returnedlength:))*