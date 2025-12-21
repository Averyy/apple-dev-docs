# classForArchiver

**Framework**: Objective-C Runtime  
**Kind**: property

The class to substitute for the receiver’s own class during archiving.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var classForArchiver: AnyClass? { get }
```

## See Also

- [func awakeAfter(using: NSCoder) -> Any?](nsobject-swift.class/awakeafter(using:).md)
  Overridden by subclasses to substitute another object in place of the object that was decoded and subsequently received this message.
- [var classForCoder: AnyClass](nsobject-swift.class/classforcoder.md)
  Overridden by subclasses to substitute a class other than its own during coding.
- [var classForKeyedArchiver: AnyClass?](nsobject-swift.class/classforkeyedarchiver.md)
  Subclasses to substitute a new class for instances during keyed archiving.
- [class func classFallbacksForKeyedArchiver() -> [String]](nsobject-swift.class/classfallbacksforkeyedarchiver.md)
  Overridden to return the names of classes that can be used to decode objects if their class is unavailable.
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

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classforarchiver)*