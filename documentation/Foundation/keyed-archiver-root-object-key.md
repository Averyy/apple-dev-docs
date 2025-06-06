# Keyed Archiver Root Object Key

**Framework**: Foundation

Keys that the archiver uses in the hierarchy of encoded objects.

## Topics

### Constants
- [let NSKeyedArchiveRootObjectKey: String](nskeyedarchiverootobjectkey.md)
  Archives created using the class method [`archivedData(withRootObject:)`](nskeyedarchiver/archiveddata(withrootobject:).md) use this key for the root object in the hierarchy of encoded objects. The [`NSKeyedUnarchiver`](nskeyedunarchiver.md) class method [`unarchiveObject(with:)`](nskeyedunarchiver/unarchiveobject(with:).md) looks for this root key as well.

## See Also

- [Keyed Archiving Exception Names](keyed-archiving-exception-names.md)
  Names of exceptions raised by this class if problems occur while creating an archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/keyed-archiver-root-object-key)*