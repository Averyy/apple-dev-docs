# NSArchiver

**Framework**: Foundation  
**Kind**: class

A coder that stores an object’s data to an archive.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+

## Declaration

```swift
class NSArchiver
```

#### Overview

[`NSArchiver`](nsarchiver.md), a concrete subclass of [`NSCoder`](nscoder.md), provides a way to encode objects into an architecture-independent format that can be stored in a file. When you archive a graph of objects, the class information and instance variables for each object are written to the archive. The companion class [`NSUnarchiver`](nsunarchiver.md) decodes the data in an archive and creates a graph of objects equivalent to the original set.

[`NSArchiver`](nsarchiver.md) stores the archive data in a mutable data object ([`NSMutableData`](nsmutabledata.md)). After encoding the objects, you can have the [`NSArchiver`](nsarchiver.md) object write this mutable data object immediately to a file, or you can retrieve the mutable data object for some other use.

In macOS 10.2 and later, [`NSArchiver`](nsarchiver.md) and [`NSUnarchiver`](nsunarchiver.md) have been replaced by [`NSKeyedArchiver`](nskeyedarchiver.md) and [`NSKeyedUnarchiver`](nskeyedunarchiver.md) respectively—see [`Archives and Serializations Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i).

## Topics

### Initializing an NSArchiver
- [init(forWritingWith: NSMutableData)](nsarchiver/init(forwritingwith:).md)
  Returns an archiver, initialized to encode stream and version information into a given mutable data object.
### Archiving data
- [class func archivedData(withRootObject: Any) -> Data](nsarchiver/archiveddata(withrootobject:).md)
  Returns a data object containing the encoded form of the object graph whose root object is given.
- [class func archiveRootObject(Any, toFile: String) -> Bool](nsarchiver/archiverootobject(_:tofile:).md)
  Creates a temporary instance of `NSArchiver` and archives an object graph by encoding it into a data object and writing the resulting data object to a specified file.
- [func encodeRootObject(Any)](nsarchiver/encoderootobject(_:).md)
  Archives a given object along with all the objects to which it is connected.
- [func encodeConditionalObject(Any?)](nsarchiver/encodeconditionalobject(_:).md)
  Conditionally archives a given object.
### Getting the archived data
- [var archiverData: NSMutableData](nsarchiver/archiverdata.md)
  The receiver’s archive data.
### Substituting classes or objects
- [func classNameEncoded(forTrueClassName: String) -> String?](nsarchiver/classnameencoded(fortrueclassname:).md)
  Returns the name of the class used to archive instances of the class with a given true name.
- [func encodeClassName(String, intoClassName: String)](nsarchiver/encodeclassname(_:intoclassname:).md)
  Encodes a substitute name for the class with a given true name.
- [func replace(Any, with: Any)](nsarchiver/replace(_:with:).md)
  Causes the receiver to treat subsequent requests to encode a given object as though they were requests to encode another given object.
### Constants
- [Archiving Exception Names](archiving-exception-names.md)
  Raised by `NSArchiver` if there are problems initializing or encoding.

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

- [class NSUnarchiver](nsunarchiver.md)
  A decoder that restores data from an archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarchiver)*