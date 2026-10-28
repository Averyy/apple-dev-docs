# finishDecoding()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the receiver that you are finished decoding objects.

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
func finishDecoding()
```

```objc
- (void) finishDecoding;
```

## Discussion

Invoking this method allows the receiver to notify its delegate and to perform any final operations on the archive. Once this method is invoked, the receiver cannot decode any further values.

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
- [var decodingFailurePolicy: NSCoder.DecodingFailurePolicy](./decodingfailurepolicy.md)
  The action to take when this unarchiver fails to decode an entry.
- [- decodeIntForKey:](./decodeintforkey_.md)
  Decodes an integer value associated with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/finishdecoding())*