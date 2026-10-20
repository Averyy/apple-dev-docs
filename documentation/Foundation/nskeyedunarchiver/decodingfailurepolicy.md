# decodingFailurePolicy

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readwrite) NSDecodingFailurePolicy decodingFailurePolicy;
```

#### Discussion

The unarchiver may fail to decode an entry for the following reasons:

- The keyed archive data is corrupt or missing.
- A type mismatch occurs, such as expecting a class by calling [`decodeObject(of:forKey:)`](../nscoder/decodeobject%28of,forkey%29-7tmft.md), but the unarchiver encounters a numeric value for that key instead. This also occurs when [`decodeIntForKey:`](./decodeintforkey_.md) encounters a value encoded as floating-point, or vice versa.
- A secure coding violation occurs. This happens when attempting to decode an object that doesn’t conform to [`NSSecureCoding`](../nssecurecoding.md). This also happens when the encoded type doesn’t match any of the classes passed to [`unarchivedObject(ofClasses:from:)`](./unarchivedobject%28ofclasses,from%29-b9t5.md).

## See Also

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
- [func decodeObject(forKey: String) -> Any?](./decodeobject%28forkey%29.md)
  Decodes and returns an object associated with a given key.
- [func finishDecoding()](./finishdecoding%28%29.md)
  Tells the receiver that you are finished decoding objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/decodingfailurepolicy)*