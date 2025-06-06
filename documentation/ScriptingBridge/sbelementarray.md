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

`SBElementArray` defines methods beyond those of [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) for obtaining individual objects. In addition to [`objectAtIndex:`](https://developer.apple.com/documentation/foundation/nsarray/1417555-objectatindex), `SBElementArray` also defines [`object(withName:)`](sbelementarray/object(withname:).md), [`object(withID:)`](sbelementarray/object(withid:).md), and [`object(atLocation:)`](sbelementarray/object(atlocation:).md).

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
- [NSMutableArray](../Foundation/NSMutableArray.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSFastEnumeration](../Foundation/NSFastEnumeration.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbelementarray)*