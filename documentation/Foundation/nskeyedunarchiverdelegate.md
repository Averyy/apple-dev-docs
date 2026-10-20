# NSKeyedUnarchiverDelegate

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol NSKeyedUnarchiverDelegate <NSObject>
```

## Topics

### Decoding Objects
- [func unarchiver(NSKeyedUnarchiver, cannotDecodeObjectOfClassName: String, originalClasses: [String]) -> AnyClass?](./nskeyedunarchiverdelegate/unarchiver%28_,cannotdecodeobjectofclassname,originalclasses%29.md)
  Informs the delegate that the class with a given name is not available during decoding.
- [func unarchiver(NSKeyedUnarchiver, didDecode: consuming Any?) -> Any?](./nskeyedunarchiverdelegate/unarchiver%28_,diddecode%29.md)
  Informs the delegate that a given object has been decoded.
- [func unarchiver(NSKeyedUnarchiver, willReplace: Any, with: Any)](./nskeyedunarchiverdelegate/unarchiver%28_,willreplace,with%29.md)
  Informs the delegate that one object is being substituted for another.
### Finishing Decoding
- [func unarchiverDidFinish(NSKeyedUnarchiver)](./nskeyedunarchiverdelegate/unarchiverdidfinish%28_%29.md)
  Notifies the delegate that decoding has finished.
- [func unarchiverWillFinish(NSKeyedUnarchiver)](./nskeyedunarchiverdelegate/unarchiverwillfinish%28_%29.md)
  Notifies the delegate that decoding is about to finish.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Keyed Archivers
- [class NSKeyedArchiver](./nskeyedarchiver.md)
  An encoder that stores an object’s data to an archive referenced by keys.
- [protocol NSKeyedArchiverDelegate](./nskeyedarchiverdelegate.md)
  The optional methods implemented by the delegate of a keyed archiver.
- [class NSKeyedUnarchiver](./nskeyedunarchiver.md)
  A decoder that restores data from an archive referenced by keys.
- [class NSCoder](./nscoder.md)
  An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.
- [class NSSecureUnarchiveFromDataTransformer](./nssecureunarchivefromdatatransformer.md)
  A value transformer that converts data to and from classes that support secure coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiverdelegate)*