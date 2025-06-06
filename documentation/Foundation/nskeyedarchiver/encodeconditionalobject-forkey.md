# encodeConditionalObject(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Encodes a reference to a given object and associates it with a key only if it has been unconditionally encoded elsewhere in the archive.

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
func encodeConditionalObject(_ object: Any?, forKey key: String)
```

#### Discussion

This method is effective only if you’ve previously archived this object with this key by calling [`encodeInt:forKey:`](nskeyedarchiver/encodeint:forkey:.md).

## Parameters

- `object`: The object to encode.
- `key`: The key with which to associate the encoded value. This value must not be  .

## See Also

- [func encodeEncodable<T>(T, forKey: String) throws](nskeyedarchiver/encodeencodable(_:forkey:).md)
  Encodes a given value and associates it with a key.
- [func encode(Bool, forKey: String)](nskeyedarchiver/encode(_:forkey:)-9pxhm.md)
  Encodes a given Boolean value and associates it with a key.
- [func encodeBytes(UnsafePointer<UInt8>?, length: Int, forKey: String)](nskeyedarchiver/encodebytes(_:length:forkey:).md)
  Encodes a given number of bytes from a given C array of bytes and associates them with a key.
- [func encode(Double, forKey: String)](nskeyedarchiver/encode(_:forkey:)-1mkfl.md)
  Encodes a given `double` value and associates it with a key.
- [func encode(Float, forKey: String)](nskeyedarchiver/encode(_:forkey:)-67rcs.md)
  Encodes a given `float` value and associates it with a key.
- [func encode(Int32, forKey: String)](nskeyedarchiver/encode(_:forkey:)-5i7tc.md)
  Encodes a given 32-bit integer value and associates it with a key.
- [func encode(Int64, forKey: String)](nskeyedarchiver/encode(_:forkey:)-ycdd.md)
  Encodes a given 64-bit integer value and associates it with a key.
- [func encode(Any?, forKey: String)](nskeyedarchiver/encode(_:forkey:)-9f4n9.md)
  Encodes a given object and associates it with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver/encodeconditionalobject(_:forkey:))*