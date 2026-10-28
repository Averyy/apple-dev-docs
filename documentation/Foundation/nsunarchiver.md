# NSUnarchiver

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A decoder that restores data from an archive.

**Availability**:
- iOS 2.0+ - Deprecated in 11.0
- iPadOS 2.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use NSKeyedUnarchiver instead

## Declaration

```swift
class NSUnarchiver
```

```objc
@interface NSUnarchiver : NSCoder
```

## Overview

[`NSUnarchiver`](./nsunarchiver.md), a concrete subclass of [`NSCoder`](./nscoder.md), defines methods for decoding a set of Objective-C objects from an archive. Such archives are produced by objects of the [`NSArchiver`](./nsarchiver.md) class.

In macOS 10.2 and later, [`NSArchiver`](./nsarchiver.md) and [`NSUnarchiver`](./nsunarchiver.md) have been replaced by [`NSKeyedArchiver`](./nskeyedarchiver.md) and [`NSKeyedUnarchiver`](./nskeyedunarchiver.md) respectively—see [Archives and Serializations Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

## Topics

### Initializing an NSUnarchiver
- [init?(forReadingWith: Data)](./nsunarchiver/init%28forreadingwith%29.md)
  Returns an `NSUnarchiver` object initialized to read an archive from a given data object.
### Decoding objects
- [class func unarchiveObject(with: Data) -> Any?](./nsunarchiver/unarchiveobject%28with%29.md)
  Decodes and returns the object archived in a given `NSData` object.
- [class func unarchiveObject(withFile: String) -> Any?](./nsunarchiver/unarchiveobject%28withfile%29.md)
  Decodes and returns the object archived in the file `path`.
### Managing an NSUnarchiver
- [var isAtEnd: Bool](./nsunarchiver/isatend.md)
  A Boolean value that indicates whether the receiver has reached the end of the encoded data while decoding.
- [var systemVersion: UInt32](./nsunarchiver/systemversion-swift.property.md)
  The system version number in effect when the archive was created.
- [- objectZone](./nsunarchiver/objectzone-c.method.md)
  Returns the memory zone used to allocate decoded objects.
- [- setObjectZone:](./nsunarchiver/setobjectzone_.md)
  Sets the memory zone used to allocate decoded objects.
### Substituting classes or objects
- [class func classNameDecoded(forArchiveClassName: String) -> String](./nsunarchiver/classnamedecoded%28forarchiveclassname%29-swift.type.method.md)
  Returns the name of the class used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [class func decodeClassName(String, asClassName: String)](./nsunarchiver/decodeclassname%28_,asclassname%29-swift.type.method.md)
  Instructs instances of `NSUnarchiver` to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.
- [func classNameDecoded(forArchiveClassName: String) -> String](./nsunarchiver/classnamedecoded%28forarchiveclassname%29-swift.method.md)
  Returns the name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [func decodeClassName(String, asClassName: String)](./nsunarchiver/decodeclassname%28_,asclassname%29-swift.method.md)
  Instructs the receiver to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.
- [func replace(Any, with: Any)](./nsunarchiver/replace%28_,with%29.md)
  Causes the receiver to substitute one given object for another whenever the latter is extracted from the archive.
### Initializers
- [init?(forReadingWithData: Data)](./nsunarchiver/init%28forreadingwithdata%29.md)
### Instance Variables
- [allUnarchivedObjects](./nsunarchiver/allunarchivedobjects.md)
- [classVersions](./nsunarchiver/classversions.md)
- [cursor](./nsunarchiver/cursor.md)
- [datax](./nsunarchiver/datax.md)
- [lastLabel](./nsunarchiver/lastlabel.md)
- [map](./nsunarchiver/map.md)
- [objectZone](./nsunarchiver/objectzone-c.ivar.md)
- [pointerTable](./nsunarchiver/pointertable.md)
- [reserved](./nsunarchiver/reserved.md)
- [streamerVersion](./nsunarchiver/streamerversion.md)
- [stringTable](./nsunarchiver/stringtable.md)
- [swap](./nsunarchiver/swap.md)
- [systemVersion](./nsunarchiver/systemversion-c.ivar.md)
- [unused1](./nsunarchiver/unused1.md)
- [unused2](./nsunarchiver/unused2.md)

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

### Deprecated
- [class NSArchiver](./nsarchiver.md)
  A coder that stores an object’s data to an archive.
- [NXReadNSObjectFromCoder](./nxreadnsobjectfromcoder.md)
  Returns the next object from the coder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver)*