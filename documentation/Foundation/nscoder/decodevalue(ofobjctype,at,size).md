# decodeValue(ofObjCType:at:size:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes a single value of a known type from the specified data buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func decodeValue(ofObjCType type: UnsafePointer<CChar>, at data: UnsafeMutableRawPointer, size: Int)
```

```objc
- (void) decodeValueOfObjCType:(const char *) type at:(void *) data size:(NSUInteger) size;
```

## Discussion

The `type` parameter must contain exactly one type code, and the buffer specified by `data` must be large enough to hold the value corresponding to that type code. For information on creating an Objective-C type code suitable for `type`, see [Type Encodings](../nsmethodsignature.md#Type-Encodings).

Subclasses must override this method and provide an implementation to decode the value. In your overriding implementation, decode the value into the buffer beginning at data.

This method matches an [`encodeValue(ofObjCType:at:)`](./encodevalue%28ofobjctype,at%29.md) message used during encoding.

## Parameters

- `type`: The Objective-C type to decode.
- `data`: The data buffer to decode from.
- `size`: The size of the data buffer.

## See Also

### Decoding General Data
- [func decodeArray(ofObjCType: UnsafePointer<CChar>, count: Int, at: UnsafeMutableRawPointer)](./decodearray%28ofobjctype,count,at%29.md)
  Decodes an array of `count` items, whose Objective-C type is given by `itemType`.
- [func decodeBool(forKey: String) -> Bool](./decodebool%28forkey%29.md)
  Decodes and returns a boolean value that was previously encoded with [`encode(_:forKey:)`](./encode%28_,forkey%29-7o6mu.md) and associated with the string `key`.
- [func decodeBytes(forKey: String, returnedLength: UnsafeMutablePointer<Int>?) -> UnsafePointer<UInt8>?](./decodebytes%28forkey,returnedlength%29.md)
  Decodes a buffer of data that was previously encoded with [`encodeBytes(_:length:forKey:)`](./encodebytes%28_,length,forkey%29.md) and associated with the string `key`.
- [func decodeBytes(withReturnedLength: UnsafeMutablePointer<Int>) -> UnsafeMutableRawPointer?](./decodebytes%28withreturnedlength%29.md)
  Decodes a buffer of data whose types are unspecified.
- [func decodeData() -> Data?](./decodedata%28%29.md)
  Decodes and returns an `NSData` object that was previously encoded with [`encode(_:)`](./encode%28_%29-1qd1e.md). Subclasses must override this method.
- [func decodeDouble(forKey: String) -> Double](./decodedouble%28forkey%29.md)
  Decodes and returns a double value that was previously encoded with either [`encode(_:forKey:)`](./encode%28_,forkey%29-84cez.md) or [`encode(_:forKey:)`](./encode%28_,forkey%29-9xiiu.md) and associated with the string `key`.
- [func decodeFloat(forKey: String) -> Float](./decodefloat%28forkey%29.md)
  Decodes and returns a float value that was previously encoded with [`encode(_:forKey:)`](./encode%28_,forkey%29-84cez.md) or [`encode(_:forKey:)`](./encode%28_,forkey%29-9xiiu.md) and associated with the string `key`.
- [func decodeCInt(forKey: String) -> Int32](./decodecint%28forkey%29.md)
  Decodes and returns an int value that was previously encoded with [`encodeCInt(_:forKey:)`](./encodecint%28_,forkey%29.md), [`encode(_:forKey:)`](./encode%28_,forkey%29-2dprz.md), [`encode(_:forKey:)`](./encode%28_,forkey%29-5sk4z.md), or [`encode(_:forKey:)`](./encode%28_,forkey%29-dixg.md) and associated with the string `key`.
- [func decodeInteger(forKey: String) -> Int](./decodeinteger%28forkey%29.md)
  Decodes and returns an NSInteger value that was previously encoded with [`encodeCInt(_:forKey:)`](./encodecint%28_,forkey%29.md), [`encode(_:forKey:)`](./encode%28_,forkey%29-2dprz.md), [`encode(_:forKey:)`](./encode%28_,forkey%29-5sk4z.md), or [`encode(_:forKey:)`](./encode%28_,forkey%29-dixg.md) and associated with the string `key`.
- [func decodeInt32(forKey: String) -> Int32](./decodeint32%28forkey%29.md)
  Decodes and returns a 32-bit integer value that was previously encoded with [`encodeCInt(_:forKey:)`](./encodecint%28_,forkey%29.md), [`encode(_:forKey:)`](./encode%28_,forkey%29-2dprz.md), [`encode(_:forKey:)`](./encode%28_,forkey%29-5sk4z.md), or [`encode(_:forKey:)`](./encode%28_,forkey%29-dixg.md) and associated with the string `key`.
- [func decodeInt64(forKey: String) -> Int64](./decodeint64%28forkey%29.md)
  Decodes and returns a 64-bit integer value that was previously encoded with [`encodeCInt(_:forKey:)`](./encodecint%28_,forkey%29.md), [`encode(_:forKey:)`](./encode%28_,forkey%29-2dprz.md), [`encode(_:forKey:)`](./encode%28_,forkey%29-5sk4z.md), or [`encode(_:forKey:)`](./encode%28_,forkey%29-dixg.md) and associated with the string `key`.
- [func decodeObject() -> Any?](./decodeobject%28%29.md)
  Decodes and returns an object that was previously encoded with any of the `encode…Object` methods.
- [func decodeObject(forKey: String) -> Any?](./decodeobject%28forkey%29.md)
  Decodes and returns a previously-encoded object that was previously encoded with [`encode(_:forKey:)`](./encode%28_,forkey%29-1mlmu.md) or [`encodeConditionalObject(_:forKey:)`](./encodeconditionalobject%28_,forkey%29.md) and associated with the string `key`.
- [func decodePoint() -> NSPoint](./decodepoint%28%29.md)
  Decodes and returns an NSPoint structure that was previously encoded with [`encode(_:)`](./encode%28_%29-75jv4.md).
- [func decodePoint(forKey: String) -> NSPoint](./decodepoint%28forkey%29.md)
  Decodes and returns an NSPoint structure that was previously encoded with [`encode(_:forKey:)`](./encode%28_,forkey%29-27lif.md).
- [- decodeNXObject](./decodenxobject.md)
  Decodes an object previously written with [`encodeNXObject:`](./encodenxobject_.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodevalue(ofobjctype:at:size:))*