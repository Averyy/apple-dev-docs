# classForKeyedUnarchiver()

**Framework**: Objective-C Runtime  
**Kind**: method

Overridden by subclasses to substitute a new class during keyed unarchiving.

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
class func classForKeyedUnarchiver() -> AnyClass
```

#### Return Value

The class to substitute for the receiver during keyed unarchiving.

#### Discussion

During keyed unarchiving, instances of the receiver will be decoded as members of the returned class. This method overrides the results of the decoder’s class and instance name to class encoding tables.

## See Also

- [func awakeAfter(using: NSCoder) -> Any?](nsobject-swift.class/awakeafter(using:).md)
  Overridden by subclasses to substitute another object in place of the object that was decoded and subsequently received this message.
- [var classForArchiver: AnyClass?](nsobject-swift.class/classforarchiver.md)
  The class to substitute for the receiver’s own class during archiving.
- [var classForCoder: AnyClass](nsobject-swift.class/classforcoder.md)
  Overridden by subclasses to substitute a class other than its own during coding.
- [var classForKeyedArchiver: AnyClass?](nsobject-swift.class/classforkeyedarchiver.md)
  Subclasses to substitute a new class for instances during keyed archiving.
- [class func classFallbacksForKeyedArchiver() -> [String]](nsobject-swift.class/classfallbacksforkeyedarchiver.md)
  Overridden to return the names of classes that can be used to decode objects if their class is unavailable.
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

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classforkeyedunarchiver())*