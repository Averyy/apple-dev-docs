# decodeObjectOfClasses:forKey:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Decodes an object for the key, restricted to the specified classes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (id) decodeObjectOfClasses:(NSSet<Class> *) classes forKey:(NSString *) key;
```

#### Return Value

The decoded object.

#### Discussion

The class of the object may be any class in the `classes` set, or a subclass of any class in the set. Otherwise, the behavior is the same as [`decodeObjectOfClass:forKey:`](./decodeobjectofclass_forkey_.md).

## Parameters

- `classes`: A set of the expected classes.
- `key`: The coder key.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodeobjectofclasses:forkey:)*