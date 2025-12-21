# classFallbacksForKeyedArchiver()

**Framework**: Objective-C Runtime  
**Kind**: method

Overridden to return the names of classes that can be used to decode objects if their class is unavailable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func classFallbacksForKeyedArchiver() -> [String]
```

#### Return Value

An array of string objects that specify the names of classes in preferred order for unarchiving

#### Discussion

[`NSKeyedArchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedArchiver) calls this method and stores the result inside the archive. If the actual class of an object doesn’t exist at the time of unarchiving, [`NSKeyedUnarchiver`](https://developer.apple.com/documentation/Foundation/NSKeyedUnarchiver) goes through the stored list of classes and uses the first one that does exists as a substitute class for decoding the object. The default implementation of this method returns an empty array.

You can use this method if you introduce a new class into your application to provide some backwards compatibility in case the archive will be read on a system that does not have that class. Sometimes there may be another class which may work nearly as well as a substitute for the new class, and the archive keys and archived state for the new class can be carefully chosen (or compatibility written out) so that the object can be unarchived as the substitute class if necessary.

## See Also

- [func awakeAfter(using: NSCoder) -> Any?](nsobject-swift.class/awakeafter(using:).md)
  Overridden by subclasses to substitute another object in place of the object that was decoded and subsequently received this message.
- [var classForArchiver: AnyClass?](nsobject-swift.class/classforarchiver.md)
  The class to substitute for the receiver’s own class during archiving.
- [var classForCoder: AnyClass](nsobject-swift.class/classforcoder.md)
  Overridden by subclasses to substitute a class other than its own during coding.
- [var classForKeyedArchiver: AnyClass?](nsobject-swift.class/classforkeyedarchiver.md)
  Subclasses to substitute a new class for instances during keyed archiving.
- [class func classForKeyedUnarchiver() -> AnyClass](nsobject-swift.class/classforkeyedunarchiver.md)
  Overridden by subclasses to substitute a new class during keyed unarchiving.
- [func replacementObject(for: NSArchiver) -> Any?](nsobject-swift.class/replacementobject(for:)-8ih2x.md)
  Overridden by subclasses to substitute another object for itself during archiving.
- [func replacementObject(for: NSCoder) -> Any?](nsobject-swift.class/replacementobject(for:)-2l8ox.md)
  Overridden by subclasses to substitute another object for itself during encoding.
- [func replacementObject(for: NSKeyedArchiver) -> Any?](nsobject-swift.class/replacementobject(for:)-60vwc.md)
  Overridden by subclasses to substitute another object for itself during keyed archiving.
- [class func setVersion(Int)](nsobject-swift.class/setversion(_:).md)
  Sets the receiver’s version number.
- [class func version() -> Int](nsobject-swift.class/version.md)
  Returns the version number assigned to the class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classfallbacksforkeyedarchiver())*