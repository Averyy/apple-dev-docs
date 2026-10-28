# encodeNXObject:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Encodes an old-style object onto the coder.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Apple discourages the use of this symbol.

## Declaration

```objc
- (void) encodeNXObject:(id) object;
```

## Discussion

No sharing is done across separate [`encodeNXObject:`](./encodenxobject_.md) invocations. Callers must have implemented an [`encode(with:)`](../nscoding/encode%28with%29.md), which parallels the `write:` methods, on all of their classes that may be touched by this operation.

## See Also

### Encoding General Data
- [func encodeArray(ofObjCType: UnsafePointer<CChar>, count: Int, at: UnsafeRawPointer)](./encodearray%28ofobjctype,count,at%29.md)
  Encodes an array of the given Objective-C type, provided the number of items and a pointer.
- [func encode(Bool, forKey: String)](./encode%28_,forkey%29-7o6mu.md)
  Encodes a Boolean value and associates it with the string `key`.
- [func encodeBycopyObject(Any?)](./encodebycopyobject%28_%29.md)
  An encoding method for subclasses to override such that it creates a copy, rather than a proxy, when decoded.
- [func encodeByrefObject(Any?)](./encodebyrefobject%28_%29.md)
  An encoding method for subclasses to override such that it creates a proxy, rather than a copy, when decoded.
- [func encodeBytes(UnsafeRawPointer?, length: Int)](./encodebytes%28_,length%29.md)
  Encodes a buffer of data of an unspecified type.
- [func encodeBytes(UnsafePointer<UInt8>?, length: Int, forKey: String)](./encodebytes%28_,length,forkey%29.md)
  Encodes a buffer of data, given its length and a pointer, and associates it with a string key.
- [func encodeConditionalObject(Any?)](./encodeconditionalobject%28_%29.md)
  An encoding method for subclasses to override to conditionally encode an object, preserving common references to it.
- [func encodeConditionalObject(Any?, forKey: String)](./encodeconditionalobject%28_,forkey%29.md)
  An encoding method for subclasses to override to conditionally encode an object, preserving common references to it, only if it has been unconditionally encoded.
- [func encode(Data)](./encode%28_%29-1qd1e.md)
  Encodes a given data object.
- [func encode(Double, forKey: String)](./encode%28_,forkey%29-9xiiu.md)
  Encodes a double-precision floating point value and associates it with the string key.
- [func encode(Float, forKey: String)](./encode%28_,forkey%29-84cez.md)
  Encodes a floating point value and associates it with the string key.
- [func encodeCInt(Int32, forKey: String)](./encodecint%28_,forkey%29.md)
  Encodes a C integer value and associates it with the string key.
- [func encode(Int, forKey: String)](./encode%28_,forkey%29-2dprz.md)
  Encodes an integer value and associates it with the string key.
- [func encode(Int32, forKey: String)](./encode%28_,forkey%29-5sk4z.md)
  Encodes a 32-bit integer value and associates it with the string key.
- [func encode(Int64, forKey: String)](./encode%28_,forkey%29-dixg.md)
  Encodes a 64-bit integer value and associates it with the string key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/encodenxobject:)*