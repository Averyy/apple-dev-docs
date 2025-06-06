# decodingFailurePolicy

**Framework**: Foundation  
**Kind**: property

The action to take when this unarchiver fails to decode an entry.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var decodingFailurePolicy: NSCoder.DecodingFailurePolicy { get set }
```

#### Discussion

The unarchiver may fail to decode an entry for the following reasons:

- The keyed archive data is corrupt or missing.
- A type mismatch occurs, such as expecting a class by calling [`decodeObject(of:forKey:)`](nscoder/decodeobject(of:forkey:)-7tmft.md), but the unarchiver encounters a numeric value for that key instead. This also occurs when [`decodeIntForKey:`](nskeyedunarchiver/decodeintforkey:.md) encounters a value encoded as floating-point, or vice versa.
- A secure coding violation occurs. This happens when attempting to decode an object that doesn’t conform to [`NSSecureCoding`](nssecurecoding.md). This also happens when the encoded type doesn’t match any of the classes passed to [`unarchivedObject(ofClasses:from:)`](nskeyedunarchiver/unarchivedobject(ofclasses:from:)-b9t5.md).

## See Also

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
- [func decodeInt64(forKey: String) -> Int64](nskeyedunarchiver/decodeint64(forkey:).md)
  Decodes a 64-bit integer value associated with a given key.
- [func decodeObject(forKey: String) -> Any?](nskeyedunarchiver/decodeobject(forkey:).md)
  Decodes and returns an object associated with a given key.
- [func finishDecoding()](nskeyedunarchiver/finishdecoding.md)
  Tells the receiver that you are finished decoding objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/decodingfailurepolicy)*