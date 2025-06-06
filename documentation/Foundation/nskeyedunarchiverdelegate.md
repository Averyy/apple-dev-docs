# NSKeyedUnarchiverDelegate

**Framework**: Foundation  
**Kind**: protocol

The optional methods implemented by the delegate of a keyed unarchiver.

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
protocol NSKeyedUnarchiverDelegate : NSObjectProtocol
```

## Topics

### Decoding Objects
- [func unarchiver(NSKeyedUnarchiver, cannotDecodeObjectOfClassName: String, originalClasses: [String]) -> AnyClass?](nskeyedunarchiverdelegate/unarchiver(_:cannotdecodeobjectofclassname:originalclasses:).md)
  Informs the delegate that the class with a given name is not available during decoding.
- [func unarchiver(NSKeyedUnarchiver, didDecode: Any?) -> Any?](nskeyedunarchiverdelegate/unarchiver(_:diddecode:).md)
  Informs the delegate that a given object has been decoded.
- [func unarchiver(NSKeyedUnarchiver, willReplace: Any, with: Any)](nskeyedunarchiverdelegate/unarchiver(_:willreplace:with:).md)
  Informs the delegate that one object is being substituted for another.
### Finishing Decoding
- [func unarchiverDidFinish(NSKeyedUnarchiver)](nskeyedunarchiverdelegate/unarchiverdidfinish(_:).md)
  Notifies the delegate that decoding has finished.
- [func unarchiverWillFinish(NSKeyedUnarchiver)](nskeyedunarchiverdelegate/unarchiverwillfinish(_:).md)
  Notifies the delegate that decoding is about to finish.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSKeyedArchiver](nskeyedarchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [protocol NSKeyedArchiverDelegate](nskeyedarchiverdelegate.md)
  The optional methods implemented by the delegate of a keyed archiver.
- [class NSKeyedUnarchiver](nskeyedunarchiver.md)
  A decoder that restores data from an archive referenced by keys.
- [class NSCoder](nscoder.md)
  An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.
- [class NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md)
  A value transformer that converts data to and from classes that support secure coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate)*