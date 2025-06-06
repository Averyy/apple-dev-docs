# decodeInt64(forKey:)

**Framework**: Foundation  
**Kind**: method

Decodes a 64-bit integer value associated with a given key.

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
func decodeInt64(forKey key: String) -> Int64
```

#### Return Value

The 64-bit integer value associated with the key `key`. Returns `0` if `key` does not exist.

#### Discussion

If the archived value was encoded with a different size but is still an integer, the type is coerced.

## Parameters

- `key`: A key in the archive within the current decoding scope.   must not be  .

## See Also

- [func encode(Int64, forKey: String)](nskeyedarchiver/encode(_:forkey:)-ycdd.md)
  Encodes a given 64-bit integer value and associates it with a key.
- [func containsValue(forKey: String) -> Bool](nskeyedunarchiver/containsvalue(forkey:).md)
  Returns a Boolean value that indicates whether the archive contains a value for a given key within the current decoding scope.
- [func decodeDecodable<T>(T.Type, forKey: String) -> T?](nskeyedunarchiver/decodedecodable(_:forkey:).md)
  Decodes a decodable value associated with a given key.
- [func decodeTopLevelDecodable<T>(T.Type, forKey: String) throws -> T?](nskeyedunarchiver/decodetopleveldecodable(_:forkey:).md)
  Decodes a top-level decodable value associated with a given key.
- [func decodeBool(forKey: String) -> Bool](nskeyedunarchiver/decodebool(forkey:).md)
  Decodes a Boolean value associated with a given key.
- [func decodeBytes(forKey: String, returnedLength: UnsafeMutablePointer<Int>?) -> UnsafePointer<UInt8>?](nskeyedunarchiver/decodebytes(forkey:returnedlength:).md)
  Decodes a stream of bytes associated with a given key.
- [func decodeDouble(forKey: String) -> Double](nskeyedunarchiver/decodedouble(forkey:).md)
  Decodes a double-precision floating-point value associated with a given key.
- [func decodeFloat(forKey: String) -> Float](nskeyedunarchiver/decodefloat(forkey:).md)
  Decodes a single-precision floating-point value associated with a given key.
- [func decodeInt32(forKey: String) -> Int32](nskeyedunarchiver/decodeint32(forkey:).md)
  Decodes a 32-bit integer value associated with a given key.
- [func decodeObject(forKey: String) -> Any?](nskeyedunarchiver/decodeobject(forkey:).md)
  Decodes and returns an object associated with a given key.
- [func finishDecoding()](nskeyedunarchiver/finishdecoding.md)
  Tells the receiver that you are finished decoding objects.
- [var decodingFailurePolicy: NSCoder.DecodingFailurePolicy](nskeyedunarchiver/decodingfailurepolicy.md)
  The action to take when this unarchiver fails to decode an entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/decodeint64(forkey:))*