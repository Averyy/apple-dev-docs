# NSKeyedArchiver

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An encoder that stores an object’s data to an archive referenced by keys.

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
class NSKeyedArchiver
```

```objc
@interface NSKeyedArchiver : NSCoder
```

#### Overview

[`NSKeyedArchiver`](./nskeyedarchiver.md), a concrete subclass of [`NSCoder`](./nscoder.md), provides a way to encode objects (and scalar values) into an architecture-independent format suitable for storage in a file. When you archive a set of objects, the archiver writes the class information and instance variables for each object to the archive. The companion class [`NSKeyedUnarchiver`](./nskeyedunarchiver.md) decodes the data in an archive and creates a set of objects equivalent to the original set.

A keyed archive differs from a non-keyed archive in that all the objects and values encoded into the archive have names, or keys. When decoding a non-keyed archive, the decoder must decode values in the same order the original encoder used. When decoding a keyed archive, the decoder requests values by name, meaning it can decode values out of sequence or not at all. Keyed archives, therefore, provide better support for forward and backward compatibility.

The keys given to encoded values must be unique only within the scope of the currently-encoding object. A keyed archive is hierarchical, so the keys used by object A to encode its instance variables don’t conflict with the keys used by object B. This is true even if A and B are instances of the same class. Within a single object, however, the keys used by a subclass can conflict with keys used in its superclasses.

An [`NSArchiver`](./nsarchiver.md) object can write the archive data to a file or to a mutable-data object (an instance of [`NSMutableData`](./nsmutabledata.md)) that you provide.

## Topics

### Creating a Keyed Archiver
- [init(requiringSecureCoding: Bool)](./nskeyedarchiver/init%28requiringsecurecoding%29.md)
  Creates an archiver to encode data, and optionally disables secure coding.
- [init()](./nskeyedarchiver/init%28%29.md)
  Initializes an archiver to encode data.
- [init(forWritingWith: NSMutableData)](./nskeyedarchiver/init%28forwritingwith%29.md)
  Initializes an archiver to encode data into a given a mutable-data object.
### Archiving Data
- [class func archivedData(withRootObject: Any, requiringSecureCoding: Bool) throws -> Data](./nskeyedarchiver/archiveddata%28withrootobject,requiringsecurecoding%29.md)
  Encodes an object graph with the given root object into a data representation, optionally requiring secure coding.
- [func finishEncoding()](./nskeyedarchiver/finishencoding%28%29.md)
  Instructs the receiver to construct the final data stream.
- [var encodedData: Data](./nskeyedarchiver/encodeddata.md)
  The encoded data for the archiver.
- [var outputFormat: PropertyListSerialization.PropertyListFormat](./nskeyedarchiver/outputformat.md)
  The format in which the receiver encodes its data.
- [var requiresSecureCoding: Bool](./nskeyedarchiver/requiressecurecoding.md)
  Indicates whether the archiver requires all archived classes to resist object substitution attacks.
- [class func archivedData(withRootObject: Any) -> Data](./nskeyedarchiver/archiveddata%28withrootobject%29.md)
  Returns a data object that contains the encoded form of the object graph formed by the given root object.
- [class func archiveRootObject(Any, toFile: String) -> Bool](./nskeyedarchiver/archiverootobject%28_,tofile%29.md)
  Archives an object graph rooted at a given object to a file at a given path.
### Encoding Data and Objects
- [func encodeEncodable<T>(T, forKey: String) throws](./nskeyedarchiver/encodeencodable%28_,forkey%29.md)
  Encodes a given value and associates it with a key.
- [func encode(Bool, forKey: String)](./nskeyedarchiver/encode%28_,forkey%29-9pxhm.md)
  Encodes a given Boolean value and associates it with a key.
- [func encodeBytes(UnsafePointer<UInt8>?, length: Int, forKey: String)](./nskeyedarchiver/encodebytes%28_,length,forkey%29.md)
  Encodes a given number of bytes from a given C array of bytes and associates them with a key.
- [func encodeConditionalObject(Any?, forKey: String)](./nskeyedarchiver/encodeconditionalobject%28_,forkey%29.md)
  Encodes a reference to a given object and associates it with a key only if it has been unconditionally encoded elsewhere in the archive.
- [func encode(Double, forKey: String)](./nskeyedarchiver/encode%28_,forkey%29-1mkfl.md)
  Encodes a given `double` value and associates it with a key.
- [func encode(Float, forKey: String)](./nskeyedarchiver/encode%28_,forkey%29-67rcs.md)
  Encodes a given `float` value and associates it with a key.
- [func encode(Int32, forKey: String)](./nskeyedarchiver/encode%28_,forkey%29-5i7tc.md)
  Encodes a given 32-bit integer value and associates it with a key.
- [func encode(Int64, forKey: String)](./nskeyedarchiver/encode%28_,forkey%29-ycdd.md)
  Encodes a given 64-bit integer value and associates it with a key.
- [func encode(Any?, forKey: String)](./nskeyedarchiver/encode%28_,forkey%29-9f4n9.md)
  Encodes a given object and associates it with a given key.
### Managing the Delegate
- [var delegate: (any NSKeyedArchiverDelegate)?](./nskeyedarchiver/delegate.md)
  The archiver’s delegate.
### Managing Classes and Class Names
- [class func setClassName(String?, for: AnyClass)](./nskeyedarchiver/setclassname%28_,for%29-swift.type.method.md)
  Sets a global translation mapping to encode instances of a given class with the provided name, rather than their real name.
- [class func className(for: AnyClass) -> String?](./nskeyedarchiver/classname%28for%29-swift.type.method.md)
  Returns the class name with which the archiver class encodes instances of a given class.
- [func setClassName(String?, for: AnyClass)](./nskeyedarchiver/setclassname%28_,for%29-swift.method.md)
  Sets a mapping for this archiver to encode instances of a given class with the provided name, rather than their real name.
- [func className(for: AnyClass) -> String?](./nskeyedarchiver/classname%28for%29-swift.method.md)
  Returns the class name with which this archiver encodes instances of a given class.
### Constants
- [Keyed Archiving Exception Names](./keyed-archiving-exception-names.md)
  Names of exceptions raised by this class if problems occur while creating an archive.
- [Keyed Archiver Root Object Key](./keyed-archiver-root-object-key.md)
  Keys that the archiver uses in the hierarchy of encoded objects.
### Initializers
- [init(forWritingWithMutableData: NSMutableData)](./nskeyedarchiver/init%28forwritingwithmutabledata%29.md)

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
- [protocol NSKeyedArchiverDelegate](./nskeyedarchiverdelegate.md)
  The optional methods implemented by the delegate of a keyed archiver.
- [class NSKeyedUnarchiver](./nskeyedunarchiver.md)
  A decoder that restores data from an archive referenced by keys.
- [protocol NSKeyedUnarchiverDelegate](./nskeyedunarchiverdelegate.md)
  The optional methods implemented by the delegate of a keyed unarchiver.
- [class NSCoder](./nscoder.md)
  An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.
- [class NSSecureUnarchiveFromDataTransformer](./nssecureunarchivefromdatatransformer.md)
  A value transformer that converts data to and from classes that support secure coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiver)*