# NSKeyedUnarchiver

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A decoder that restores data from an archive referenced by keys.

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
class NSKeyedUnarchiver
```

```objc
@interface NSKeyedUnarchiver : NSCoder
```

## Overview

[`NSKeyedUnarchiver`](./nskeyedunarchiver.md) is a concrete subclass of [`NSCoder`](./nscoder.md) that defines methods for decoding a set of named objects (and scalar values) from a keyed archive. The [`NSKeyedArchiver`](./nskeyedarchiver.md) class produces archives that this class can decode.

The archiver creates keyed archive as a hierarchy of objects. The archiver treats each object as a namespace into which it can encode other objects. This means that an unarchiver can only decode objects encoded within the immediate scope of their parent object. Objects encoded elsewhere in the hierarchy — whether higher than, lower than, or parallel to this particular object — aren’t accessible. In this way, the keys used by a particular object to encode its instance variables need to be unique only within the scope of that object.

If you invoke one of the `decode`-prefixed methods of this class using a key that does not exist in the archive, the return value indicates failure. This value varies by decoded type. For example, if a key does not exist in an archive, [`decodeBool(forKey:)`](./nskeyedunarchiver/decodebool%28forkey%29.md) returns [`false`](../Swift/false.md), [`decodeIntForKey:`](./nskeyedunarchiver/decodeintforkey_.md) returns `0`, and [`decodeObject(forKey:)`](./nskeyedunarchiver/decodeobject%28forkey%29.md) returns `nil`.

[`NSKeyedUnarchiver`](./nskeyedunarchiver.md) supports limited type coercion for numeric types. You can use any of the integer decode methods to decode a value encoded as any type of integer, whether a standard `Int` or an explicit 32-bit or 64-bit integer. Likewise, you can use the `Float`- or `Double`-returning decode methods to handle value encoded as a `Float` or `Double`. If an encoded value is too large to fit within the coerced type, the decoding method throws a [`rangeException`](./nsexceptionname/rangeexception.md). Further, when trying to coerce a value to an incompatible type — for example decoding an `Int` as a `Float` — the decoding method throws an [`invalidUnarchiveOperationException`](./nsexceptionname/invalidunarchiveoperationexception.md).

## Topics

### Creating a Keyed Unarchiver
- [init(forReadingFrom: Data) throws](./nskeyedunarchiver/init%28forreadingfrom%29.md)
  Initializes an archiver to decode data from the specified location.
- [init()](./nskeyedunarchiver/init%28%29.md)
  Initializes an archiver to decode data.
- [init(forReadingWith: Data)](./nskeyedunarchiver/init%28forreadingwith%29.md)
  Initializes an archiver to decode data from the specified location.
### Unarchiving Data
- [class func unarchiveTopLevelObjectWithData(Data) throws -> Any?](./nskeyedunarchiver/unarchivetoplevelobjectwithdata%28_%29.md)
  Decodes a previously-archived object graph, and returns the root object.
- [static func unarchivedObject<DecodedObjectType>(ofClass: DecodedObjectType.Type, from: Data) throws -> DecodedObjectType?](./nskeyedunarchiver/unarchivedobject%28ofclass,from%29.md)
  Decodes a previously-archived object graph, and returns the root object as the specified type.
- [class func unarchivedObject(ofClasses: Set<AnyHashable>, from: Data) throws -> Any](./nskeyedunarchiver/unarchivedobject%28ofclasses,from%29-b9t5.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [static func unarchivedObject(ofClasses: [AnyClass], from: Data) throws -> Any?](./nskeyedunarchiver/unarchivedobject%28ofclasses,from%29-3h32t.md)
  Decodes a previously-archived object graph, returning the root object as one of the specified classes.
- [var requiresSecureCoding: Bool](./nskeyedunarchiver/requiressecurecoding.md)
  Indicates whether the receiver requires all unarchived classes to conform to [`NSSecureCoding`](./nssecurecoding.md).
- [class func unarchiveObject(with: Data) -> Any?](./nskeyedunarchiver/unarchiveobject%28with%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` and stored in a given `NSData` object.
- [class func unarchiveObject(withFile: String) -> Any?](./nskeyedunarchiver/unarchiveobject%28withfile%29.md)
  Decodes and returns the object graph previously encoded by `NSKeyedArchiver` written to the file at a given path.
- [+ unarchivedObjectOfClass:fromData:error:](./nskeyedunarchiver/unarchivedobjectofclass_fromdata_error_.md)
  Decodes a previously-archived object graph, that returns the root object as the specified type.
- [+ unarchiveTopLevelObjectWithData:error:](./nskeyedunarchiver/unarchivetoplevelobjectwithdata_error_.md)
  Decodes a previously-archived object graph, returning the root object.
### Decoding Data
- [func containsValue(forKey: String) -> Bool](./nskeyedunarchiver/containsvalue%28forkey%29.md)
  Returns a Boolean value that indicates whether the archive contains a value for a given key within the current decoding scope.
- [func decodeDecodable<T>(T.Type, forKey: String) -> T?](./nskeyedunarchiver/decodedecodable%28_,forkey%29.md)
  Decodes a decodable value associated with a given key.
- [func decodeTopLevelDecodable<T>(T.Type, forKey: String) throws -> T?](./nskeyedunarchiver/decodetopleveldecodable%28_,forkey%29.md)
  Decodes a top-level decodable value associated with a given key.
- [func decodeBool(forKey: String) -> Bool](./nskeyedunarchiver/decodebool%28forkey%29.md)
  Decodes a Boolean value associated with a given key.
- [func decodeBytes(forKey: String, returnedLength: UnsafeMutablePointer<Int>?) -> UnsafePointer<UInt8>?](./nskeyedunarchiver/decodebytes%28forkey,returnedlength%29.md)
  Decodes a stream of bytes associated with a given key.
- [func decodeDouble(forKey: String) -> Double](./nskeyedunarchiver/decodedouble%28forkey%29.md)
  Decodes a double-precision floating-point value associated with a given key.
- [func decodeFloat(forKey: String) -> Float](./nskeyedunarchiver/decodefloat%28forkey%29.md)
  Decodes a single-precision floating-point value associated with a given key.
- [func decodeInt32(forKey: String) -> Int32](./nskeyedunarchiver/decodeint32%28forkey%29.md)
  Decodes a 32-bit integer value associated with a given key.
- [func decodeInt64(forKey: String) -> Int64](./nskeyedunarchiver/decodeint64%28forkey%29.md)
  Decodes a 64-bit integer value associated with a given key.
- [func decodeObject(forKey: String) -> Any?](./nskeyedunarchiver/decodeobject%28forkey%29.md)
  Decodes and returns an object associated with a given key.
- [func finishDecoding()](./nskeyedunarchiver/finishdecoding%28%29.md)
  Tells the receiver that you are finished decoding objects.
- [var decodingFailurePolicy: NSCoder.DecodingFailurePolicy](./nskeyedunarchiver/decodingfailurepolicy.md)
  The action to take when this unarchiver fails to decode an entry.
- [- decodeIntForKey:](./nskeyedunarchiver/decodeintforkey_.md)
  Decodes an integer value associated with a given key.
### Managing the Delegate
- [var delegate: (any NSKeyedUnarchiverDelegate)?](./nskeyedunarchiver/delegate.md)
  The receiver’s delegate.
### Managing Class Names
- [class func setClass(AnyClass?, forClassName: String)](./nskeyedunarchiver/setclass%28_,forclassname%29-swift.type.method.md)
  Sets a global translation mapping to decode objects encoded with a given class name as instances of a given class instead.
- [class func `class`(forClassName: String) -> AnyClass?](./nskeyedunarchiver/class%28forclassname%29-swift.type.method.md)
  Returns the class from which this unarchiver instantiates an encoded object with a given class name.
- [func setClass(AnyClass?, forClassName: String)](./nskeyedunarchiver/setclass%28_,forclassname%29-swift.method.md)
  Sets a translation mapping on this unarchiver to decode objects encoded with a given class name as instances of a given class instead.
- [func `class`(forClassName: String) -> AnyClass?](./nskeyedunarchiver/class%28forclassname%29-swift.method.md)
  Returns the class from which this unarchiver instantiates an encoded object with a given class name.
### Constants
- [Keyed Unarchiving Exception Names](./keyed-unarchiving-exception-names.md)
  Names of exceptions that are raised by `NSKeyedUnarchiver` if there is a problem extracting an archive.
### Initializers
- [init(forReadingFromData: Data) throws](./nskeyedunarchiver/init%28forreadingfromdata%29.md)
- [init(forReadingWithData: Data)](./nskeyedunarchiver/init%28forreadingwithdata%29.md)
### Type Methods
- [static func unarchivedArrayOfObjects<DecodedObject>(ofClass: DecodedObject.Type, from: Data) throws -> [DecodedObject]?](./nskeyedunarchiver/unarchivedarrayofobjects%28ofclass,from%29.md)
- [static func unarchivedArrayOfObjects(ofClasses: [AnyClass], from: Data) throws -> [Any]?](./nskeyedunarchiver/unarchivedarrayofobjects%28ofclasses,from%29.md)
- [static func unarchivedDictionary(keysOfClasses: [AnyClass], objectsOfClasses: [AnyClass], from: Data) throws -> [AnyHashable : Any]?](./nskeyedunarchiver/unarchiveddictionary%28keysofclasses,objectsofclasses,from%29.md)
- [static func unarchivedDictionary<DecodedKey, DecodedObject>(ofKeyClass: DecodedKey.Type, objectClass: DecodedObject.Type, from: Data) throws -> [DecodedKey : DecodedObject]?](./nskeyedunarchiver/unarchiveddictionary%28ofkeyclass,objectclass,from%29.md)
- [+ unarchivedArrayOfObjectsOfClass:fromData:error:](./nskeyedunarchiver/unarchivedarrayofobjectsofclass_fromdata_error_.md)
  Decodes the \c NSArray root object from \c data which should be an \c NSArray containing the given non-collection class (no nested arrays or arrays of dictionaries, etc) from the given archive, previously encoded by \c NSKeyedArchiver.
- [+ unarchivedArrayOfObjectsOfClasses:fromData:error:](./nskeyedunarchiver/unarchivedarrayofobjectsofclasses_fromdata_error_.md)
  Decodes the \c NSArray root object from \c data which should be an \c NSArray, containing the given non-collection classes in \c classes  (no nested arrays or arrays of dictionaries, etc) from the given archive, previously encoded by \c NSKeyedArchiver.
- [+ unarchivedDictionaryWithKeysOfClass:objectsOfClass:fromData:error:](./nskeyedunarchiver/unarchiveddictionarywithkeysofclass_objectsofclass_fromdata_error_.md)
  Decodes the \c NSDictionary root object from \c data which should be an \c NSDictionary<keyCls,objectCls>  with keys of type given in \c keyCls and objects of the given non-collection class \c objectCls (no nested dictionaries or other dictionaries contained in the dictionary, etc) from the given archive, previously encoded by \c NSKeyedArchiver.
- [+ unarchivedDictionaryWithKeysOfClasses:objectsOfClasses:fromData:error:](./nskeyedunarchiver/unarchiveddictionarywithkeysofclasses_objectsofclasses_fromdata_error_.md)
  Decodes the \c NSDictionary root object from \c data which should be an \c NSDictionary, with keys of the types given in \c keyClasses and objects of the given non-collection classes in \c objectClasses (no nested dictionaries or other dictionaries contained in the dictionary, etc) from the given archive, previously encoded by \c NSKeyedArchiver.

## Relationships

### Inherits From
- [NSCoder](./nscoder.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Keyed Archivers
- [class NSKeyedArchiver](./nskeyedarchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [protocol NSKeyedArchiverDelegate](./nskeyedarchiverdelegate.md)
  The optional methods implemented by the delegate of a keyed archiver.
- [protocol NSKeyedUnarchiverDelegate](./nskeyedunarchiverdelegate.md)
  The optional methods implemented by the delegate of a keyed unarchiver.
- [class NSCoder](./nscoder.md)
  An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.
- [class NSSecureUnarchiveFromDataTransformer](./nssecureunarchivefromdatatransformer.md)
  A value transformer that converts data to and from classes that support secure coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver)*