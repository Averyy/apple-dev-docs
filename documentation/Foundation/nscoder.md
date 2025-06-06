# NSCoder

**Framework**: Foundation  
**Kind**: class

An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.

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
class NSCoder
```

#### Overview

[`NSCoder`](nscoder.md) declares the interface used by concrete subclasses to transfer objects and other values between memory and some other format. This capability provides the basis for archiving (storing objects and data on disk) and distribution (copying objects and data items between different processes or threads). The concrete subclasses provided by Foundation for these purposes are [`NSArchiver`](nsarchiver.md), [`NSUnarchiver`](nsunarchiver.md), [`NSKeyedArchiver`](nskeyedarchiver.md), [`NSKeyedUnarchiver`](nskeyedunarchiver.md), and [`NSPortCoder`](nsportcoder.md). Concrete subclasses of [`NSCoder`](nscoder.md) are “coder classes”, and instances of these classes are “coder objects” (or simply “coders”). A coder that can only encode values is an “encoder”, and one that can only decode values is a “decoder”.

[`NSCoder`](nscoder.md) operates on objects, scalars, C arrays, structures, strings, and on pointers to these types. It doesn’t handle types whose implementation varies across platforms, such as `union`, `void *`, function pointers, and long chains of pointers. A coder stores object type information along with the data, so an object decoded from a stream of bytes is normally of the same class as the object that was originally encoded into the stream. An object can change its class when encoded, however; this is described in [`Archives and Serializations Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

The AVFoundation framework adds methods to the [`NSCoder`](nscoder.md) class to make it easier to create archives including Core Media time structures, and extract Core Media time structure from archives.

##### Subclassing Notes

For details of how to create a subclass of `NSCoder`, see [`Subclassing NSCoder`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/subclassing.html#//apple_ref/doc/uid/20000951) in [`Archives and Serializations Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

## Topics

### Inspecting a Coder
- [var allowsKeyedCoding: Bool](nscoder/allowskeyedcoding.md)
  A Boolean value that indicates whether the receiver supports keyed coding of objects.
- [func containsValue(forKey: String) -> Bool](nscoder/containsvalue(forkey:).md)
  Returns a Boolean value that indicates whether an encoded value is available for a string.
- [var decodingFailurePolicy: NSCoder.DecodingFailurePolicy](nscoder/decodingfailurepolicy-swift.property.md)
  The action the coder should take when decoding fails.
- [NSCoder.DecodingFailurePolicy](nscoder/decodingfailurepolicy-swift.enum.md)
  Policies describing the action the coder should take when encountering decode failures.
### Encoding General Data
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
- [func encode(Any?)](nscoder/encode(_:)-9648d.md)
  Encodes an object.
- [func encode(Any?, forKey: String)](nscoder/encode(_:forkey:)-1mlmu.md)
  Encodes an object and associates it with the string key.
- [func encode(NSPoint)](nscoder/encode(_:)-75jv4.md)
  Encodes a point.
- [func encode(NSPoint, forKey: String)](nscoder/encode(_:forkey:)-27lif.md)
  Encodes a point and associates it with the string key.
- [func encodePropertyList(Any)](nscoder/encodepropertylist(_:).md)
  Encodes a property list.
- [func encode(NSRect)](nscoder/encode(_:)-3c1wz.md)
  Encodes a rectangle structure.
- [func encode(NSRect, forKey: String)](nscoder/encode(_:forkey:)-2knxx.md)
  Encodes a rectangle structure and associates it with the string key.
- [func encodeRootObject(Any)](nscoder/encoderootobject(_:).md)
  An encoding method for subclasses to override to encode an interconnected group of objects, starting with the provided root object.
- [func encode(NSSize)](nscoder/encode(_:)-82i7c.md)
  Encodes a size structure.
- [func encode(NSSize, forKey: String)](nscoder/encode(_:forkey:)-9imtu.md)
  Encodes a size structure and associates it with the given string key.
- [func encodeValue(ofObjCType: UnsafePointer<CChar>, at: UnsafeRawPointer)](nscoder/encodevalue(ofobjctype:at:).md)
  Encodes a value of the given type at the given address.
### Encoding Geometry-Based Data
- [func encode(CGAffineTransform, forKey: String)](nscoder/encode(_:forkey:)-29jyx.md)
  Encodes an affine transform and associates it with the specified key in the receiver’s archive.
- [func encode(CGPoint, forKey: String)](nscoder/encode(_:forkey:)-7z9kc.md)
  Encodes a point and associates it with the specified key in the receiver’s archive.
- [func encode(CGRect, forKey: String)](nscoder/encode(_:forkey:)-10qhm.md)
  Encodes a rectangle and associates it with the specified key in the receiver’s archive.
- [func encode(CGSize, forKey: String)](nscoder/encode(_:forkey:)-6wq3n.md)
  Encodes size information and associates it with the specified key in the coder’s archive.
- [func encode(CGVector, forKey: String)](nscoder/encode(_:forkey:)-26fxa.md)
  Encodes vector data and associates it with the specified key in the coder’s archive.
- [func encode(NSDirectionalEdgeInsets, forKey: String)](nscoder/encode(_:forkey:)-7oo2n.md)
  Encodes directional edge inset data and associates it with the specified key in the coder’s archive.
- [func encode(UIEdgeInsets, forKey: String)](nscoder/encode(_:forkey:)-44zsc.md)
  Encodes edge inset data and associates it with the specified key in the coder’s archive.
- [func encode(UIOffset, forKey: String)](nscoder/encode(_:forkey:)-9d1qy.md)
  Encodes offset data and associates it with the specified key in the coder’s archive.
### Encoding Core Media Time Structures
- [func encode(CMTime, forKey: String)](nscoder/encode(_:forkey:)-6wbby.md)
  Encodes a given Core Media time structure and associates it with a specified key.
- [func encode(CMTimeRange, forKey: String)](nscoder/encode(_:forkey:)-46lo8.md)
  Encodes a given Core Media time range structure and associates it with a specified key.
- [func encode(CMTimeMapping, forKey: String)](nscoder/encode(_:forkey:)-8tefb.md)
  Encodes a given Core Media time mapping structure and associates it with a specified key.
### Secure Coding
- [var requiresSecureCoding: Bool](nscoder/requiressecurecoding.md)
  Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [var allowedClasses: Set<AnyHashable>?](nscoder/allowedclasses.md)
  The set of coded classes allowed for secure coding.
### Decoding Top-Level Objects
- [func decodeObject<DecodedObjectType>(of: DecodedObjectType.Type, forKey: String) -> DecodedObjectType?](nscoder/decodeobject(of:forkey:)-7tmft.md)
  Decode an object as an expected type, failing if the archived type doesn’t match.
- [func decodeObject(of: [AnyClass]?, forKey: String) -> Any?](nscoder/decodeobject(of:forkey:)-roif.md)
  Decode an object as one of several expected types, failing if the archived type doesn’t match any of the types.
- [func decodeTopLevelObject() throws -> Any?](nscoder/decodetoplevelobject.md)
  Decodes a previously-encoded object.
- [func decodeTopLevelObject(forKey: String) throws -> Any?](nscoder/decodetoplevelobject(forkey:)-7cram.md)
  Decodes the previously-encoded object associated by a key.
- [func decodeTopLevelObject<DecodedObjectType>(of: DecodedObjectType.Type, forKey: String) throws -> DecodedObjectType?](nscoder/decodetoplevelobject(of:forkey:)-3w6pd.md)
  Decode an object as one of several expected types, failing if the archived type does not match.
- [func decodeTopLevelObject(of: [AnyClass]?, forKey: String) throws -> Any?](nscoder/decodetoplevelobject(of:forkey:)-5lnnn.md)
  Decode an object as one of several expected types, failing if the archived type does not match.
### Decoding General Data
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
- [func decodeInt64(forKey: String) -> Int64](nscoder/decodeint64(forkey:).md)
  Decodes and returns a 64-bit integer value that was previously encoded with [`encodeCInt(_:forKey:)`](nscoder/encodecint(_:forkey:).md), [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-2dprz.md), [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-5sk4z.md), or [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-dixg.md) and associated with the string `key`.
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
- [func decodeRect() -> NSRect](nscoder/decoderect.md)
  Decodes and returns an NSRect structure that was previously encoded with [`encode(_:)`](nscoder/encode(_:)-3c1wz.md).
- [func decodeRect(forKey: String) -> NSRect](nscoder/decoderect(forkey:).md)
  Decodes and returns an NSRect structure that was previously encoded with [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-2knxx.md).
- [func decodeSize() -> NSSize](nscoder/decodesize.md)
  Decodes and returns an NSSize structure that was previously encoded with [`encode(_:)`](nscoder/encode(_:)-82i7c.md).
- [func decodeSize(forKey: String) -> NSSize](nscoder/decodesize(forkey:).md)
  Decodes and returns an NSSize structure that was previously encoded with [`encode(_:forKey:)`](nscoder/encode(_:forkey:)-9imtu.md).
- [func decodeValue(ofObjCType: UnsafePointer<CChar>, at: UnsafeMutableRawPointer)](nscoder/decodevalue(ofobjctype:at:).md)
  Decodes a single value, whose Objective-C type is given by `valueType`.
- [func decodeValue(ofObjCType: UnsafePointer<CChar>, at: UnsafeMutableRawPointer, size: Int)](nscoder/decodevalue(ofobjctype:at:size:).md)
  Decodes a single value of a known type from the specified data buffer.
- [func decodePropertyList(forKey: String) -> Any?](nscoder/decodepropertylist(forkey:).md)
  Returns a decoded property list for the specified key.
### Decoding Geometry-Based Data
- [func decodeCGAffineTransform(forKey: String) -> CGAffineTransform](nscoder/decodecgaffinetransform(forkey:).md)
  Decodes and returns the Core Graphics affine transform structure associated with the specified key in the coder’s archive.
- [func decodeCGPoint(forKey: String) -> CGPoint](nscoder/decodecgpoint(forkey:).md)
  Decodes and returns the Core Graphics point structure associated with the specified key in the coder’s archive.
- [func decodeCGRect(forKey: String) -> CGRect](nscoder/decodecgrect(forkey:).md)
  Decodes and returns the Core Graphics rectangle structure associated with the specified key in the coder’s archive.
- [func decodeCGSize(forKey: String) -> CGSize](nscoder/decodecgsize(forkey:).md)
  Decodes and returns the Core Graphics size structure associated with the specified key in the coder’s archive.
- [func decodeCGVector(forKey: String) -> CGVector](nscoder/decodecgvector(forkey:).md)
  Decodes and returns the Core Graphics vector data associated with the specified key in the coder’s archive.
- [func decodeDirectionalEdgeInsets(forKey: String) -> NSDirectionalEdgeInsets](nscoder/decodedirectionaledgeinsets(forkey:).md)
  Decodes and returns the UIKit directional edge insets structure associated with the specified key in the coder’s archive.
- [func decodeUIEdgeInsets(forKey: String) -> UIEdgeInsets](nscoder/decodeuiedgeinsets(forkey:).md)
  Decodes and returns the UIKit edge insets structure associated with the specified key in the coder’s archive.
- [func decodeUIOffset(forKey: String) -> UIOffset](nscoder/decodeuioffset(forkey:).md)
  Decodes and returns the UIKit offset structure associated with the specified key in the coder’s archive.
### Decoding Core Media Time Structures
- [func decodeTime(forKey: String) -> CMTime](nscoder/decodetime(forkey:).md)
  Returns the Core Media time structure associated with a given key.
- [func decodeTimeRange(forKey: String) -> CMTimeRange](nscoder/decodetimerange(forkey:).md)
  Returns the Core Media time range structure associated with a given key.
- [func decodeTimeMapping(forKey: String) -> CMTimeMapping](nscoder/decodetimemapping(forkey:).md)
  Returns the Core Media time mapping structure associated with a given key.
### Managing Decode Errors
- [func failWithError(any Error)](nscoder/failwitherror(_:).md)
  Signals to this coder that the decode operation has failed.
- [var error: (any Error)?](nscoder/error.md)
  An error in the top-level encode.
### Getting Version Information
- [var systemVersion: UInt32](nscoder/systemversion.md)
  The system version in effect for the archive.
- [func version(forClassName: String) -> Int](nscoder/version(forclassname:).md)
  This method is present for historical reasons and is not used with keyed archivers.
### Representing Geometric Types as Strings
- [class func cgAffineTransform(for: String) -> CGAffineTransform](nscoder/cgaffinetransform(for:).md)
  Returns a Core Graphics affine transform structure corresponding to the data in a given string.
- [class func cgPoint(for: String) -> CGPoint](nscoder/cgpoint(for:).md)
  Returns a Core Graphics point structure corresponding to the data in a given string.
- [class func cgRect(for: String) -> CGRect](nscoder/cgrect(for:).md)
  Returns a Core Graphics rectangle structure corresponding to the data in a given string.
- [class func cgSize(for: String) -> CGSize](nscoder/cgsize(for:).md)
  Returns a Core Graphics size structure corresponding to the data in a given string.
- [class func cgVector(for: String) -> CGVector](nscoder/cgvector(for:).md)
  Returns a Core Graphics vector corresponding to the data in a given string.
- [class func nsDirectionalEdgeInsets(for: String) -> NSDirectionalEdgeInsets](nscoder/nsdirectionaledgeinsets(for:).md)
  Returns a directional edge insets structure based on data in the specified string.
- [class func uiEdgeInsets(for: String) -> UIEdgeInsets](nscoder/uiedgeinsets(for:).md)
  Returns a UIKit edge insets structure based on the data in the specified string.
- [class func uiOffset(for: String) -> UIOffset](nscoder/uioffset(for:).md)
  Returns a UIKit offset structure corresponding to the data in a given string.
- [class func string(for: CGRect) -> String](nscoder/string(for:)-4qz0a.md)
  Returns a string formatted to contain the data from a rectangle.
- [class func string(for: CGVector) -> String](nscoder/string(for:)-4omzv.md)
  Returns a string formatted to contain the data from a vector data structure.
- [class func string(for: CGAffineTransform) -> String](nscoder/string(for:)-6yx6n.md)
  Returns a string formatted to contain the data from an affine transform.
- [class func string(for: CGPoint) -> String](nscoder/string(for:)-6ix86.md)
  Returns a string formatted to contain the data from a point.
- [class func string(for: CGSize) -> String](nscoder/string(for:)-2f1xb.md)
  Returns a string formatted to contain the data from a size data structure.
- [class func string(for: NSDirectionalEdgeInsets) -> String](nscoder/string(for:)-hp8b.md)
  Returns a string formatted to contain the data from a directional edge insets structure.
- [class func string(for: UIEdgeInsets) -> String](nscoder/string(for:)-26b4z.md)
  Returns a string formatted to contain the data from an edge insets structure.
- [class func string(for: UIOffset) -> String](nscoder/string(for:)-454dj.md)
  Returns a string formatted to contain the data from an offset structure.
### Error Codes
- [var NSCoderErrorMaximum: Int](nscodererrormaximum-swift.var.md)
  The end of the range of error codes reserved for coder errors.
- [var NSCoderErrorMinimum: Int](nscodererrorminimum-swift.var.md)
  The start of the range of error codes reserved for coder errors.
- [var NSCoderReadCorruptError: Int](nscoderreadcorrupterror-swift.var.md)
  Decoding failed due to corrupt data.
- [var NSCoderValueNotFoundError: Int](nscodervaluenotfounderror-swift.var.md)
  The requested data wasn’t found.
- [var NSCoderInvalidValueError: Int](nscoderinvalidvalueerror-swift.var.md)
  Data wasn’t valid to encode.
### Instance Methods
- [func decodeArrayOfObjects<DecodedObject>(ofClass: DecodedObject.Type, forKey: String) -> [DecodedObject]?](nscoder/decodearrayofobjects(ofclass:forkey:).md)
- [func decodeArrayOfObjects(ofClasses: [AnyClass], forKey: String) -> [Any]?](nscoder/decodearrayofobjects(ofclasses:forkey:).md)
- [func decodeBytes(forKey: String, minimumLength: Int) -> UnsafePointer<UInt8>?](nscoder/decodebytes(forkey:minimumlength:).md)
  Decode bytes from the decoder for a given key. The length of the bytes must be greater than or equal to the `length` parameter. If the result exists, but is of insufficient length, then the decoder uses `failWithError` to fail the entire decode operation. The result of that is configurable on a per-NSCoder basis using `NSDecodingFailurePolicy`.
- [func decodeBytes(withMinimumLength: Int) -> UnsafeMutableRawPointer?](nscoder/decodebytes(withminimumlength:).md)
  Decode bytes from the decoder. The length of the bytes must be greater than or equal to the `length` parameter. If the result exists, but is of insufficient length, then the decoder uses `failWithError` to fail the entire decode operation. The result of that is configurable on a per-NSCoder basis using `NSDecodingFailurePolicy`.
- [func decodeDictionary<DecodedKey, DecodedObject>(withKeyClass: DecodedKey.Type, objectClass: DecodedObject.Type, forKey: String) -> [DecodedKey : DecodedObject]?](nscoder/decodedictionary(withkeyclass:objectclass:forkey:).md)
- [func decodeDictionary(withKeysOfClasses: [AnyClass], objectsOfClasses: [AnyClass], forKey: String) -> [AnyHashable : Any]?](nscoder/decodedictionary(withkeysofclasses:objectsofclasses:forkey:).md)
- [func decodeTopLevelObject(forKey: String) throws -> AnyObject?](nscoder/decodetoplevelobject(forkey:)-22smg.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSArchiver](nsarchiver.md)
- [NSKeyedArchiver](nskeyedarchiver.md)
- [NSKeyedUnarchiver](nskeyedunarchiver.md)
- [NSUnarchiver](nsunarchiver.md)
- [NSXPCCoder](nsxpccoder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSKeyedArchiver](nskeyedarchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [protocol NSKeyedArchiverDelegate](nskeyedarchiverdelegate.md)
  The optional methods implemented by the delegate of a keyed archiver.
- [class NSKeyedUnarchiver](nskeyedunarchiver.md)
  A decoder that restores data from an archive referenced by keys.
- [protocol NSKeyedUnarchiverDelegate](nskeyedunarchiverdelegate.md)
  The optional methods implemented by the delegate of a keyed unarchiver.
- [class NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md)
  A value transformer that converts data to and from classes that support secure coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder)*