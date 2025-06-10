# NSUnarchiver

**Framework**: Foundation  
**Kind**: class

A decoder that restores data from an archive.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class NSUnarchiver
```

#### Overview

[`NSUnarchiver`](nsunarchiver.md), a concrete subclass of [`NSCoder`](nscoder.md), defines methods for decoding a set of Objective-C objects from an archive. Such archives are produced by objects of the [`NSArchiver`](nsarchiver.md) class.

In macOS 10.2 and later, [`NSArchiver`](nsarchiver.md) and [`NSUnarchiver`](nsunarchiver.md) have been replaced by [`NSKeyedArchiver`](nskeyedarchiver.md) and [`NSKeyedUnarchiver`](nskeyedunarchiver.md) respectively—see [`Archives and Serializations Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

## Topics

### Initializing an NSUnarchiver
- [init?(forReadingWith: Data)](nsunarchiver/init(forreadingwith:).md)
  Returns an `NSUnarchiver` object initialized to read an archive from a given data object.
### Decoding objects
- [class func unarchiveObject(with: Data) -> Any?](nsunarchiver/unarchiveobject(with:).md)
  Decodes and returns the object archived in a given `NSData` object.
- [class func unarchiveObject(withFile: String) -> Any?](nsunarchiver/unarchiveobject(withfile:).md)
  Decodes and returns the object archived in the file `path`.
### Managing an NSUnarchiver
- [var isAtEnd: Bool](nsunarchiver/isatend.md)
  A Boolean value that indicates whether the receiver has reached the end of the encoded data while decoding.
- [var systemVersion: UInt32](nsunarchiver/systemversion-swift.property.md)
  The system version number in effect when the archive was created.
### Substituting classes or objects
- [class func classNameDecoded(forArchiveClassName: String) -> String](nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.type.method.md)
  Returns the name of the class used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [class func decodeClassName(String, asClassName: String)](nsunarchiver/decodeclassname(_:asclassname:)-swift.type.method.md)
  Instructs instances of `NSUnarchiver` to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.
- [func classNameDecoded(forArchiveClassName: String) -> String](nsunarchiver/classnamedecoded(forarchiveclassname:)-swift.method.md)
  Returns the name of the class that will be used when instantiating objects whose ostensible class, according to the archived data, is a given name.
- [func decodeClassName(String, asClassName: String)](nsunarchiver/decodeclassname(_:asclassname:)-swift.method.md)
  Instructs the receiver to use the class with a given name when instantiating objects whose ostensible class, according to the archived data, is another given name.
- [func replace(Any, with: Any)](nsunarchiver/replace(_:with:).md)
  Causes the receiver to substitute one given object for another whenever the latter is extracted from the archive.

## Relationships

### Inherits From
- [NSCoder](nscoder.md)
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

- [class NSArchiver](nsarchiver.md)
  A coder that stores an object’s data to an archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsunarchiver)*