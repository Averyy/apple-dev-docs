# NSSecureUnarchiveFromDataTransformer

**Framework**: Foundation  
**Kind**: class

A value transformer that converts data to and from classes that support secure coding.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class NSSecureUnarchiveFromDataTransformer
```

#### Overview

This class provides a default [`ValueTransformer`](valuetransformer.md) implementation for secure decoding. This class attempts to decode data into the classes listed within [`allowedTopLevelClasses`](nssecureunarchivefromdatatransformer/allowedtoplevelclasses.md), which includes [`NSArray`](nsarray.md), [`NSDictionary`](nsdictionary.md), [`NSSet`](nsset.md), [`NSString`](nsstring.md), [`NSNumber`](nsnumber.md), [`NSDate`](nsdate.md), [`NSData`](nsdata.md), [`NSURL`](nsurl.md), [`NSUUID`](nsuuid.md), and [`NSNull`](nsnull.md).

To archive or unarchive other classes that support [`NSSecureCoding`](nssecurecoding.md), create a subclass and override [`allowedTopLevelClasses`](nssecureunarchivefromdatatransformer/allowedtoplevelclasses.md) to list the classes to transform.

To use [`NSSecureUnarchiveFromDataTransformer`](nssecureunarchivefromdatatransformer.md) with [`Core Data`](https://developer.apple.com/documentation/CoreData), use the name of this class, or the name of a subclass you implement, as the name of the transformer for an entity’s attribute within a Core Data Model. If you use your own transformer subclass, register it with your app before intializing your persistent container with Core Data.

For an example of subclassing [`NSSecureUnarchiveFromDataTransformer`](nssecureunarchivefromdatatransformer.md), see [`Handling Different Data Types in Core Data`](https://developer.apple.com/documentation/CoreData/handling-different-data-types-in-core-data), which has a `ColorToDataTransformer` class that transforms [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) to [`NSData`](nsdata.md) and the reverse, to support archiving instances of [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor).

## Topics

### Getting Information About a Transformer
- [class var allowedTopLevelClasses: [AnyClass]](nssecureunarchivefromdatatransformer/allowedtoplevelclasses.md)
  A list of allowed classes the top-level object in an archive must conform to, for encoding and decoding.

## Relationships

### Inherits From
- [ValueTransformer](valuetransformer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssecureunarchivefromdatatransformer)*