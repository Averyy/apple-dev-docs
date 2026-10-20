# encodeBytes(_:length:forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Encodes a buffer of data, given its length and a pointer, and associates it with a string key.

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
func encodeBytes(_ bytes: UnsafePointer<UInt8>?, length: Int, forKey key: String)
```

```objc
- (void) encodeBytes:(const uint8_t *) bytes length:(NSUInteger) length forKey:(NSString *) key;
```

#### Discussion

Subclasses must override this method if they perform keyed coding.

## See Also

### Related Documentation
- [func decodeBytes(forKey: String, returnedLength: UnsafeMutablePointer<Int>?) -> UnsafePointer<UInt8>?](./decodebytes%28forkey,returnedlength%29.md)
  Decodes a buffer of data that was previously encoded with [`encodeBytes(_:length:forKey:)`](./encodebytes%28_,length,forkey%29.md) and associated with the string `key`.
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
- [func encode(Any?)](./encode%28_%29-9648d.md)
  Encodes an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/encodebytes(_:length:forkey:))*