# NSKeyedArchiverDelegate

**Framework**: Foundation  
**Kind**: protocol

The optional methods implemented by the delegate of a keyed archiver.

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
protocol NSKeyedArchiverDelegate : NSObjectProtocol
```

## Topics

### Encoding Data and Objects
- [func archiver(NSKeyedArchiver, didEncode: Any?)](nskeyedarchiverdelegate/archiver(_:didencode:).md)
  Informs the delegate that a given object has been encoded.
- [func archiverDidFinish(NSKeyedArchiver)](nskeyedarchiverdelegate/archiverdidfinish(_:).md)
  Notifies the delegate that encoding has finished.
- [func archiver(NSKeyedArchiver, willEncode: Any) -> Any?](nskeyedarchiverdelegate/archiver(_:willencode:).md)
  Informs the delegate that `object` is about to be encoded.
- [func archiverWillFinish(NSKeyedArchiver)](nskeyedarchiverdelegate/archiverwillfinish(_:).md)
  Notifies the delegate that encoding is about to finish.
- [func archiver(NSKeyedArchiver, willReplace: Any?, with: Any?)](nskeyedarchiverdelegate/archiver(_:willreplace:with:).md)
  Informs the delegate that one given object is being substituted for another given object.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSKeyedArchiver](nskeyedarchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [class NSKeyedUnarchiver](nskeyedunarchiver.md)
  A decoder that restores data from an archive referenced by keys.
- [protocol NSKeyedUnarchiverDelegate](nskeyedunarchiverdelegate.md)
  The optional methods implemented by the delegate of a keyed unarchiver.
- [class NSCoder](nscoder.md)
  An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.
- [class NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md)
  A value transformer that converts data to and from classes that support secure coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedarchiverdelegate)*