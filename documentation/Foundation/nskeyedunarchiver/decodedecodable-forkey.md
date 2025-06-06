# decodeDecodable(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Decodes a decodable value associated with a given key.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@nonobjc
func decodeDecodable<T>(_ type: T.Type, forKey key: String) -> T? where T : Decodable
```

## Parameters

- `type`: The type of the value to decode.
- `key`: The key in the archive associated with the value to decode.

## See Also

- [func containsValue(forKey: String) -> Bool](nskeyedunarchiver/containsvalue(forkey:).md)
  Returns a Boolean value that indicates whether the archive contains a value for a given key within the current decoding scope.
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
- [func decodeInt64(forKey: String) -> Int64](nskeyedunarchiver/decodeint64(forkey:).md)
  Decodes a 64-bit integer value associated with a given key.
- [func decodeObject(forKey: String) -> Any?](nskeyedunarchiver/decodeobject(forkey:).md)
  Decodes and returns an object associated with a given key.
- [func finishDecoding()](nskeyedunarchiver/finishdecoding.md)
  Tells the receiver that you are finished decoding objects.
- [var decodingFailurePolicy: NSCoder.DecodingFailurePolicy](nskeyedunarchiver/decodingfailurepolicy.md)
  The action to take when this unarchiver fails to decode an entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/decodedecodable(_:forkey:))*