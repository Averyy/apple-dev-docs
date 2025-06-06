# encode(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Encodes an object and associates it with the string key.

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
func encode(_ object: Any?, forKey key: String)
```

#### Discussion

Subclasses must override this method to identify multiple encodings of `objv` and encode a reference to `objv` instead. For example, `NSKeyedArchiver` detects duplicate objects and encodes a reference to the original object rather than encode the same object twice.

## See Also

- [func decodeObject(forKey: String) -> Any?](nscoder/decodeobject(forkey:).md)
  Decodes and returns a previously-encoded object that was previously encoded with [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-1mlmu.md) or [`encodeConditionalObject(_:forKey:)`](nscoder/encodeconditionalobject(_:forkey:).md) and associated with the string `key`.
- [func encodeArray(ofObjCType: UnsafePointer<CChar>, count: Int, at: UnsafeRawPointer)](nscoder/encodearray(ofobjctype:count:at:).md)
  Encodes an array of the given Objective-C type, provided the number of items and a pointer.
- [func encode(Bool, forKey: String)](nscoder/encode(_:forkey:)-7o6mu.md)
  Encodes a Boolean value and associates it with the string `key`.
- [func encodeBycopyObject(Any?)](nscoder/encodebycopyobject(_:).md)
  An encoding method for subclasses to override such that it creates a copy, rather than a proxy, when decoded.
- [func encodeByrefObject(Any?)](nscoder/encodebyrefobject(_:).md)
  An encoding method for subclasses to override such that it creates a proxy, rather than a copy, when decoded.
- [func encodeBytes(UnsafeRawPointer?, length: Int)](nscoder/encodebytes(_:length:).md)
  Encodes a buffer of data of an unspecified type.
- [func encodeBytes(UnsafePointer<UInt8>?, length: Int, forKey: String)](nscoder/encodebytes(_:length:forkey:).md)
  Encodes a buffer of data, given its length and a pointer, and associates it with a string key.
- [func encodeConditionalObject(Any?)](nscoder/encodeconditionalobject(_:).md)
  An encoding method for subclasses to override to conditionally encode an object, preserving common references to it.
- [func encodeConditionalObject(Any?, forKey: String)](nscoder/encodeconditionalobject(_:forkey:).md)
  An encoding method for subclasses to override to conditionally encode an object, preserving common references to it, only if it has been unconditionally encoded.
- [func encode(Data)](nscoder/encode(_:)-1qd1e.md)
  Encodes a given data object.
- [func encode(Double, forKey: String)](nscoder/encode(_:forkey:)-9xiiu.md)
  Encodes a double-precision floating point value and associates it with the string key.
- [func encode(Float, forKey: String)](nscoder/encode(_:forkey:)-84cez.md)
  Encodes a floating point value and associates it with the string key.
- [func encodeCInt(Int32, forKey: String)](nscoder/encodecint(_:forkey:).md)
  Encodes a C integer value and associates it with the string key.
- [func encode(Int, forKey: String)](nscoder/encode(_:forkey:)-2dprz.md)
  Encodes an integer value and associates it with the string key.
- [func encode(Int32, forKey: String)](nscoder/encode(_:forkey:)-5sk4z.md)
  Encodes a 32-bit integer value and associates it with the string key.
- [func encode(Int64, forKey: String)](nscoder/encode(_:forkey:)-dixg.md)
  Encodes a 64-bit integer value and associates it with the string key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/encode(_:forkey:)-1mlmu)*