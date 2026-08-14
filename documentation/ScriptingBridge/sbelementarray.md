# SBElementArray

**Framework**: Scripting Bridge  
**Kind**: class

`SBElementArray` is subclass of `NSMutableArray` that manages collections of related [`SBObject`](sbobject.md) objects. For example, when you ask the Finder for a list of disks, or ask iTunes for a list of playlists, you get the result back as an `SBElementArray` containing Scripting Bridge objects representing those items.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
class SBElementArray
```

#### Overview

`SBElementArray` defines methods beyond those of [`NSArray`](https://developer.apple.com/documentation/foundation/nsarray) for obtaining individual objects. In addition to [`object(at:)`](https://developer.apple.com/documentation/foundation/nsarray/object(at:)), `SBElementArray` also defines [`object(withName:)`](sbelementarray/object(withname:).md), [`object(withID:)`](sbelementarray/object(withid:).md), and [`object(atLocation:)`](sbelementarray/object(atlocation:).md).

#### Subclassing Notes

The `SBElementArray` class is not designed for subclassing.

## Topics

### Getting Objects in the Array
- [func object(withName: String) -> Any](sbelementarray/object(withname:).md)
  Returns the object in the array with the given name.
- [func object(withID: Any) -> Any](sbelementarray/object(withid:).md)
  Returns the object in the array with the given identifier.
- [func object(atLocation: Any) -> Any](sbelementarray/object(atlocation:).md)
  Returns the object at the given location in the receiver.
### Getting the Referenced Array
- [func get() -> [Any]?](sbelementarray/get.md)
  Forces evaluation of the receiver, causing the real object to be returned immediately.
### Filtering an Element Array
- [func array(byApplying: Selector) -> [Any]](sbelementarray/array(byapplying:).md)
  Returns an array containing the results of sending the specified message to each object in the receiver.
- [func array(byApplying: Selector, with: Any) -> [Any]](sbelementarray/array(byapplying:with:).md)
  Returns an array containing the results of sending the specified message to each object in the receiver.

## Relationships

### Inherits From
- [NSMutableArray](../foundation/nsmutablearray.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomReflectable](../swift/customreflectable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSFastEnumeration](../foundation/nsfastenumeration.md)
- [NSMutableCopying](../foundation/nsmutablecopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Sequence](../swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbelementarray)*