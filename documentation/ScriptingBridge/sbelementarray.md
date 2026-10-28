# SBElementArray

**Framework**: Scripting Bridge  
**Kind**: class  
**Role**: Class

`SBElementArray` is subclass of `NSMutableArray` that manages collections of related [`SBObject`](./sbobject.md) objects. For example, when you ask the Finder for a list of disks, or ask iTunes for a list of playlists, you get the result back as an `SBElementArray` containing Scripting Bridge objects representing those items.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
class SBElementArray
```

```objc
@interface SBElementArray : NSMutableArray
```

## Overview

`SBElementArray` defines methods beyond those of [`NSArray`](../Foundation/nsarray.md) for obtaining individual objects. In addition to [`object(at:)`](../Foundation/nsarray/object%28at%29.md), `SBElementArray` also defines [`object(withName:)`](./sbelementarray/object%28withname%29.md), [`object(withID:)`](./sbelementarray/object%28withid%29.md), and [`object(atLocation:)`](./sbelementarray/object%28atlocation%29.md).

## Subclassing Notes

The `SBElementArray` class is not designed for subclassing.

## Topics

### Getting Objects in the Array
- [func object(withName: String) -> Any](./sbelementarray/object%28withname%29.md)
  Returns the object in the array with the given name.
- [func object(withID: Any) -> Any](./sbelementarray/object%28withid%29.md)
  Returns the object in the array with the given identifier.
- [func object(atLocation: Any) -> Any](./sbelementarray/object%28atlocation%29.md)
  Returns the object at the given location in the receiver.
### Getting the Referenced Array
- [func get() -> [Any]?](./sbelementarray/get%28%29.md)
  Forces evaluation of the receiver, causing the real object to be returned immediately.
### Filtering an Element Array
- [func array(byApplying: Selector) -> [Any]](./sbelementarray/array%28byapplying%29.md)
  Returns an array containing the results of sending the specified message to each object in the receiver.
- [func array(byApplying: Selector, with: Any) -> [Any]](./sbelementarray/array%28byapplying,with%29.md)
  Returns an array containing the results of sending the specified message to each object in the receiver.

## Relationships

### Inherits From
- [NSMutableArray](../Foundation/nsmutablearray.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSFastEnumeration](../Foundation/nsfastenumeration.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbelementarray)*