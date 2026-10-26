# classFallbacksForKeyedArchiver()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Overridden to return the names of classes that can be used to decode objects if their class is unavailable.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class func classFallbacksForKeyedArchiver() -> [String]
```

```objc
+ (NSArray<NSString *> *) classFallbacksForKeyedArchiver;
```

#### Return Value

An array of string objects that specify the names of classes in preferred order for unarchiving

#### Discussion

[`NSKeyedArchiver`](../../Foundation/nskeyedarchiver.md) calls this method and stores the result inside the archive. If the actual class of an object doesn’t exist at the time of unarchiving, [`NSKeyedUnarchiver`](../../Foundation/nskeyedunarchiver.md) goes through the stored list of classes and uses the first one that does exists as a substitute class for decoding the object. The default implementation of this method returns an empty array.

You can use this method if you introduce a new class into your application to provide some backwards compatibility in case the archive will be read on a system that does not have that class. Sometimes there may be another class which may work nearly as well as a substitute for the new class, and the archive keys and archived state for the new class can be carefully chosen (or compatibility written out) so that the object can be unarchived as the substitute class if necessary.

## See Also

### Archiving
- [func awakeAfter(using: NSCoder) -> Any?](./awakeafter%28using%29.md)
  Overridden by subclasses to substitute another object in place of the object that was decoded and subsequently received this message.
- [var classForArchiver: AnyClass?](./classforarchiver.md)
  The class to substitute for the receiver’s own class during archiving.
- [var classForCoder: AnyClass](./classforcoder.md)
  Overridden by subclasses to substitute a class other than its own during coding.
- [var classForKeyedArchiver: AnyClass?](./classforkeyedarchiver.md)
  Subclasses to substitute a new class for instances during keyed archiving.
- [class func classForKeyedUnarchiver() -> AnyClass](./classforkeyedunarchiver%28%29.md)
  Overridden by subclasses to substitute a new class during keyed unarchiving.
- [func replacementObject(for: NSArchiver) -> Any?](./replacementobject%28for%29-8ih2x.md)
  Overridden by subclasses to substitute another object for itself during archiving.
- [func replacementObject(for: NSCoder) -> Any?](./replacementobject%28for%29-2l8ox.md)
  Overridden by subclasses to substitute another object for itself during encoding.
- [func replacementObject(for: NSKeyedArchiver) -> Any?](./replacementobject%28for%29-60vwc.md)
  Overridden by subclasses to substitute another object for itself during keyed archiving.
- [class func setVersion(Int)](./setversion%28_%29.md)
  Sets the receiver’s version number.
- [class func version() -> Int](./version%28%29.md)
  Returns the version number assigned to the class.
- [classForPortCoder](./classforportcoder.md)
  Class to substitute for the receiver in distribution encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classfallbacksforkeyedarchiver())*