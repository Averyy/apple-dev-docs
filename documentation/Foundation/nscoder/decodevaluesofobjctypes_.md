# decodeValuesOfObjCTypes:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes a series of potentially different Objective-C types.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (void) decodeValuesOfObjCTypes:(const char *) types;
```

#### Discussion

`valueTypes` is a single C string containing any number of type codes. The variable arguments to this method consist of one or more pointer arguments, each of which specifies the buffer in which to place a single decoded value. For each type code in `valueTypes`, you must specify a corresponding pointer argument whose buffer is large enough to hold the decoded value.

This method matches an [`encodeValuesOfObjCTypes:`](./encodevaluesofobjctypes_.md) message used during encoding.

`NSCoder`’s implementation invokes [`decodeValue(ofObjCType:at:)`](./decodevalue%28ofobjctype,at%29.md) to decode individual types. Subclasses that implement the [`decodeValue(ofObjCType:at:)`](./decodevalue%28ofobjctype,at%29.md) method do not need to override this method.

For information on creating Objective-C type codes suitable for `valueTypes`, see [Type Encodings](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100).

##### Special Considerations

You should not use this method to decode Objective-C objects. See [`decodeArray(ofObjCType:count:at:)`](./decodearray%28ofobjctype,count,at%29.md) for more details.

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
- [- decodeNXObject](./decodenxobject.md)
  Decodes an object previously written with [`encodeNXObject:`](./encodenxobject_.md).
- [func decodeObject() -> Any?](./decodeobject%28%29.md)
  Decodes and returns an object that was previously encoded with any of the `encode…Object` methods.
- [func decodeObject(forKey: String) -> Any?](./decodeobject%28forkey%29.md)
  Decodes and returns a previously-encoded object that was previously encoded with [`encode(_:forKey:)`](./encode%28_,forkey%29-1mlmu.md) or [`encodeConditionalObject(_:forKey:)`](./encodeconditionalobject%28_,forkey%29.md) and associated with the string `key`.
- [func decodePoint() -> NSPoint](./decodepoint%28%29.md)
  Decodes and returns an NSPoint structure that was previously encoded with [`encode(_:)`](./encode%28_%29-75jv4.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodevaluesofobjctypes:)*