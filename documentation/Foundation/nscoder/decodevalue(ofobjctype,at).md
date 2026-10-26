# decodeValue(ofObjCType:at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes a single value, whose Objective-C type is given by `valueType`.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`decodeValue(ofObjCType:at:size:)`](./decodevalue%28ofobjctype,at,size%29.md) instead.

## Declaration

```swift
func decodeValue(ofObjCType type: UnsafePointer<CChar>, at data: UnsafeMutableRawPointer)
```

```objc
- (void) decodeValueOfObjCType:(const char *) type at:(void *) data;
```

#### Discussion

`valueType` must contain exactly one type code, and the buffer specified by `data` must be large enough to hold the value corresponding to that type code. For information on creating an Objective-C type code suitable for `valueType`, see [Type Encodings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100).

Subclasses must override this method and provide an implementation to decode the value. In your overriding implementation, decode the value into the buffer beginning at `data`.

This method matches an [`encodeValue(ofObjCType:at:)`](./encodevalue%28ofobjctype,at%29.md) message used during encoding.

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
### Related Documentation
- [- decodeValuesOfObjCTypes:](./decodevaluesofobjctypes_.md)
  Decodes a series of potentially different Objective-C types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodevalue(ofobjctype:at:))*