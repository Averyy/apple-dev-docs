# encodeBytes(_:length:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Encodes a given number of bytes from a given C array of bytes and associates them with a key.

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
func encodeBytes(_ bytes: UnsafePointer<UInt8>?, length: Int, forKey key: String)
```

```objc
- (void) encodeBytes:(const uint8_t *) bytes length:(NSUInteger) length forKey:(NSString *) key;
```

## Parameters

- `bytes`: A C array of bytes to encode.
- `length`: The number of bytes from `bytesp` to encode.
- `key`: The key with which to associate the encoded value. This value must not be `nil`.

## See Also

### Related Documentation
- [func decodeBytes(forKey: String, returnedLength: UnsafeMutablePointer<Int>?) -> UnsafePointer<UInt8>?](../nskeyedunarchiver/decodebytes%28forkey,returnedlength%29.md)
  Decodes a stream of bytes associated with a given key.
### Encoding Data and Objects
- [func encodeEncodable<T>(T, forKey: String) throws](./encodeencodable%28_,forkey%29.md)
  Encodes a given value and associates it with a key.
- [func encode(Bool, forKey: String)](./encode%28_,forkey%29-9pxhm.md)
  Encodes a given Boolean value and associates it with a key.
- [func encodeConditionalObject(Any?, forKey: String)](./encodeconditionalobject%28_,forkey%29.md)
  Encodes a reference to a given object and associates it with a key only if it has been unconditionally encoded elsewhere in the archive.
- [func encode(Double, forKey: String)](./encode%28_,forkey%29-1mkfl.md)
  Encodes a given `double` value and associates it with a key.
- [func encode(Float, forKey: String)](./encode%28_,forkey%29-67rcs.md)
  Encodes a given `float` value and associates it with a key.
- [func encode(Int32, forKey: String)](./encode%28_,forkey%29-5i7tc.md)
  Encodes a given 32-bit integer value and associates it with a key.
- [func encode(Int64, forKey: String)](./encode%28_,forkey%29-ycdd.md)
  Encodes a given 64-bit integer value and associates it with a key.
- [func encode(Any?, forKey: String)](./encode%28_,forkey%29-9f4n9.md)
  Encodes a given object and associates it with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/encodebytes(_:length:forkey:))*