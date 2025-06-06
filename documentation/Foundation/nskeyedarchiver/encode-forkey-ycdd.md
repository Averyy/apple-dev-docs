# encode(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Encodes a given 64-bit integer value and associates it with a key.

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
func encode(_ value: Int64, forKey key: String)
```

## Parameters

- `value`: The value to encode.
- `key`: The key with which to associate  . This value must not be  .

## See Also

- [func decodeInt64(forKey: String) -> Int64](nskeyedunarchiver/decodeint64(forkey:).md)
  Decodes a 64-bit integer value associated with a given key.
- [func encodeEncodable<T>(T, forKey: String) throws](nskeyedarchiver/encodeencodable(_:forkey:).md)
  Encodes a given value and associates it with a key.
- [func encode(Bool, forKey: String)](nskeyedarchiver/encode(_:forkey:)-9pxhm.md)
  Encodes a given Boolean value and associates it with a key.
- [func encodeBytes(UnsafePointer<UInt8>?, length: Int, forKey: String)](nskeyedarchiver/encodebytes(_:length:forkey:).md)
  Encodes a given number of bytes from a given C array of bytes and associates them with a key.
- [func encodeConditionalObject(Any?, forKey: String)](nskeyedarchiver/encodeconditionalobject(_:forkey:).md)
  Encodes a reference to a given object and associates it with a key only if it has been unconditionally encoded elsewhere in the archive.
- [func encode(Double, forKey: String)](nskeyedarchiver/encode(_:forkey:)-1mkfl.md)
  Encodes a given `double` value and associates it with a key.
- [func encode(Float, forKey: String)](nskeyedarchiver/encode(_:forkey:)-67rcs.md)
  Encodes a given `float` value and associates it with a key.
- [func encode(Int32, forKey: String)](nskeyedarchiver/encode(_:forkey:)-5i7tc.md)
  Encodes a given 32-bit integer value and associates it with a key.
- [func encode(Any?, forKey: String)](nskeyedarchiver/encode(_:forkey:)-9f4n9.md)
  Encodes a given object and associates it with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/encode(_:forkey:)-ycdd)*