# version()

**Framework**: Objective-C Runtime  
**Kind**: method

Returns the version number assigned to the class.

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
class func version() -> Int
```

#### Return Value

The version number assigned to the class.

#### Discussion

If no version has been set, the default is `0`.

Version numbers are needed for decoding or unarchiving, so older versions of an object can be detected and decoded correctly.

Caution should be taken when obtaining the version from within an `NSCoding` protocol or other methods. Use the class name explicitly when getting a class version number:

```objc
version = [MyClass version];
```

Don’t simply send `version` to the return value of class—a subclass version number may be returned instead.

##### Special Considerations

The version number applies to `NSArchiver`/`NSUnarchiver`, but not to `NSKeyedArchiver`/`NSKeyedUnarchiver`.  A keyed archiver does not encode class version numbers.

## See Also

- [func version(forClassName: String) -> Int](../Foundation/NSCoder/version(forClassName:).md)
  This method is present for historical reasons and is not used with keyed archivers.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/version())*