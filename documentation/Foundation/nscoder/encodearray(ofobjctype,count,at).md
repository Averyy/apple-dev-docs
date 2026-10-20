# encodeArray(ofObjCType:count:at:)

**Framework**: Foundation  
**Kind**: method

Encodes an array of the given Objective-C type, provided the number of items and a pointer.

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
func encodeArray(ofObjCType type: UnsafePointer<CChar>, count: Int, at array: UnsafeRawPointer)
```

#### Discussion

The values are encoded from the buffer beginning at `address`. `itemType` must contain exactly one type code. `NSCoder`’s implementation invokes [`encodeValue(ofObjCType:at:)`](nscoder/encodevalue(ofobjctype:at:).md) to encode the entire array of items. Subclasses that implement the [`encodeValue(ofObjCType:at:)`](nscoder/encodevalue(ofobjctype:at:).md) method do not need to override this method.

This method must be matched by a subsequent [`decodeArray(ofObjCType:count:at:)`](nscoder/decodearray(ofobjctype:count:at:).md) message.

For information on creating an Objective-C type code suitable for `itemType`, see [`Type Encodings`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100).

##### Special Considerations

You should not use this method to encode C arrays of Objective-C objects. See [`decodeArray(ofObjCType:count:at:)`](nscoder/decodearray(ofobjctype:count:at:).md) for more details.

## See Also

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
- [func encode(Any?)](nscoder/encode(_:)-9648d.md)
  Encodes an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/encodearray(ofobjctype:count:at:))*