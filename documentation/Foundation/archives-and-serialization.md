# Archives and Serialization

**Framework**: Foundation

Convert objects and values to and from property list, JSON, and other flat binary representations.

#### Overview

Use these APIs to convert your app’s in-memory types to representations suitable for serialization over I/O and network interfaces or to long-term storage.

In Swift, the standard library defines the [`Encodable`](https://developer.apple.com/documentation/Swift/Encodable), [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable), and [`Codable`](https://developer.apple.com/documentation/Swift/Codable) types, along with [`Encoder`](https://developer.apple.com/documentation/Swift/Encoder) and [`Decoder`](https://developer.apple.com/documentation/Swift/Decoder) APIs to perform encoding and decoding, as described in [`Encoding, Decoding, and Serialization`](https://developer.apple.com/documentation/Swift/encoding-decoding-and-serialization). Foundation extends this with the [`EncodableWithConfiguration`](encodablewithconfiguration.md) and [`DecodableWithConfiguration`](decodablewithconfiguration.md) protocols, used for types that require additional static information to encode and decode, such as [`AttributedString`](attributedstring.md).

In Objective-C, [`NSCoding`](nscoding.md) defines a protocol for encoding and decoding objects. When adding serialization to your own types, you should also adopt [`NSSecureCoding`](nssecurecoding.md). This protocol adds protection against security vulnerabilities introduced by instantiating arbitrary objects as part of the decoding process.

Many system frameworks use these types. When working with external systems, such as URL endpoints, use the JSON and XML APIs to serialize your app’s types to standard formats.

## Topics

### Adopting Codability
- [Encoding and Decoding Custom Types](encoding-and-decoding-custom-types.md)
  Make your data types encodable and decodable for compatibility with external representations such as JSON.
- [typealias Codable = Decodable & Encodable](../Swift/Codable.md)
  A type that can convert itself into and out of an external representation.
- [protocol NSCoding](nscoding.md)
  A protocol that enables an object to be encoded and decoded for archiving and distribution.
- [protocol NSSecureCoding](nssecurecoding.md)
  A protocol that enables encoding and decoding in a manner that is robust against object substitution attacks.
### Serializing Arbitrary Payloads
- [typealias CodableWithConfiguration](codablewithconfiguration.md)
  A type that can convert itself into and out of an external representation with the help of a configuration that handles encoding contained types.
- [struct CodableConfiguration](codableconfiguration.md)
  A property wrapper that makes a type codable, by supplying a configuration that provides additional information for serialization.
- [protocol DecodableWithConfiguration](decodablewithconfiguration.md)
  A protocol for types that support decoding when supplied with an additional configuration type.
- [protocol DecodingConfigurationProviding](decodingconfigurationproviding.md)
  A protocol whose conformers provide a configuration instance to help decode types that don’t support encoding by themselves.
- [protocol EncodableWithConfiguration](encodablewithconfiguration.md)
  A protocol for types that support encoding when supplied with an additional configuration type.
- [protocol EncodingConfigurationProviding](encodingconfigurationproviding.md)
  A protocol whose conformers provide a configuration instance to help encode types that don’t support encoding by themselves.
### JSON
- [class JSONEncoder](jsonencoder.md)
  An object that encodes instances of a data type as JSON objects.
- [class JSONDecoder](jsondecoder.md)
  An object that decodes instances of a data type from JSON objects.
- [class JSONSerialization](jsonserialization.md)
  An object that converts between JSON and the equivalent Foundation objects.
### Property Lists
- [class PropertyListEncoder](propertylistencoder.md)
  An object that encodes instances of data types to a property list.
- [class PropertyListDecoder](propertylistdecoder.md)
  An object that decodes instances of data types from a property list.
- [class PropertyListSerialization](propertylistserialization.md)
  An object that converts between a property list and one of several serialized representations.
### XML
- [XML Processing and Modeling](xml-processing-and-modeling.md)
  Parse XML documents.
### Keyed Archivers
- [class NSKeyedArchiver](nskeyedarchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [protocol NSKeyedArchiverDelegate](nskeyedarchiverdelegate.md)
  The optional methods implemented by the delegate of a keyed archiver.
- [class NSKeyedUnarchiver](nskeyedunarchiver.md)
  A decoder that restores data from an archive referenced by keys.
- [protocol NSKeyedUnarchiverDelegate](nskeyedunarchiverdelegate.md)
  The optional methods implemented by the delegate of a keyed unarchiver.
- [class NSCoder](nscoder.md)
  An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.
- [class NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md)
  A value transformer that converts data to and from classes that support secure coding.
### Deprecated
- [class NSArchiver](nsarchiver.md)
  A coder that stores an object’s data to an archive.
- [class NSUnarchiver](nsunarchiver.md)
  A decoder that restores data from an archive.

## See Also

- [File System](file-system.md)
  Create, read, write, and examine files and folders in the file system.
- [Preferences](preferences.md)
  Persistently store domain-scoped pieces of information for configuring your app.
- [Spotlight](spotlight.md)
  Search for files and other items on the local device, and index your app’s content for searching.
- [iCloud](icloud.md)
  Manage files and key-value data that automatically synchronize among a user’s iCloud devices.
- [Optimizing Your App’s Data for iCloud Backup](optimizing-your-app-s-data-for-icloud-backup.md)
  Minimize the space and time that backups take to create by excluding purgeable and nonpurgeable data from backups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/archives-and-serialization)*