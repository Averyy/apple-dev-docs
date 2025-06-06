# decodeInt64(forKey:)

**Framework**: Foundation  
**Kind**: method

Decodes and returns a 64-bit integer value that was previously encoded with [`encodeCInt(_:forKey:)`](nscoder/encodecint(_:forkey:).md), [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-2dprz.md), [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-5sk4z.md), or [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-dixg.md) and associated with the string `key`.

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

#### Discussion

Subclasses must override this method if they perform keyed coding.

## See Also

- [func decodeArray(ofObjCType: UnsafePointer<CChar>, count: Int, at: UnsafeMutableRawPointer)](nscoder/decodearray(ofobjctype:count:at:).md)
  Decodes an array of `count` items, whose Objective-C type is given by `itemType`.
- [func decodeBool(forKey: String) -> Bool](nscoder/decodebool(forkey:).md)
  Decodes and returns a boolean value that was previously encoded with [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-7o6mu.md) and associated with the string `key`.
- [func decodeBytes(forKey: String, returnedLength: UnsafeMutablePointer<Int>?) -> UnsafePointer<UInt8>?](nscoder/decodebytes(forkey:returnedlength:).md)
  Decodes a buffer of data that was previously encoded with [`encodeBytes(_:length:forKey:)`](nscoder/encodebytes(_:length:forkey:).md) and associated with the string `key`.
- [func decodeBytes(withReturnedLength: UnsafeMutablePointer<Int>) -> UnsafeMutableRawPointer?](nscoder/decodebytes(withreturnedlength:).md)
  Decodes a buffer of data whose types are unspecified.
- [func decodeData() -> Data?](nscoder/decodedata.md)
  Decodes and returns an `NSData` object that was previously encoded with [`encode(_:)`](nscoder/encode(_:)-1qd1e.md). Subclasses must override this method.
- [func decodeDouble(forKey: String) -> Double](nscoder/decodedouble(forkey:).md)
  Decodes and returns a double value that was previously encoded with either [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-84cez.md) or [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-9xiiu.md) and associated with the string `key`.
- [func decodeFloat(forKey: String) -> Float](nscoder/decodefloat(forkey:).md)
  Decodes and returns a float value that was previously encoded with [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-84cez.md) or [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-9xiiu.md) and associated with the string `key`.
- [func decodeCInt(forKey: String) -> Int32](nscoder/decodecint(forkey:).md)
  Decodes and returns an int value that was previously encoded with [`encodeCInt(_:forKey:)`](nscoder/encodecint(_:forkey:).md), [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-2dprz.md), [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-5sk4z.md), or [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-dixg.md) and associated with the string `key`.
- [func decodeInteger(forKey: String) -> Int](nscoder/decodeinteger(forkey:).md)
  Decodes and returns an NSInteger value that was previously encoded with [`encodeCInt(_:forKey:)`](nscoder/encodecint(_:forkey:).md), [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-2dprz.md), [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-5sk4z.md), or [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-dixg.md) and associated with the string `key`.
- [func decodeInt32(forKey: String) -> Int32](nscoder/decodeint32(forkey:).md)
  Decodes and returns a 32-bit integer value that was previously encoded with [`encodeCInt(_:forKey:)`](nscoder/encodecint(_:forkey:).md), [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-2dprz.md), [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-5sk4z.md), or [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-dixg.md) and associated with the string `key`.
- [func decodeObject() -> Any?](nscoder/decodeobject.md)
  Decodes and returns an object that was previously encoded with any of the `encode…Object` methods.
- [func decodeObject(forKey: String) -> Any?](nscoder/decodeobject(forkey:).md)
  Decodes and returns a previously-encoded object that was previously encoded with [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-1mlmu.md) or [`encodeConditionalObject(_:forKey:)`](nscoder/encodeconditionalobject(_:forkey:).md) and associated with the string `key`.
- [func decodePoint() -> NSPoint](nscoder/decodepoint.md)
  Decodes and returns an NSPoint structure that was previously encoded with [`encode(_:)`](nscoder/encode(_:)-75jv4.md).
- [func decodePoint(forKey: String) -> NSPoint](nscoder/decodepoint(forkey:).md)
  Decodes and returns an NSPoint structure that was previously encoded with [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-27lif.md).
- [func decodePropertyList() -> Any?](nscoder/decodepropertylist.md)
  Decodes a property list that was previously encoded with [`encodePropertyList(_:)`](nscoder/encodepropertylist(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodeint64(forkey:))*